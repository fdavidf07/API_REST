from rest_framework import serializers
from .models import Espacio, Reserva
from django.utils import timezone

class EspacioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Espacio
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):
    usuario_nombre = serializers.ReadOnlyField(source='usuario.username')

    class Meta:
        model = Reserva
        fields = ['id', 'espacio', 'fecha', 'hora_inicio', 'hora_fin', 'usuario', 'usuario_nombre']
        read_only_fields = ['usuario']

    def validate(self, data):
        # 1. Validación de fecha pasada
        if data['fecha'] < timezone.now().date():
            raise serializers.ValidationError("No se puede reservar en una fecha que ya ha pasado.")

        # 2. Validación de solapamiento
        existe_solapamiento = Reserva.objects.filter(
            espacio=data['espacio'],
            fecha=data['fecha'],
            hora_inicio__lt=data['hora_fin'],
            hora_fin__gt=data['hora_inicio']
        ).exists()

        if existe_solapamiento:
            raise serializers.ValidationError("Lo sentimos, este espacio ya está reservado en ese horario.")
        return data

    def to_representation(self, instance):
        """MÁSCARA DE PRIVACIDAD: Oculta el usuario si no es Admin."""
        ret = super().to_representation(instance)
        request = self.context.get('request')
        if request and not (request.user.is_staff or request.user.groups.filter(name='Admins_Espacios').exists()):
            ret['usuario'] = "Privado"
            ret['usuario_nombre'] = "Usuario Registrado"
        return ret
from rest_framework import serializers
from .models import Espacio, Reserva

class EspacioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Espacio
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'

    def validate(self, data):
        # Ejecuta la validación de solapamiento de horarios
        reserva_temp = Reserva(**data)
        try:
            reserva_temp.clean()
        except Exception as e:
            raise serializers.ValidationError(e.message if hasattr(e, 'message') else str(e))
        return data
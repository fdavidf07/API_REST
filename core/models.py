from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class Espacio(models.Model):
    TIPOS = [('SALA', 'Sala de Juntas'), ('MESA', 'Puesto Individual')]
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=10, choices=TIPOS)
    capacidad = models.IntegerField()
    precio_hora = models.DecimalField(max_digits=6, decimal_places=2)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    espacio = models.ForeignKey(Espacio, on_delete=models.CASCADE)
    inicio = models.DateTimeField()
    fin = models.DateTimeField()

    def clean(self):
        # Lógica para detectar si el espacio está ocupado
        solapamientos = Reserva.objects.filter(
            espacio=self.espacio,
            inicio__lt=self.fin,
            fin__gt=self.inicio
        ).exclude(pk=self.pk)
        
        if solapamientos.exists():
            raise ValidationError('Lo sentimos, este espacio ya está reservado en ese horario.')

    def save(self, *args, **kwargs):
        self.full_clean() # Obliga a ejecutar el clean() antes de guardar
        super().save(*args, **kwargs)
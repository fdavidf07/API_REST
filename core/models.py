from django.db import models
from django.contrib.auth.models import User

class Espacio(models.Model):
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()

    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    espacio = models.ForeignKey(Espacio, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return f"{self.espacio.nombre} - {self.fecha}"
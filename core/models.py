from django.db import models

class Espacio(models.Model):
    TIPO_CHOICES = [
        ('MESA', 'Puesto Individual'),
        ('SALA', 'Sala de Reuniones'),
        ('OFICINA', 'Oficina Privada'),
    ]
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, default='MESA')
    capacidad = models.IntegerField(default=1)
    precio_hora = models.DecimalField(max_digits=6, decimal_places=2)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"

class Reserva(models.Model):
    espacio = models.ForeignKey(Espacio, on_delete=models.CASCADE)
    usuario = models.CharField(max_length=100)
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return f"Reserva de {self.usuario} en {self.espacio.nombre}"
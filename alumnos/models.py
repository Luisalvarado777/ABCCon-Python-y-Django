
from django.db import models
from datetime import datetime

class Alumno(models.Model):
    carnet = models.CharField(max_length=10, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo_electronico = models.EmailField()
    fecha_nacimiento = models.DateField()

    def calcular_edad(self):
        hoy = datetime.now().date()
        edad = hoy.year - self.fecha_nacimiento.year - ((hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))
        return edad

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
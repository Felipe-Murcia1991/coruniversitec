from django.db import models

# Create your models here.
class Empleado(models.Model):
    documento=models.IntegerField()
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    telefono=models.CharField(max_length=15)
    cargo=models.CharField(max_length=50)
    correo=models.EmailField()

class Elegir(models.Model):
    documento=models.ForeignKey(Empleado, on_delete=models.CASCADE)
    nombre=models.CharField(max_length=50)

from django.db import models

# Create your models here.
class Empleado(models.Model):
    id = models.AutoField(primary_key=True)
    documento=models.IntegerField()
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    telefono=models.IntegerField()
    cargo=models.CharField(max_length=50)
    correo=models.EmailField()

class Elegir(models.Model):
    
    documento=models.ForeignKey(Empleado, on_delete=models.CASCADE)
    nombre=models.CharField(max_length=50)

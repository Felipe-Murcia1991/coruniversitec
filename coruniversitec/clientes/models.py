from django.db import models

# Create your models here.
class Cliente(models.Model):
    folio=models.IntegerField(primary_key=True)
    documento=models.CharField(max_length=15)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    telefono=models.CharField(max_length=50)
    edad=models.IntegerField()
    correo=models.EmailField()
    postulado=models.CharField(max_length=50)

class Buscar(models.Model):
    folio=models.ForeignKey(Cliente, on_delete=models.CASCADE)
    documento=models.CharField(max_length=15)

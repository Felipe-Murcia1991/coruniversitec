from django.db import models

# Create your models here.
class Cliente(models.Model):
    folio=models.CharField(max_length=10,primary_key=True)
    documento=models.CharField(max_length=15)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    telefono=models.IntegerField()
    edad=models.IntegerField()
    correo=models.EmailField()
    

class Buscar(models.Model):
    folio=models.ForeignKey(Cliente, on_delete=models.CASCADE)
    documento=models.CharField(max_length=15)

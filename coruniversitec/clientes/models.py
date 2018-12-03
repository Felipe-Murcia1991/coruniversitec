from django.db import models

# Create your models here.
class Cliente(models.Model):
    folio=models.CharField(max_length=10,primary_key=True)
    documento=models.IntegerField()
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    telefono=models.IntegerField()
    edad=models.IntegerField()
    correo=models.EmailField()

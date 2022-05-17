
from django.db import models


# Create your models here.

class personaje(models.Model):
    id = models.IntegerField  (null=False , primary_key=True)
    nombre = models.CharField(null=False ,max_length=40)
    descripcion = models.CharField(null=True ,max_length=200)
    imagen = models.CharField(null=False ,max_length=500)
    extension = models.CharField(null=False ,max_length=4)
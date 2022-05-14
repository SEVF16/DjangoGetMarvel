from ast import mod
from mailbox import NoSuchMailboxError
from django.db import models
from django.forms import CharField, IntegerField

# Create your models here.

class personaje(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=200)
    imagen = models.CharField()
    extension = models.CharField(max_length=4)
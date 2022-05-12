from mailbox import NoSuchMailboxError
from django.db import models
from django.forms import CharField, IntegerField

# Create your models here.

class personaje(models.Model):
    id = IntegerField()
    nombre4 = CharField()
    descripcion =CharField()
    imagen = CharField()
    
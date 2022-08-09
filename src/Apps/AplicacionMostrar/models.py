from django.db import models
from django.contrib.auth.models import User
class Estudiante(models.Model):
    tutor  = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    id_estudiante = models.IntegerField()
    celular  = models.CharField(max_length=9)
    genero  = models.CharField(max_length=1)
    turno  = models.CharField(max_length=20)
    grado  = models.IntegerField(max_length=1)

# Create your models here.

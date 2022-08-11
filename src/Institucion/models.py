from operator import mod
from django.db import models

# Create your models here.
class Tutor(models.Model):
    codigoTutor = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    tipoDocumento = models.CharField(max_length=50)
    numDocumento = models.CharField(max_length=15)

    def nombre_completo(self):
        return "{}, {}".format(self.apellidos, self.nombres)
    def __str__(self):
        return self.nombre_completo()

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

class Alumno(models.Model):
    codigoAlumno = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=50, verbose_name='Nombres')
    apellidos = models.CharField(max_length=50)
    direccion = models.CharField(max_length=150)
    telefono = models.CharField(max_length=15)
    tipoDocumento = models.CharField(max_length=50)
    numDocumento = models.CharField(max_length=15)
    fechaNacimiento = models.DateField()
    codigoTutor = models.ForeignKey(Tutor, related_name='fk_alumno', on_delete=models.CASCADE)

    def nombre_completo(self):
        return "{}, {}".format(self.apellidos, self.nombres)
    def __str__(self):
        return self.nombre_completo()

 class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    tipoUsuario = models.CharField(max_length=100)
    def nombre_completo(self):
        return "{}, {}".format(self.apellidos, self.nombres)
    def __str__(self):
        return self.nombre_completo()


  class Profesor(models.Model):
    codigoProfesor = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    tipoDocumento = models.CharField(max_length=50)
    numDocumento = models.CharField(max_length=15)
    def nombre_completo(self):
    return "{}, {}".format(self.apellidos, self.nombres)
def __str__(self):
    return self.nombre_completo()


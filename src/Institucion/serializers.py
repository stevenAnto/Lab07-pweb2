from dataclasses import fields
from rest_framework import serializers
from Institucion.models import Alumno, Admin, Tutor, Profesor, Cursos, Matriculas, Honorarios

class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tutor
        fields='__all__'
        
class AlumnoSerializer(serializers.ModelSerializer):
    codigoTutor = TutorSerializer()
    class Meta:
        model=Alumno
        fields='__all__'
        #fields=('codigoAlumno', 'nombres', 'apellidos', 'direccion', 'telefono', 'tipoDocumento', 'numDocumento', 'fechaNacimiento', 'codigoTutor')

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model=Admin
        fields='__all__'
        #fields=('id', 'usuario', 'password', 'nombres', 'apellidos', 'tipoUsuario')

class AdminsGetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Admin
        fields=('id', 'usuario', 'nombres', 'apellidos', 'tipoUsuario')

class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profesor
        fields='__all__'

class CursosSerializer(serializers.ModelSerializer):
    fk_codigoProfesor = ProfesorSerializer()
    class Meta:
        model=Cursos
        fields='__all__'

class HonorariosSerializer(serializers.ModelSerializer):
    fk_codigoProfesor = ProfesorSerializer()
    class Meta:
        model=Honorarios
        fields='__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    codigoAlumno = AlumnoSerializer()
    codigoCurso = CursosSerializer()
    class Meta:
        model=Matriculas
        fields='__all__'


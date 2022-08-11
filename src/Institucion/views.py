from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Institucion.models import Alumno, Admin, Honorarios, Matriculas, Profesor, Cursos, Tutor
from Institucion.serializers import AlumnoSerializer, AdminSerializer, AdminsGetSerializer, HonorariosSerializer, MatriculaSerializer, ProfesorSerializer, CursosSerializer, TutorSerializer
from rest_framework import viewsets
# Create your views here.


class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer

class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

class ProfesorViewSet(viewsets.ModelViewSet):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Cursos.objects.all()
    serializer_class = CursosSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matriculas.objects.all()
    serializer_class = MatriculaSerializer

class HonorariosViewSet(viewsets.ModelViewSet):
    queryset = Honorarios.objects.all()
    serializer_class = HonorariosSerializer

class TutorViewSet(viewsets.ModelViewSet):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer

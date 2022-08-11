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

# #ALUMNOS
# @csrf_exempt
# def alumnoApi(request, codigoAlumno=0):
#     if request.method == 'GET':
#         alumnos = Alumno.objects.all()
#         alumnos_serializer = AlumnoSerializer(alumnos, many=True)
#         return JsonResponse(alumnos_serializer.data, safe=False)
#     elif request.method == 'POST':
#         alumno_data = JSONParser().parse(request)
#         alumno_serializer = AlumnoSerializer(data = alumno_data)
#         if alumno_serializer.is_valid():
#             alumno_serializer.save()
#             return JsonResponse("Alumno registrado exitosamente!!", safe=False)
#         return JsonResponse("Error al registrar alumno", safe=False)
#     elif request.method == 'PUT':
#         alumno_data = JSONParser().parse(request)
#         alumno_before = Alumno.objects.get(codigoAlumno = alumno_data['codigoAlumno'])
#         alumno_serializer = AlumnoSerializer(alumno_before, data = alumno_data)
#         if alumno_serializer.is_valid():
#             alumno_serializer.save()
#             return JsonResponse("Datos del alumno actualizado exitosamente!!", safe=False)
#         return JsonResponse("Error al actualizar los datos del alumno", safe=False)
#     elif request.method == 'DELETE':
#         alumno = Alumno.objects.get(codigoAlumno=codigoAlumno)
#         alumno.delete()
#         return JsonResponse("Alumno eliminado exitosamente!!", safe=False)

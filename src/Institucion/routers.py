from rest_framework.routers import DefaultRouter
from Institucion.views import AdminViewSet, AlumnoViewSet, CursoViewSet, HonorariosViewSet, MatriculaViewSet, ProfesorViewSet, TutorViewSet

router = DefaultRouter()
router.register(r'alumnos', AlumnoViewSet, basename='alumnos')
router.register(r'admin', AdminViewSet, basename='admin')
router.register(r'profesor', ProfesorViewSet, basename='profesor')
router.register(r'cursos', CursoViewSet, basename='curso')
router.register(r'matricula', MatriculaViewSet, basename='matriculas')
router.register(r'honorarios', HonorariosViewSet, basename='honorarios')
router.register(r'tutor', TutorViewSet, basename='tutor')
from django.urls import path
from . import views

urlpatterns = [
    path("cursos_disponibles/", views.cursos_disponibles, name="cursos_disponibles"),
    path("profesores/", views.profesores, name="profesores"),
    path("estudiantes/", views.estudiantes, name="estudiantes"),
]
"""
URL configuration for Mayorga_Entrega_Final project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from blog import views
from blog.views import EditarCursos, detalle_curso, BorrarCursos
from blog.views import detalle_profesor, EditarProfesor, BorrarProfesor
from blog.views import detalle_estudiante, EditarEstudiante, BorrarEstudiante

app_name="blog"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("index/", views.index, name="index"),
    path("about/", views.about, name="about"),
    path('pages/', include('blog.urls')),
    path('usuarios/', include('autenticacion.urls')),
    path("agregar_curso/", views.agregar_curso, name="agregar_curso"),
    path("agregar_profesor/", views.agregar_profesor, name="agregar_profesor"),
    path("agregar_estudiante/", views.agregar_estudiante, name="agregar_estudiante"),
    path("detalle_curso/<int:id>/", detalle_curso, name="detalle_curso"),
    path("borrar_curso/<int:pk>/", BorrarCursos.as_view(), name="borrar_curso"),
    path("editar_curso/<int:pk>/", EditarCursos.as_view(), name="editar_curso"),
    path("detalle_profesor.html/<int:id>/", detalle_profesor, name="detalle_profesor"),
    path("borrar_profesor/<int:pk>/", BorrarProfesor.as_view(), name="borrar_profesor"),
    path("editar_profesor/<int:pk>/", EditarProfesor.as_view(), name="editar_profesor"),
    path("detalle_estudiante.html/<int:id>/", detalle_estudiante, name="detalle_estudiante"),
    path("borrar_estudiante/<int:pk>/", BorrarEstudiante.as_view(), name="borrar_estudiante"),
    path("editar_estudiante/<int:pk>/", EditarEstudiante.as_view(), name="editar_estudiante"),
]
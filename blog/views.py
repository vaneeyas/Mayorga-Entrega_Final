from django.shortcuts import render, redirect
from .models import Curso
from .models import Profesor
from .models import Estudiante
from .forms import CursoForm
from .forms import ProfesorForm
from .forms import EstudianteForm

app_name="blog"

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def about(request):
    return render(request, 'blog/about.html')

def cursos_disponibles(request):
    curso = Curso.objects.all()
    return render(request, 'blog/cursos_disponibles.html', context={"cursos": curso})

def agregar_curso(request):
    if request.method=="POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            return redirect('cursos_disponibles')
    else:
        cursoForm = CursoForm()
    return render(request, 'blog/agregar_curso.html', context={"cursoForm": cursoForm})    


def profesores(request):
    profesor = Profesor.objects.all()
    return render(request, 'blog/profesores.html', context={"profesores": profesor})

def agregar_profesor(request):
    if request.method=="POST":
        form = ProfesorForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            return redirect('profesores')
    else:
        profesorForm = ProfesorForm()
    return render(request, 'blog/agregar_profesor.html', context={"profesorForm": profesorForm})   


def estudiantes(request):
    busqueda = request.GET.get("busqueda", None)
    if busqueda:
        estudiante = Estudiante.objects.filter(carrera__icontains=busqueda)
    else:
        estudiante = Estudiante.objects.all()
    return render(request, 'blog/estudiantes.html', context={"estudiantes": estudiante})

def agregar_estudiante(request):
    if request.method=="POST":
        form = EstudianteForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            return redirect('estudiantes')
    else:
        estudianteForm = EstudianteForm()
    return render(request, 'blog/agregar_estudiante.html', context={"estudianteForm": estudianteForm})   
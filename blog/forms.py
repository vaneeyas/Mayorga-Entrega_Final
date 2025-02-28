from django import forms
from .models import Curso
from .models import Profesor
from .models import Estudiante

class CursoForm(forms.ModelForm):
    class Meta:
        model= Curso
        fields = ['nombre', 'comision']
        
class ProfesorForm(forms.ModelForm):
    class Meta:
        model= Profesor
        fields = ['nombre', 'apellido', 'email', 'materia']
        
class EstudianteForm(forms.ModelForm):
    class Meta:
        model= Estudiante
        fields = ['nombre', 'apellido', 'email', 'carrera']
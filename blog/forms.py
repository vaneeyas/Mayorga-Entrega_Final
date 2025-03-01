from django import forms
from .models import Curso
from .models import Profesor
from .models import Estudiante

class CursoForm(forms.ModelForm):
    fecha_creacion = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model= Curso
        fields = ['nombre', 'comision', 'fecha_creacion']
        
class ProfesorForm(forms.ModelForm):
    class Meta:
        model= Profesor
        fields = ['nombre', 'apellido', 'email', 'materia']
        
class EstudianteForm(forms.ModelForm):
    class Meta:
        model= Estudiante
        fields = ['nombre', 'apellido', 'email', 'carrera']
        
class EditarCursoForm(forms.ModelForm):
    fecha_creacion = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = Curso
        fields = "__all__"

class EditarProfesorForm(forms.ModelForm):
        
    class Meta:
        model = Profesor
        fields = "__all__"
        
class EditarEstudianteForm(forms.ModelForm):
        
    class Meta:
        model = Estudiante
        fields = "__all__"
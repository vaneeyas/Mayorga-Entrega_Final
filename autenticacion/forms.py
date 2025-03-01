from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class UnRegistro(UserCreationForm):
    email = forms.EmailField(required=False)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)
    
    first_name= forms.CharField(label="Nombre", required=False)
    last_name= forms.CharField(label="Apellido", required=False)
    
    class Model:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
        help_texts = {field: "" for field in fields}
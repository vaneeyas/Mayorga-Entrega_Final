from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UnRegistro(UserCreationForm):
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)
    
    email = forms.EmailField(required=False)
    first_name = forms.CharField(label="Nombre", required=False)
    last_name = forms.CharField(label="Apellido", required=False)
    fecha_nacimiento = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    # first_name= forms.CharField(label="Nombre", required=True)
    # last_name= forms.CharField(label="Apellido", required=True)
    # fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)  # <-- esto es clave!

    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
        help_texts = {field: "" for field in fields}
        
        
    def save(self, commit=True):
        user = super().save(commit)
        if commit:
            profile = user.profile
            profile.fecha_nacimiento = self.cleaned_data.get('fecha_nacimiento')
            profile.save()
        return user
 
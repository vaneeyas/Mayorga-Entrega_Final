from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as django_login
from autenticacion.forms import UnRegistro
from django.contrib.auth.decorators import login_required
from .models import Profile

def login(request):
    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()
            django_login(request, usuario)
            return redirect("index")
    else:
        formulario = AuthenticationForm()  
    return render(request, "autenticacion/login.html", {'formulario': formulario})

def registrar(request):
    if request.method == "POST":
        form = UnRegistro(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("login")
    else:
        form = UnRegistro()
    return render(request, "autenticacion/registrar.html", {"form": form})

def profile(request):
    context = {
        'user': request.user,
        'profile': request.user.profile  # si usas un perfil extendido
    }
    return render(request, 'autenticacion/profile.html', context)

@login_required
def profile(request):
    context = {
        'user': request.user,
        'profile': request.user.profile  # si querés mostrar el perfil extendido
    }
    return render(request, 'autenticacion/profile.html', context)
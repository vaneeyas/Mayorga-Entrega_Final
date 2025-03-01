from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as django_login
from autenticacion.forms import UnRegistro

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
        formulario = UnRegistro(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("login")
    else:
        formulario = UnRegistro()
    return render(request, "autenticacion/registrar.html", {"formulario": formulario})
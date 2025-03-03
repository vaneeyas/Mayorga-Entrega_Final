from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as django_login
from autenticacion.forms import UnRegistro, EditaUnPerfil, EditarPerfilExtendido
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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

@login_required
def profile(request):
    profile = request.user.profile

    context = {
        'user': request.user,
        'profile': profile,
    }
    return render(request, 'autenticacion/profile.html', context)

@login_required
def editar_perfil(request):
    user = request.user
    profile = user.profile 
    
    if request.method == 'POST':
        form_user = EditaUnPerfil(request.POST, instance=user)
        form_profile = EditarPerfilExtendido(request.POST, request.FILES, instance=profile)

        if form_user.is_valid() and form_profile.is_valid():
            form_user.save()
            form_profile.save()
            messages.success(request, 'Perfil actualizado correctamente.')
            return redirect('profile')

    else:
        form_user = EditaUnPerfil(instance=user)
        form_profile = EditarPerfilExtendido(instance=profile)

    context = {
        'form_user': form_user,
        'form_profile': form_profile
    }
    return render(request, 'autenticacion/editar_perfil.html', context)
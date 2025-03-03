from django.urls import path
from django.contrib.auth.views import LogoutView
from autenticacion.views import login, registrar
from . import views
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from .views import CambiarContraseña

urlpatterns = [
    path('login/', login, name="login"),
    path('logout/', LogoutView.as_view(template_name="autenticacion/logout.html"), name="logout"),
    path('registrar/', registrar, name="registrar"),
    path('profile/', views.profile, name='profile'),
    path('editar-perfil/', views.editar_perfil, name='editar_perfil'),
    path('cambiar-password/', PasswordChangeView.as_view(template_name='autenticacion/cambiar_password.html'), name='cambiar_password'),
    path('cambiar-password-exito/', PasswordChangeDoneView.as_view(template_name='autenticacion/cambiar_password_exito.html'), name='password_change_done'),
    path('cambiar-password/', CambiarContraseña.as_view(), name='cambiar_password'),
]

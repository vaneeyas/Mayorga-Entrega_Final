from django.urls import path
from django.contrib.auth.views import LogoutView
from autenticacion.views import login, registrar

urlpatterns = [
    path('login/', login, name="login"),
    path('logout/', LogoutView.as_view(template_name="autenticacion/logout.html"), name="logout"),
    path('registrar/', registrar, name="registrar"),
]

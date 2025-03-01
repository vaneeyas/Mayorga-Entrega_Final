from django.urls import path
from django.contrib.auth.views import LogoutView

urlpatterns = [
    #path('login/', login, name="login"),
    path('logout/', LogoutView.as_view(template_name="autenticacion/logout.html"), name="logout"),
    #path('registro/', registro, name="registro"),
]

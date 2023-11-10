from django.urls import path
from .views import *
urlpatterns = [
    path("", home, name="home"),
    path("login/", LoginView.as_view(), name="login"),
    path("solicitud/", solicitud, name="solicitud"),
    path("medico/", medico, name="medico"),
    path("registropaciente/", registropaciente, name="registropaciente")
]


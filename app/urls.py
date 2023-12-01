from django.urls import path
from .views import *
urlpatterns = [
    path("", home, name="home"),
    path("login/", LoginView.as_view(), name="login"),
    path("solicitud/", SolicitudView.as_view(), name="solicitud"),
    path("paciente/", registropaciente, name="paciente"),
    path("medico/", medico, name="medico"),
    path("registropaciente/", registropaciente, name="registropaciente"),
    path("estudios/", estudios, name="estudios")
]


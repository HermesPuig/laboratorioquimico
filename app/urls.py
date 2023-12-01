from django.urls import path
from .views import *
urlpatterns = [
    path("", home, name="home"),
    path("login/", LoginView.as_view(), name="login"),
    path("solicitud/", SolicitudView.as_view(), name="solicitud"),
    path("solicitudext/<int:solicitud_id>/", SolicitudExtView.as_view(), name="solicitudext"),
    path("registropaciente/", RegPacienteView.as_view(), name="registropaciente"),
    path("estudios/", EstudiosView.as_view(), name="estudios"),
    path("resultado/", ResultadoView.as_view(), name="resultado"),
    path("resultado_final/", resultado_final, name="resultado_final"),
    path("extraccionista/", extraccionista, name="extraccionista"),
]


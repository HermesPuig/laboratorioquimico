from django.urls import path
from .views import *
urlpatterns = [
    path("", home, name="home"),
    path("login/", login, name="login"),
    path("solicitud/", solicitud, name="solicitud")
]

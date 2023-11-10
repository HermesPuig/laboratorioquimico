from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, View
from django.contrib.auth import *

# Create your views here.

def home(request):
    return render(request, "home.html")

def medico(request):
    return render(request,"medico.html")

def registropaciente(request):
    return render(request, "registropaciente.html")

def solicitud(request):
    return render(request, "solicitud.html")

class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        print(username, password)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, self.template_name, {'error_message': 'Credenciales inválidas'})

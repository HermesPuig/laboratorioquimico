from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, View
from django.contrib.auth import *
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import usuarioRecepcionista, usuario, Solicitud, medicos
from .forms import RecetaForm
from datetime import datetime
# Create your views here.

def home(request):
    return render(request, "home.html")

def medico(request):
    return render(request,"medico.html")

def registropaciente(request):
    return render(request, "registropaciente.html")

def estudios(request):
    return render(request, "estudios.html")

class LoginView(View):
    

    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        

        print(username, password)

        usuario = usuarioRecepcionista.objects.filter(username=username)
        if usuario:
            usuario = usuario.get()
            if usuario.password == password:
                return redirect('solicitud')
    
        return render(request, self.template_name, {'error_message': 'Credenciales inválidas'})

class SolicitudView(View):
    template_name = 'solicitud.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        
        MP = request.POST['MP']
        DNI = request.POST['DNIP']
        fechaForm = request.POST['fecha']


        print(MP, DNI, fechaForm)


        Paciente = usuario.objects.filter(documento=DNI)
        medico = medicos.objects.filter(MP=MP)
        
        if fechaForm:
            
            fecha = datetime.strptime(fechaForm, "%Y-%m-%d").date()

            if fecha:
                fecha_actual = datetime.now().date()
                diferencia_dias = (fecha_actual - fecha).days
        
        if Paciente and medico and fecha and diferencia_dias >= 0 and diferencia_dias <= 30:
            Paciente = Paciente.get()
            medico = medico.get()
            context = {'usuario': Paciente, 'medico':medico}
            nuevaSolicitud = Solicitud.objects.create(MP=MP, DNI=DNI, fecha=fecha)
            nuevaSolicitud.save()
            return render(request,'paciente.html', context)


        context = {'error_message': 'errores al procesar el formulario'}
        if not Paciente:
            context['error_paciente'] = 'El paciente no existe'
        if not medico:
            context['error_medico'] = 'El medico no existe'
        if not fecha:
            context['error_fecha'] = 'La fecha no es correcta'
        if diferencia_dias and diferencia_dias <= 0:
            context['error_diferencia'] = 'La fecha supera la fecha actual'
        elif diferencia_dias and diferencia_dias > 30:
            context['error_diferencia'] = 'La fecha supera los 30 dias'
            
        return render(request, self.template_name,context)

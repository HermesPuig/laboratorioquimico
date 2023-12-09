from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, View
from django.contrib.auth import *
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *
from .forms import RecetaForm
from datetime import datetime
from django.core.mail import send_mail

def home(request):
    return render(request, "home.html")

def extraccionista(request):
    solicitudes_activas = Solicitud.objects.filter(estado='activa')
    
    return render(request, "extraccionista.html", {'solicitudes': solicitudes_activas})

def medico(request):
    return render(request,"medico.html")

class RegPacienteView(View):
    template_name = 'registropaciente.html'
    
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        dni = request.POST['dni']
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        direccion = request.POST['direccion']
        email = request.POST['email']

        paciente_con_dni = Paciente.objects.filter(documento=dni).exists()
        paciente_con_email = Paciente.objects.filter(email=email).exists()

        if paciente_con_dni:
            return render(request, self.template_name, {'error_message': 'El DNI ya existe en la base de datos.'})
        if paciente_con_email:
            return render(request, self.template_name, {'error_message': 'El correo electrónico ya existe en la base de datos.'})

        else:
            try:
                paciente = Paciente.objects.create(nombre=nombre, apellido=apellido, email=email, descripcion='-', direccion=direccion, tipo_documento='DNI', documento=dni)
                return render(request, self.template_name, {'success_message': 'Paciente Creado.'})
            except:
                return render(request, self.template_name, {'error_message': 'Credenciales Inválidas.'})


class EstudiosView(View):
    template_name = 'estudios.html'
    
    def get(self, request):
        estudios = Estudio.objects.all()
        
        return render(request, self.template_name, {'estudios':estudios})

    def post(self, request):
        estudios = [int(key[7:]) for key in request.POST if key.startswith('estudio')]
        solicitud = Solicitud.objects.last() 
        estudios_list = []
        
        for i in range(len(estudios)):
            estudios_list.append(estudios[i])
        
        
        for estudio in estudios_list:
            solicitud.estudios.add(estudio)

        return redirect('solicitud')
    
    
class ResultadoView(View):
    template_name = 'resultado.html'
    
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        codigo = request.POST.get('codigo')
        
        try:
            solicitud = Solicitud.objects.get(id=codigo)
            return render(request, 'resultado_final.html', {'solicitud':  solicitud})
        except:
            return render(request, self.template_name, {'error_message':  'El codigo ingresado no existe.'})
    
def resultado_final(request):
    return render(request,"resultado_final.html")


    
class SolicitudExtView(View):
    template_name = 'solicitud_ext.html'
    
    def get(self, request, solicitud_id):
        solicitud = Solicitud.objects.get(id=solicitud_id)
        
        return render(request, self.template_name, {'solicitud': solicitud})
    
    
    def post(self, request, solicitud_id):
        solicitud = Solicitud.objects.get(id=solicitud_id)
        tus_estudios = Estudio.objects.all()

        values = [request.POST.get(f'value_{estudio.id}', '') for estudio in tus_estudios]
        
        for estudio, valor in zip(solicitud.estudios.all(), values):
            estudio.valor_hallado = valor
            estudio.save()



        solicitud.marcar_finalizada()
        
        return redirect('extraccionista')


class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            if user.is_recep == True:
                return redirect('solicitud')
            else:
                return redirect('solicitud')
        else:
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


        paciente = Paciente.objects.filter(documento=DNI)
        medico = medicos.objects.filter(MP=MP)
        
        try:
            fecha = datetime.strptime(fechaForm, "%Y-%m-%d").date()
            fecha_actual = datetime.now().date()
            diferencia_dias = (fecha_actual - fecha).days
        
        
            if paciente and medico and fecha and diferencia_dias >= 0 and diferencia_dias <= 30:
                paciente = paciente.get()
                medico = medico.get()
                try:
                    nuevaSolicitud = Solicitud.objects.create(MP=MP, DNI=DNI, fecha=fecha, paciente=paciente)
                    nuevaSolicitud.save()

                    return redirect('estudios')
                except:
                    context = {'error_message': 'Errores al procesar el formulario.'}
    

            context = {'error_message': 'Errores al procesar el formulario.'}
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

        except:
            context = {'error_message': 'Errores al procesar el formulario.'}
            return render(request, self.template_name,context)


def menu_recepcionista(request):
    return render(request,"menu_recepcionista.html")



def menu_extraccionista(request):
    return render(request,"menu_extraccionista.html")

class MyLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('home')


class ConsultaPacientesView(View):
    template_name = 'consulta_pacientes.html'
    
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        dni = request.POST.get('dni_paciente')
        
        try:
            paciente = Paciente.objects.get(documento=dni)
            return render(request, 'datos_paciente.html', {'paciente':  paciente})
        except:
            return render(request, self.template_name, {'error_message':  'El paciente no existe.'})

            
        


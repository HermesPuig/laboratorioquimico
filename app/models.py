from django.utils import timezone
from django.db import models
from django.core.exceptions import ValidationError


    
class Solicitud(models.Model):
    ESTADO_CHOICES = [
        ('activa', 'Activa'),
        ('finalizada', 'Finalizada'),
    ]

    MP = models.CharField (("nombre pedido:"),max_length=25)
    DNI = models.CharField (("descripcion pedido"),max_length=25)
    fecha =  models.DateField (max_length=25)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='activa')
    
    def marcar_finalizada(self):
        self.estado = 'finalizada'
        self.save()
    

class AnalisisDisponibles(models.Model):
    NombreAnalisis = models.CharField("Analisis Disponibles", max_length=100)
    descripcionAnalisis = models.CharField("Descripción del Analisis", max_length=300)

    def __str__(self) -> str:
        return self.NombreAnalisis

class RecetaPDF(models.Model):
    pdf_file = models.FileField(upload_to='pdfs/')
    
class Receta(models.Model):
    analisissolicitado = models.ForeignKey(AnalisisDisponibles, on_delete=models.CASCADE,max_length=30)
    medicamentosolicitado = models.CharField (max_length=25)
    nombremedico = models.CharField (max_length=25)
    fecha =  models.DateField (max_length=25)
    MP = models.CharField(max_length=25)
    def clean(self):
        # Validar la antigüedad de la receta
        if self.fecha < timezone.now().date() - timezone.timedelta(days=30):
            raise ValidationError('La receta no puede tener más de un mes de antigüedad.')

 


class mediciones(models.Model):
    nombremedicamento = models.CharField(max_length=25)
    cantML = models.CharField(max_length=25)
    
    def __str__(self) -> str:
        return self.nombremedicamento


class medicos(models.Model):
    nombremedico = models.CharField(max_length=25)
    especialidad = models.CharField(max_length=25)
    MP = models.CharField(max_length=25)


class usuarioRecepcionista(models.Model):
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=25)

class usuario(models.Model):
    nombre = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=25)
    documento = models.IntegerField()
    direccion = models.CharField(max_length=25)
    telefono = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)


    
class resultadopedidomedico(models.Model):
    nombre = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=25)
    
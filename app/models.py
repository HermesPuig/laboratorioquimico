from django.utils import timezone
from django.db import models
from django.core.exceptions import ValidationError

class Pedido(models.Model):
    nombre = models.CharField (("nombre pedido:"),max_length=25)
    descripcion = models.CharField (("descripcion pedido"),max_length=25)
    receta = models.ForeignKey (("receta pedido"),max_length=25)

class AnalisisDisponibles(models.Model):
    NombreAnalisis = models.CharField("Analisis Disponibles", max_length=100)
    descripcionAnalisis = models.CharField("Descripción del Analisis", max_length=300)

    def __str__(self) -> str:
        return self.NombreAnalisis

class Medico(models.Model):
    mp = models.CharField(max_length=25, unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

    
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

        # Validar la matrícula del médico utilizando un webservice (aquí simulado)
        medico = Medico.objects.filter(mp=self.mp).first()

        if not medico:
            raise ValidationError('No se encontró un médico con esa matrícula.')

        # Si es la primera vez que se recibe una receta de ese médico, registrar al médico
        if not Receta.objects.filter(mp=self.mp).exists():
            Medico.objects.create(mp=self.mp, nombre=medico.nombre, apellido=medico.apellido)



class mediciones(models.Model):
    nombremedicamento = models.CharField(max_length=25)
    cantML = models.CharField(max_length=25)
    
    def __str__(self) -> str:
        return self.nombremedicamento



class TipoDocumento(models.Model):
    nombreTipoDocumento = models.CharField("Tipo de Documento", max_length=100)
    descripcionTipoDocumento = models.CharField("Descripción del Tipo de Documento", max_length=200)

    def __str__(self) -> str:
        return self.nombreTipoDocumento
    


class usuario(models.Model):
    nombre = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=25)
    tipodocumento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    documento = models.IntegerField(max_length=25)
    direccion = models.CharField(max_length=25)
    telefono = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)


    
class resultadopedidomedico(models.Model):
    nombre = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=25)
    
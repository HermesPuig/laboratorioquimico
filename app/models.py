from django.db import models

class Pedido(models.Model):
    nombre = models.CharField (("nombre pedido:"),max_length=25)
    descripcion = models.CharField (("descripcion pedido"),max_length=25)
    receta = models.CharField (("receta pedido"),max_length=25)

class AnalisisDisponibles(models.Model):
    NombreAnalisis = models.CharField("Analisis Disponibles", max_length=100)
    descripcionAnalisis = models.CharField("Descripción del Analisis", max_length=300)

    def __str__(self) -> str:
        return self.NombreAnalisis
    
    
class receta(models.Model):
    analisissolicitado = models.ForeignKey(AnalisisDisponibles, on_delete=models.CASCADE,max_length=30)
    medicamentosolicitado = models.CharField (max_length=25)
    nombremedico = models.CharField (max_length=25)
    fecha =  models.DateField (max_length=25)
    MP = models.CharField(max_length=25)


class mediciones(models.Model):
    nombremedicamento = models.CharField(max_length=25)
    cantML = models.CharField(max_length=25)



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
    
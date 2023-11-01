from django.db import models

class Pedido(models.Model):
    nombre = models.CharField (("nombre pedido:"),max_length=25)
    descripcion = models.CharField (("descripcion pedido"),max_length=25)
    reseta = models.CharField (("reseta pedido"),max_length=25)

class reseta(models.Model):
    analisissolicitado = models.CharField (("analisis reseta"),max_length=25)
    medicamentosolicitado = models.CharField (max_length=25)
    nombremedico = models.CharField (max_length=25)
    fecha =  models.DateField (max_length=25)
    MP = models.CharField(max_length=25)

class mediciones(models.Model):
    nombremedicamento = models.CharField(max_length=25)
    cantML = models.CharField(max_length=25)

class usuario(models.Model):
    nombre = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=25)
    documento = models.CharField(max_length=25)
    direccion = models.CharField(max_length=25)
    telefono = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)

class resultadopedidomedico(models.Model):
    nombre = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=25)
    
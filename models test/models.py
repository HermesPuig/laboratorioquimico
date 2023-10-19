from django.db import models
 
class Recepcionista(models.Model):
    nombre = models.CharField(("Nombre Recepcionista:"),max_length=50)
    apellido = models.CharField(("Apellido Recepcionista:"),max_length=11)
    telefono = models.CharField(("Telefono"),max_length=11)
    email = models.EmailField(("Email Recepcionista:"),max_length=254)
    usuario = models.CharField(("Usuario Recepcionista:"),max_length=50)
    passw = models.CharField(("Contraseña Recepcionista:"),max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Paciente(models.Model):
    nombre = models.CharField(("Nombre Paciente:"),max_length=50)
    apellido = models.CharField(("Apellido Paciente:"),max_length=11)
    docmicilio = models.CharField(("Domicilio"),max_length=50)
    telefono = models.CharField(("Telefono"),max_length=11)
    email = models.EmailField(("Email Paciente:"),max_length=254)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Medico(models.Model):
    nombre = models.CharField(("Nombre Medico:"),max_length=50)
    apellido = models.CharField(("Apellido Medico:"),max_length=11)
    telefono = models.CharField(("Telefono"),max_length=11)
    email = models.EmailField(("Email Medico:"),max_length=254)
    matricula = models.CharField(("Matricula"),max_length=50)

    def __str__(self):
        return f" {self.pk} {self.nombre} {self.apellido}"

class Extraccionista(models.Model):
    nombre = models.CharField(("Nombre Extraccionista:"),max_length=50)
    apellido = models.CharField(("Apellido Extraccionista:"),max_length=11)
    telefono = models.CharField(("Telefono"),max_length=11)
    email = models.EmailField(("Email Extraccionista:"),max_length=254)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class SolicitudAnalisis(models.Model):
    ESTADO = ("Pendiente","Pendiente"),("Realizado","Realizado")
    
    num_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    num_medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    estado = models.CharField(("Estado"), max_length=50, choices=ESTADO)
    fecha_solicitud = models.DateField(("Fecha Solicitud"))
    fecha_receta = models.DateField(("Fecha Receta"))
    url_receta_pdf = models.CharField(("URL Receta PDF"),max_length=50)


class Estudio(models.Model):
    nombre = models.CharField(("Nombre Estudio:"),max_length=50)
    codigo = models.IntegerField(("Codigo:"))
    tecnica = models.CharField(("Tecnica:"), max_length=50)
    valor_referencia = models.CharField(("Valor de Referencia:"), max_length=50)
    descripcion = models.CharField(("Descripcion:"),max_length=50)

class Resultado(models.Model):
    solicitud_analisis = models.ForeignKey(SolicitudAnalisis, on_delete=models.CASCADE)
    valor_hallado = models.CharField(("Valor Hallado:"), max_length=50)
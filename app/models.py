from django.utils import timezone
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("El campo de nombre de usuario es obligatorio")
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("El superusuario debe tener is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("El superusuario debe tener is_superuser=True.")

        return self.create_user(username, password, **extra_fields)

    
    

class AnalisisDisponibles(models.Model):
    NombreAnalisis = models.CharField("Analisis Disponibles", max_length=100)
    descripcionAnalisis = models.CharField("Descripción del Analisis", max_length=300)

    def __str__(self) -> str:
        return self.NombreAnalisis


class RecetaPDF(models.Model):
    pdf_file = models.FileField(upload_to='pdfs/')
    
    
class Receta(models.Model):
    analisissolicitado = models.ForeignKey(AnalisisDisponibles, on_delete=models.CASCADE)
    medicamentosolicitado = models.CharField(max_length=25)
    nombremedico = models.CharField(max_length=25)
    fecha = models.DateField(max_length=25)
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


class Usuario(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    nombre = models.CharField(("Nombre"), max_length=50)
    apellido = models.CharField(("Apellido"), max_length=50)
    is_recep = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    USERNAME_FIELD = "username"

    objects = CustomUserManager()


class Paciente(models.Model):
    nombre = models.CharField(("Nombre"), max_length=50)
    apellido = models.CharField(("Apellido"), max_length=50)
    email = models.EmailField(("Email"), max_length=254, default='')
    descripcion = models.CharField(max_length=25)
    direccion = models.CharField(("Direccion"), max_length=50) 
    tipo_documento = models.CharField(("Tipo Documento"), max_length=50)
    documento = models.CharField(("Numero Documento"), max_length=50)


class resultadopedidomedico(models.Model):
    nombre = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=25)
    

class Estudio(models.Model):
    nombre = models.CharField(("Nombre"), max_length=50)
    codigo = models.CharField(("Codigo"), max_length=50)
    valor_ref_min = models.CharField(("Valor Referencia Minimo"), max_length=50)
    valor_ref_max = models.CharField(("Valor Referencia Maximo"), max_length=50)
    valor_hallado = models.CharField(("Valor Hallado"), max_length=50, null=True)
    unidad_medida = models.CharField(("Unidad de Medida"), max_length=10, null=True)

class Solicitud(models.Model):
    ESTADO_CHOICES = [
        ('activa', 'Activa'),
        ('finalizada', 'Finalizada'),
    ]

    MP = models.CharField(("nombre pedido:"),max_length=25)
    DNI = models.CharField(("descripcion pedido"),max_length=25)
    fecha =  models.DateField (max_length=26)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='activa')
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=True)
    estudios = models.ManyToManyField(Estudio, blank=True , related_name='estudios')

    def marcar_finalizada(self):
        self.estado = 'finalizada'
        self.save()



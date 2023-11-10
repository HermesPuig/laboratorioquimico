from django.db import models
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


class Pedido(models.Model):
    nombre = models.CharField (("nombre pedido:"),max_length=25)
    descripcion = models.CharField (("descripcion pedido"),max_length=25)
    receta = models.CharField (("receta pedido"),max_length=25)


class Receta(models.Model):
    analisissolicitado = models.CharField (("analisis receta"),max_length=25)
    medicamentosolicitado = models.CharField (max_length=25)
    nombremedico = models.CharField (max_length=25)
    fecha =  models.DateField (max_length=25)
    MP = models.CharField(max_length=25)


class Medicion(models.Model):
    nombremedicamento = models.CharField(max_length=25)
    cantML = models.CharField(max_length=25)


class ResultadoPedidoMedico(models.Model):
    nombre = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=25)
    
    def __str__(self):
        return f"{self.nombre}"


class Usuario(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    telefono = models.CharField(max_length=25)
    email = models.EmailField(("Email"), max_length=254)
    nombre = models.CharField(("Nombre"), max_length=50)
    apellido = models.CharField(("Apellido"), max_length=50)
    direccion = models.CharField(("Direccion"), max_length=50) 
    tipo_documento = models.CharField(("Tipo Documento"), max_length=50)
    numero_documento = models.CharField(("Numero Documento"), max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "nombre", "apellido", "tipo_documento", "numero_documento"]
    
    objects = CustomUserManager()

    def __str__(self):
        return f"{self.username} - {self.nombre} {self.apellido}"

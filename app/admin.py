from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(usuario)
admin.site.register(Solicitud)
admin.site.register(Receta)
admin.site.register(mediciones)
admin.site.register(AnalisisDisponibles)
admin.site.register(usuarioRecepcionista)
admin.site.register(medicos)
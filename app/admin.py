from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Usuario)
admin.site.register(Solicitud)
admin.site.register(Receta)
admin.site.register(mediciones)
admin.site.register(AnalisisDisponibles)
admin.site.register(Paciente)
admin.site.register(medicos)
admin.site.register(Estudio)
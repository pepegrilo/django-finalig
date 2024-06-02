# Register your models here.
# libreria/admin.py
from django.contrib import admin
from .models import Programa, Modalidad, Empresa, Estado, Estudiante, Asesor, Profesor, Jurado, TrabajoDeGrado, Actividad, Evaluacion

admin.site.register(Programa)
admin.site.register(Modalidad)
admin.site.register(Empresa)
admin.site.register(Estado)
admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Jurado)
admin.site.register(TrabajoDeGrado)
admin.site.register(Actividad)
admin.site.register(Evaluacion)
admin.site.register(Asesor)
from django.contrib import admin

from empresa.models import Empleado, Departamento, Habilidad

# Register your models here.
admin.site.register(Empleado)
admin.site.register(Departamento)
admin.site.register(Habilidad)
from django.contrib import admin
from .models import Empleado


class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('dni', 'nombre', 'apellidos', 'email', 'estado')

admin.site.register(Empleado, EmpleadoAdmin)
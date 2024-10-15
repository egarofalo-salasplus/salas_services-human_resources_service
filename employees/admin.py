from django.contrib import admin
from .models import Empleado


class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('dni', 'primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido', 'email', 'estado')

admin.site.register(Empleado, EmpleadoAdmin)
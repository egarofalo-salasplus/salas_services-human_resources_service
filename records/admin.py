from django.contrib import admin
from .models import Fichaje

class FichajedAdmin(admin.ModelAdmin):
    list_display = ("empleado", "empresa", "fecha", "tiempo_teorico", "tiempo_trabajado")

admin.site.register(Fichaje, FichajedAdmin)

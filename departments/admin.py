from django.contrib import admin
from .models import Departamento

class DepartmentoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "empresa")

admin.site.register(Departamento, DepartmentoAdmin)

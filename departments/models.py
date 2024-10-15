from django.db import models
from companies.models import Empresa
from django.contrib import admin

class Departamento(models.Model):
    departamento_id = models.AutoField(primary_key=True, db_column='departamento_id')
    nombre = models.CharField(max_length=100, db_column='nombre')
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, db_column='empresa_id')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'Dim_Departamento'

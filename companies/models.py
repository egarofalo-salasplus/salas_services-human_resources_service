from django.db import models
from django.contrib import admin


class Empresa(models.Model):
    empresa_id = models.AutoField(primary_key=True, db_column='empresa_id')
    nombre = models.CharField(max_length=100, db_column='nombre')
    CIF = models.CharField(max_length=10, null=True, db_column='CIF')
    direccion = models.ForeignKey('Direccion', on_delete=models.CASCADE, db_column='direccion_id')
    telefono = models.CharField(max_length=15, null=True, db_column='telefono')
    email = models.CharField(max_length=100, db_column='email')
    fecha_creacion = models.DateField(db_column='fecha_creacion', auto_now_add=True)
    estado_empresa = models.CharField(max_length=50, db_column='estado_empresa', default='Activa')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "Dim_Empresa"


class Direccion(models.Model):
    direccion_id = models.AutoField(primary_key=True, db_column='direccion_id')
    pais = models.CharField(max_length=50, db_column='pais')
    region = models.CharField(max_length=50, db_column='region')
    ciudad = models.CharField(max_length=50, db_column='cuidad')
    codigo_postal = models.CharField(max_length=10, db_column='codigo_postal')
    calle = models.CharField(max_length=100, db_column='calle')
    complemento = models.CharField(max_length=100, db_column='complemento')

    def __str__(self):
        return f"{self.calle}, {self.complemento}, {self.ciudad}, {self.pais}"

    class Meta:
        db_table = "Dim_Direccion"

# Registrar modelos para se editables en admin
admin.site.register(Empresa)
admin.site.register(Direccion)
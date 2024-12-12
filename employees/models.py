from django.db import models
from companies.models import Empresa, Direccion
from departments.models import Departamento
from django.contrib import admin

class Empleado(models.Model):
    empleado_id = models.AutoField(primary_key=True, db_column='empleado_id')
    nombre = models.CharField(max_length=50, db_column='nombre')
    apellidos = models.CharField(max_length=50, db_column='apellidos')
    dni = models.CharField(max_length=20, db_column='DNI')
    email = models.CharField(max_length=100, null=True, db_column='email')
    sexo = models.CharField(max_length=10, db_column='sexo')
    fecha_nacimiento = models.DateField(db_column='fecha_nacimiento')
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, db_column='empresa_id')
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE, db_column='direccion_id')
    centro = models.ForeignKey("CentroTrabajo", null=True, on_delete=models.CASCADE, db_column="centro_id")
    planta = models.ForeignKey("Planta", null=True, on_delete=models.CASCADE, db_column="planta_id")
    area = models.ForeignKey("Area", null=True, on_delete=models.CASCADE, db_column="area_id")
    departamento = models.ForeignKey(Departamento, null=True, on_delete=models.CASCADE, db_column="departamento_id")
    puesto = models.ForeignKey("PuestoTrabajo", null=True, on_delete=models.CASCADE, db_column="puesto_trabajo_id")
    telefono = models.CharField(max_length=15, null=True, db_column='telefono')
    telefono_corto = models.CharField(max_length=4, null=True, db_column='telefono_corto')
    usuario = models.CharField(max_length=50, null=True, db_column="usuario")
    estado = models.CharField(max_length=50, null=True, db_column='estado')
    fecha_baja = models.DateField(null=True, db_column='fecha_baja')
    motivo_baja = models.CharField(max_length=200, null=True, db_column="motivo_baja")
    caducidad_nie = models.DateField(null=True, db_column='caducidad_nie')
    categoria_convenio = models.CharField(max_length=50, null=True, db_column="categoria_convenio")
    categoria_salas = models.CharField(max_length=50, null=True, db_column="categoria_salas")
    sesame_id = models.CharField(max_length=50, null=True, db_column="sesame_id")

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

    class Meta:
        db_table = "Dim_Empleado"

class HistorialPuesto(models.Model):
    historial_puesto_id = models.AutoField(primary_key=True, db_column='historial_puesto_id')
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, db_column='empleado_id')
    puesto_trabajo = models.ForeignKey('PuestoTrabajo', on_delete=models.CASCADE, db_column='puesto_trabajo_id')
    fecha_inicio = models.DateField(db_column='fecha_inicio')
    fecha_fin = models.DateField(null=True, db_column='fecha_fin')

    def __str__(self):
        return self.puesto_trabajo

    class Meta:
        db_table = "Fact_Historial_Puestos"

class PuestoTrabajo(models.Model):
    puesto_trabajo_id = models.AutoField(primary_key=True, db_column='puesto_trabajo_id')
    nombre = models.CharField(max_length=100, db_column='nombre')
    area = models.ForeignKey('Area', on_delete=models.CASCADE, db_column='area_id')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "Dim_Puesto_Trabajo"

class Area(models.Model):
    area_id = models.AutoField(primary_key=True, db_column='area_id')
    nombre = models.CharField(max_length=100, db_column='nombre')
    departamento = models.ForeignKey('departments.Departamento', on_delete=models.CASCADE, db_column='departamento_id')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "Dim_Area"

class CentroTrabajo(models.Model):
    centro_trabajo_id = models.AutoField(primary_key=True, db_column='centro_trabajo_id')
    nombre = models.CharField(max_length=100, db_column='nombre')
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE, db_column='direccion_id')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "Dim_Centro_Trabajo"

class Planta(models.Model):
    planta_id = models.AutoField(primary_key=True, db_column='planta_id')
    num_planta = models.IntegerField(db_column="num_planta")
    centro_trabajo = models.ForeignKey(CentroTrabajo, on_delete=models.CASCADE, db_column='centro_trabajo_id')

    def __str__(self):
        return str(self.num_planta)

    class Meta:
        db_table = "Dim_Planta"


# Employees se agrega desde employees/admin
admin.site.register(HistorialPuesto)
admin.site.register(PuestoTrabajo)
admin.site.register(Area)
admin.site.register(CentroTrabajo)
admin.site.register(Planta)

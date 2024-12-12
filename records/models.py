from django.db import models
from employees.models import Empleado, PuestoTrabajo
from companies.models import Empresa
from departments.models import Departamento
from django.contrib import admin

class Fichaje(models.Model):
    fichaje_id = models.AutoField(primary_key=True, db_column='fichaje_id')
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, db_column='empleado_id')
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, db_column='empresa_id')
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, db_column='departamento_id')
    fecha = models.DateField(null=True, db_column='fecha')
    tiempo_teorico = models.DecimalField(max_digits=20, decimal_places=2, null=True, db_column='tiempo_teorico')
    tiempo_trabajado = models.DecimalField(max_digits=20, decimal_places=2, null=True, db_column='tiempo_trabajado')

    def __str__(self):
        return f"{self.fecha}: {self.empleado} - Trabajado {self.tiempo_trabajado}"

    class Meta:
        db_table = "Fact_Fichajes"

class Imputacion(models.Model):
    imputacion_id = models.AutoField(primary_key=True, db_column='imputacion_id')
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, db_column='empleado_id')
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, db_column='empresa_id')
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, db_column='departamento_id')
    fecha = models.DateField(null=True, db_column='fecha')
    tarea = models.CharField(max_length=500, null=True, db_column='tarea')
    cliente = models.CharField(max_length=100, null=True, db_column='cliente')
    proyecto = models.CharField(max_length=100, null=True, db_column='proyecto')
    etiqueta = models.CharField(max_length=100, null=True, db_column='etiqueta')
    precio_hora = models.DecimalField(max_digits=20, decimal_places=2, null=True, db_column='precio_hora')
    horas_imputadas = models.DecimalField(max_digits=20, decimal_places=2, null=True, db_column='horas_imputadas')

    def __str__(self):
        return f"{self.fecha}: {self.empleado} - Tarea: {self.tarea}"

    class Meta:
        db_table = "Fact_Imputaciones"

class Alta(models.Model):
    alta_id = models.AutoField(primary_key=True, db_column="alta_id")
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, db_column='empleado_id')
    fecha_alta = models.DateField(db_column='fecha_alta')
    puesto_trabajo = models.ForeignKey(PuestoTrabajo, on_delete=models.CASCADE, db_column="puesto_trabajo_id")
    
    def __str__(self):
        return f"Fecha de alta: {self.fecha_alta} - (ID Empleado: {self.empleado})"

    class Meta:
        db_table = "Fact_Altas"

class Baja(models.Model):
    baja_id = models.AutoField(primary_key=True, db_column='baja_id')
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, db_column='empleado_id')
    fecha_baja = models.DateField(db_column='fecha_baja')
    motivo_baja = models.CharField(max_length=255, null=True, db_column='motivo_baja')

    def __str__(self):
        return f"{self.fecha_baja} - {self.motivo_baja} ({self.empleado})"

    class Meta:
        db_table = "Fact_Bajas"

class Evaluacion(models.Model):
    evaluation_id = models.AutoField(primary_key=True, db_column='evaluacion_id')
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, db_column='empleado_id')
    fecha_evaluacion = models.DateField(db_column='fecha_evaluacion')
    puntaje = models.IntegerField(db_column='puntaje')
    comentarios = models.TextField(null=True, db_column='comentarios')

    def __str__(self):
        return f"{self.fecha_evaluacion}: {self.empleado} - Calificación: {self.puntaje}"

    class Meta:
        db_table = "Fact_Evaluaciones"

admin.site.register(Imputacion)
admin.site.register(Alta)
admin.site.register(Baja)
admin.site.register(Evaluacion)

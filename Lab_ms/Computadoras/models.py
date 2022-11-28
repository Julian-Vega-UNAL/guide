from django.db import models


class Procesador(models.Model):
    Id_procesador =  models.IntegerField(primary_key=True)
    Nombre_procesador = models.CharField(max_length=50)

    def __str__(self):
        return str(f"{self.Id_procesador}: {self.Nombre_procesador}")
    
class Empresa(models.Model):
    Id_empresa = models.IntegerField(primary_key=True)
    Nombre_empresa = models.CharField(max_length=50)
    Sede_central =  models.CharField(max_length=50)
    Tipo = models.CharField(max_length=20)
    Sitio_web =  models.CharField(max_length=100)
    
    def __str__(self):
        return str(f"{self.Id_empresa}: {self.Nombre_empresa}")
    
# Create your models here.
class Computadoras(models.Model):
    Id_computadora = models.IntegerField(primary_key=True)
    Nombre_computadora = models.CharField(max_length=50)
    Medidas =  models.DecimalField(max_digits=3, decimal_places=2)
    Procesador = models.ForeignKey(Procesador, null=True, blank = True, on_delete=models.CASCADE)
    RAM = models.IntegerField()
    Disco_solido = models.IntegerField()
    Color = models.CharField(max_length=30)
    Unidades_disponibles = models.IntegerField()
    Empresa = models.ForeignKey(Empresa, null=True, blank = True, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(f"{self.Id_computadora}: {self.Nombre_computadora}")
    
    
    
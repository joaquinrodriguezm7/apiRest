from django.db import models

# Create your models here.

class Usuario (models.Model):
    id_usuario = models.IntegerField(primary_key=True, verbose_name='id_usuario')
    nombre_usuario = models.CharField(max_length=50, verbose_name='Nombre del Usuario',null=False,blank=False)
    password_usuario = models.CharField(max_length=50, verbose_name='Password del Usuario',null=False,blank=False)
    def __str__(self):
        return str(self.nombre_usuario)
    
class Vehiculo (models.Model):
    patente = models.CharField(primary_key=True, max_length=6, verbose_name='Patente del Vehiculo')
    marca = models.CharField(max_length=30, verbose_name='Marca del Vehiculo')
    modelo = models.CharField(max_length=30, verbose_name='Modelo  del Vehiculo')
    categoria = models.CharField(max_length=30, verbose_name='Categoria del Vehiculo')
    def __str__(self):
        return str(self.patente)

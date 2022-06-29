from django.db import models

# Create your models here.

class Productos(models.Model):

    nombre = models.CharField(max_length=30)
    cantidad = models.IntegerField()


class Empleados(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)


class Clientes(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    telefono = models.IntegerField()

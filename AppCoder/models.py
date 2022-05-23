from django.db import models

class Productor(models.Model):
    nombre=models.CharField(max_length=255)
    apellido=models.CharField(max_length=255)
    email=models.EmailField()
    provincia=models.CharField(max_length=255)
    descripcion=models.TextField()
    cultivo=models.CharField(max_length=255)

    class Meta():
        verbose_name='Productors'
        verbose_name_plural='Productores'



class AsesorTecnico(models.Model):
    nombre=models.CharField(max_length=255)
    apellido=models.CharField(max_length=255)
    email=models.EmailField()
    provincia=models.CharField(max_length=255)
    descripcion=models.TextField()
    cultivo=models.CharField(max_length=255)

class AgroComercio(models.Model):
    nombre=models.CharField(max_length=255)
    razonSocial=models.CharField(max_length=255)
    email=models.EmailField()
    ubicacion=models.CharField(max_length=255)
    direccion=models.CharField(max_length=255)
    descripcion=models.TextField()
    cultivo=models.CharField(max_length=255)
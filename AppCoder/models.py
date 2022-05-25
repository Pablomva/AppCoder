from django.db import models

class Productores(models.Model):
    nombre=models.CharField(max_length=255)
    apellido=models.CharField(max_length=255)
    email=models.EmailField()
    provincia=models.CharField(max_length=255)
    descripcion=models.TextField()
    cultivo=models.CharField(max_length=255)

    class Meta:
        verbose_name = "Productores"
        verbose_name_plural = "Productores"

class AsesoresTecnicos(models.Model):
    nombre=models.CharField(max_length=255)
    apellido=models.CharField(max_length=255)
    email=models.EmailField()
    provincia=models.CharField(max_length=255)
    descripcion=models.TextField()
    cultivo=models.CharField(max_length=255)

    class Meta:
        verbose_name = "Asesores Tecnicos"
        verbose_name_plural = "Asesores Tecnicos"

class AgroComercios(models.Model):
    nombre=models.CharField(max_length=255)
    razonSocial=models.CharField(max_length=255)
    email=models.EmailField()
    ubicacion=models.CharField(max_length=255)
    direccion=models.CharField(max_length=255)
    descripcion=models.TextField()
    cultivo=models.CharField(max_length=255)

    class Meta:
        verbose_name = "Agro Comercios"
        verbose_name_plural = "Agro Comercios" 
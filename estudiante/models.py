#encoding: utf-8
from django.db import models

# Create your models here.
class Cargo(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

class Grado(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

class Asignatura(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

class SecretariaEducacion(models.Model):
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return (u"%s"%self.nombre)

class CertificacionTIC(models.Model):
    estudiante = models.ForeignKey('campus.Estudiante')
    nombre = models.CharField(max_length=100, verbose_name="nombre de la certificación")
    entidad = models.CharField(max_length=100, verbose_name="entidad certificadora")
    fecha = models.DateTimeField(verbose_name="fecha de la certificación")

    def __unicode__(self):
        return (u"%s"%self.nombre)

class ProgramaTIC(models.Model):
    estudiante = models.ForeignKey('campus.Estudiante')
    nombre = models.CharField(max_length=100, verbose_name="nombre del programa")
    fecha = models.DateTimeField(verbose_name="fecha de la participación en el programa")

    def __unicode__(self):
        return (u"%s"%self.nombre)
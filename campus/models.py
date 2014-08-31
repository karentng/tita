#encoding: utf-8
from django.db.models import *
from convocat.models import Municipio


OPCIONES_GRADO = (  # son enteros, crear campo como IntegerField(choices=OPCIONES_GRADO)
    ( 1, u'Primero'),
    ( 2, u'Segundo'),
    ( 3, u'Tercero'),
    ( 4, u'Cuarto'),
    ( 5, u'Quinto'),
    ( 6, u'Sexto'),
    ( 7, u'Septimo'),
    ( 8, u'Octavo'),
    ( 9, u'Noveno'),
    (10, u'Decimo'),
    (11, u'Once'),
)


class InstitucionEducativa(Model):
    municipio = ForeignKey(Municipio)
    nombre = CharField(max_length=200)

#Corresponde a los formadores de formadores
class Formador(models.Model):    
    nombre1 = models.CharField( max_length=255, verbose_name='primer nombre')
    nombre2 = models.CharField( max_length=255, blank=True, verbose_name='segundo nombre')
    apellido1 = models.CharField( max_length=255, verbose_name='primer apellido')
    apellido2 = models.CharField( max_length=255, blank=True, verbose_name='segundo apellido')
    aspirante = models.ForeignKey(Aspirante, verbose_name='aspirante', null=True, blank=True)	
    usuario = models.OneToOneField(User)

class Curso(models.Model):
	descripcion = models.CharField
	institucion = models.ForeignKey(Institucion, verbose_name='institucion')

#Corresponde a los Maestros Estudiantes
class Estudiante(models.Model):
	nombre1 = models.CharField( max_length=255, verbose_name='primer nombre')
    nombre2 = models.CharField( max_length=255, blank=True, verbose_name='segundo nombre')
    apellido1 = models.CharField( max_length=255, verbose_name='primer apellido')
    apellido2 = models.CharField( max_length=255, blank=True, verbose_name='segundo apellido')
    formador = models.ForeignKey(Formador, verbose_name='formador', null=True)
    curso = models.ForeignKey(Curso, verbose_name='curso', null=True)

class Clase(models.Model):
	#fecha




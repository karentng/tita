#encoding: utf-8

from django.db import models
from convocat.models import Municipio, Aspirante
from django.contrib.auth.models import User


INSTITUCIONES = (
    (1, 'INEM Jorge Isaac'),
    (2, 'Liceo Departamental'),
    (3, 'Profesional'),
    (4, 'IETI Comuna 17'),
    (5, 'Normal Superior Farallones de Cali'),
    (6, 'Celmira Bueno de Orejuela'),
    (7, 'Otro')
)

CARGOS = (
    ('R', 'Rector'),
    ('C', 'Coordinador'),
    ('D', 'Docente')
)

ASIGNATURAS = (
    (1, 'Ciencias Naturales y Educación Ambiental'),
    (2, 'Ciencias Sociales, Historia, Geografía, Constitución Política y Democracia'),
    (3, 'Educación Artística'),
    (4, 'Educación Ética y en Valores Humanos'),
    (5, 'Educación Física, Recreación y Deporte'),
    (6, 'Educación Religiosa'),
    (7, 'Humanidades, Lenguas Castellana e Idiomas Extranjeros'),
    (8, 'Matemáticas'),
    (9, 'Tecnología e Informática'),
    (10, 'Todas')
)

GRADOS = (
    ('P', 'Prejardín'),
    ('J', 'Jardín'),
    ('T', 'Transición'),
    ('PRIMARIA',
        (('1', 'Primero'),
        ('2', 'Segundo'),
        ('3', 'Tercero'),
        ('4', 'Cuarto'),
        ('5', 'Quinto'))),
    ('BÁSICA SECUNDARIA',
        (('6', 'Sexto'),
        ('7', 'Séptimo'),
        ('8', 'Octavo'),
        ('9', 'Noveno'))),
    ('MEDIA VOCACIONAL',
        (('10', 'Décimo'),
        ('11', 'Once'),
        ('F', 'Programa de Formación Complementaria')))
)

JORNADAS = (
    ('M', 'Mañana'),
    ('T', 'Tarde'),
    ('A', 'Mañana y Tarde')
)

class InstitucionEducativa(models.Model):
    municipio = models.ForeignKey(Municipio)
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

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

#Corresponde a los formadores de formadores
class Formador(models.Model):    
    nombre1 = models.CharField( max_length=255, verbose_name='primer nombre')
    nombre2 = models.CharField( max_length=255, blank=True, verbose_name='segundo nombre')
    apellido1 = models.CharField( max_length=255, verbose_name='primer apellido')
    apellido2 = models.CharField( max_length=255, blank=True, verbose_name='segundo apellido')
    aspirante = models.ForeignKey(Aspirante, verbose_name='aspirante', null=True, blank=True)   
    usuario = models.OneToOneField(User)

    def __unicode__(self):
        return (u"%s %s %s %s"%(self.nombre1,self.nombre2 or '', self.apellido1, self.apellido2 or '')).strip() or "-"

class Curso(models.Model):
    descripcion = models.CharField(max_length=255, verbose_name=u'descripción del curso')
    institucion = models.ForeignKey(InstitucionEducativa, verbose_name='institucion')
    formador = models.ForeignKey(Formador)

    def __unicode__(self):
        return self.descripcion

#Corresponde a los Maestros Estudiantes    
class Estudiante(models.Model):
    numero_documento = models.BigIntegerField(unique=True, verbose_name='número documento')
    nombre1 = models.CharField( max_length=255, verbose_name='primer nombre')
    nombre2 = models.CharField( max_length=255, blank=True, verbose_name='segundo nombre')
    apellido1 = models.CharField( max_length=255, verbose_name='primer apellido')
    apellido2 = models.CharField( max_length=255, blank=True, verbose_name='segundo apellido')
    sexo = models.CharField( choices=[('M','Hombre'), ('F', 'Mujer')], max_length=1, verbose_name='sexo')
    
    telefono = models.BigIntegerField(null=True, blank=True, verbose_name=u'teléfono fijo')
    celular = models.BigIntegerField(null=True, blank=True, verbose_name=u'número de celular')
    email = models.EmailField()
    
    formador = models.ForeignKey(Formador, verbose_name='formador', null=True)
    curso = models.ForeignKey(Curso, verbose_name='curso', null=True)

    instituciones = models.ManyToManyField(InstitucionEducativa)
    cargos = models.ManyToManyField(Cargo)
    asignaturas = models.ManyToManyField(Asignatura)
    grados = models.ManyToManyField(Grado)
    jornada = models.CharField(choices=JORNADAS, max_length=1)

    def __unicode__(self):
        return (u"%s %s %s %s"%(self.nombre1,self.nombre2 or '', self.apellido1, self.apellido2 or '')).strip() or "-"

class Clase(models.Model):
    fecha_programada = models.DateTimeField(verbose_name=u'fecha de realización')
    curso = models.ForeignKey(Curso)
    
class Asistencia(models.Model):
    formador = models.ForeignKey(Formador)
    estudiante = models.ForeignKey(Estudiante)
    asistio = models.BooleanField(verbose_name=u'¿Asistió?')
from django.db import models
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

class InstitucionEducativa(models.Model):
    municipio = models.ForeignKey(Municipio)
    nombre = models.CharField(max_length=200)

class Estudiante(models.Model):

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
            ('4', 'Cuarto'))),
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

    numero_documento = models.BigIntegerField(unique=True, verbose_name='número documento')
    nombre1 = models.CharField( max_length=255, verbose_name='primer nombre')
    nombre2 = models.CharField( max_length=255, blank=True, verbose_name='segundo nombre')
    apellido1 = models.CharField( max_length=255, verbose_name='primer apellido')
    apellido2 = models.CharField( max_length=255, blank=True, verbose_name='segundo apellido')

    sexo = models.CharField( choices=[('M','Hombre'), ('F', 'Mujer')], max_length=1, verbose_name='sexo')
    
    telefono = models.BigIntegerField(null=True, blank=True, verbose_name=u'teléfono fijo')
    celular = models.BigIntegerField(null=True, blank=True, verbose_name=u'número de celular')
    email = models.EmailField()



    institucion = models.IntegerField(choices=INSTITUCIONES, verbose_name=u'Institución donde labora actualmente')
    cargo = models.CharField(choices=CARGOS, max_length=1, verbose_name='cargo')
    asignatura = models.IntegerField(choices=ASIGNATURAS, verbose_name='asignatura')

    modificado = models.DateTimeField(null=True, auto_now=True)
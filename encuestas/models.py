#encoding: utf-8
from django.db.models import *
from convocat.models import Municipio
from estudiante.models import InstitucionEducativa, OPCIONES_GRADO
# Create your models here.

OPCIONES_JORNADA = (('M', u'Mañana'), ('T', u'Tarde'))

OPCIONES_NIVEL_EDUCATIVO = (
    ('PI', u'Primaria Incompleta'),
    ('PC', u'Primaria Completa'),
    ('SI', u'Secundaria Incompleta'),
    ('SC', u'Secundaria Completa'),
    ('TI', u'Técnica Incompleta'),
    ('TC', u'Técnica Completa'),
    ('TNI', u'Tecnológica Incompleta'),
    ('TNC', u'Tecnológica Completa'),
    ('UI', u'Universidad Incompleta'),
    ('UC', u'Universidad Completa'),
    ('PGR', u'Posgrado'),
)

OPCIONES_OCUPACION = (
    ('EMP', u'Empresario'),
    ('COM', u'Comerciante (propietario de tienda de comestibles o de pequeño negocio de venta de productos o servicios)'),
    ('EST', u'Trabajador del Estado'),
    ('TEC', u'Técnico (trabajador asalariado o independiente con calificación técnica como electricista, mecanico, soldador, panadero)'),
    ('OBR', u'Obrero (trabajador no calificado y asalariado, por ejemplo, obrero de construcción o de una fábrica)'),
    ('ARTSN', u'Artesano (carpintero, costurera, sastre, zapatero)'),
    ('ARTIS', u'Artista (productor en áreas como pintura, música, escritura, escultura, artesanía, actuación)'),
    ('SERPER', u'Empleado de servicios personales (trabajadoras del hogar, vigilantes, conductor asalariado, mensajero)'),
    ('INF', u'Trabajador Informal'),
    ('HOG', u'Oficios del Hogar (tareas domésticas del propio hogar)'),
    ('JUB', u'Jubilado'),
    ('DESEM', u'Desempleado'),
)


class EncuestaPadreFamilia(Model):
    fecha = DateTimeField(auto_now_add=True)
    numero = IntegerField()
    jornada = CharField(max_length=1, choices=OPCIONES_JORNADA, help_text='Jornada en la que estudia su hijo')
    nombre = CharField(max_length=300, help_text='Nombres y Apellidos')
    parentesco = CharField(max_length=100, blank=True, help_text='Si usted no es el padre o la madre del estudiante, indique el parentesco que tiene con él/ella')
    municipio_nacimiento = ForeignKey(Municipio, null=True, blank=True)
    fecha_nacimiento = DateField()
    barrio = CharField(max_length=100, verbose_name=u'Barrio donde reside actualmente')
    institucion = ForeignKey(InstitucionEducativa, verbose_name=u'Institución educativa en la que estudia su hijo(a)')
    grado = IntegerField(choices=OPCIONES_GRADO)
    nivel_educativo = CharField(max_length=5, choices=OPCIONES_NIVEL_EDUCATIVO)
    titulo = CharField(max_length=100, blank=True, verbose_name=u'título obtenido')
    ocupacion = CharField(max_length=5, choices=OPCIONES_OCUPACION)

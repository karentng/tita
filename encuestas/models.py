#encoding: utf-8
from django.db.models import *
from multiselect import MultiSelectField
from convocat.models import Municipio
from campus.models import InstitucionEducativa, GRADOS
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

OPCIONES_FRECUENCIA_USO = (
    ('4', u'De 4 a 7 días a la semana'),
    ('3', u'3 días a la semana'),
    ('2', u'2 días a la semana'),
    ('1', u'1 día a la semana'),
    ('CN', u'Casi nunca'),
    ('N', u'Nunca'),
)

OPCIONES_AYUDA_INTERNET = (
    ('FAC', u'Es más fácil para él/ella'),
    ('IGU', u'Da lo mismo'),
    ('DIF', u'Es más dificil para él/ella')
)

OPCIONES_CLASE_CON_INTERNET = (
    (1, u'Serían más interesantes'),
    (2, u'Le entendería más al profesor'),
    (3, u'Daría lo mismo'),
    (4, u'Sería más facil aprender'),
    (5, u'Se distraería con más facilidad'),
)
# ('', u''),


OPCIONES_ACUERDO = (
    ('ACU', u'De acuerdo'),
    ('DESAC', u'Ni de acuerdo ni en desacuerdo'),
    ('NEUTR', u'En desacuerdo'),
)


class Materia(Model):
    nombre = CharField(max_length=100)

    def __unicode__(self):
        return self.nombre
        

class MejoraMateriaPadre(Model):
    encuesta = ForeignKey('EncuestaPadreFamilia')
    materia = ForeignKey(Materia)
    puntos = IntegerField(choices=((1,1),(2,2),(3,3)))


class EncuestaPadreFamilia(Model):
    fecha = DateTimeField(auto_now_add=True)
    #numero = IntegerField()
    jornada = CharField(max_length=1, choices=OPCIONES_JORNADA, help_text='Jornada en la que estudia su hijo')
    nombre = CharField(max_length=300, help_text='Nombres y Apellidos')
    parentesco = CharField(max_length=100, blank=True, help_text='Si usted no es el padre o la madre del estudiante, indique el parentesco que tiene con él/ella')
    municipio_nacimiento = ForeignKey(Municipio, null=True, blank=True)
    fecha_nacimiento = DateField()
    barrio = CharField(max_length=100, verbose_name=u'Barrio donde reside actualmente')
    institucion = ForeignKey(InstitucionEducativa, verbose_name=u'Institución educativa en la que estudia su hijo(a)')
    grado = IntegerField(choices=GRADOS)
    nivel_educativo = CharField(max_length=5, choices=OPCIONES_NIVEL_EDUCATIVO, default='x')
    titulo = CharField(max_length=100, blank=True, verbose_name=u'título obtenido')
    ocupacion = CharField(max_length=5, choices=OPCIONES_OCUPACION, default='x')

    frecuencia_uso_computador = CharField(max_length=5, choices=OPCIONES_FRECUENCIA_USO, verbose_name=u'¿Actualmente usa computador? ¿Con qué frecuencia lo usa?', default='x')
    frecuencia_uso_internet = CharField(max_length=5, choices=OPCIONES_FRECUENCIA_USO, verbose_name=u'¿Actualmente usa internet? ¿Con qué frecuencia lo usa?', default='x')

    ayuda_internet = CharField(max_length=5, choices=OPCIONES_AYUDA_INTERNET, verbose_name=u'¿Qué opina sobre que su hijo(a) haga las tareas con ayuda de Internet?', default='x')
    cualidades_clase_internet = MultiSelectField(max_length=50, choices=OPCIONES_CLASE_CON_INTERNET, verbose_name=u'¿Cómo cree que serían las clases que recibe su hijo si utilizara internet?', help_text="Puede marcar varias opciones")

    angustia_evolucion = CharField(max_length=5, choices=OPCIONES_ACUERDO, verbose_name=u'Me genera angustia la evolución que han tenido los computadores y la Internet', default='x')
    dispersan_atencion = CharField(max_length=5, choices=OPCIONES_ACUERDO, verbose_name=u'El computador y la Internet dispersan la atención de los estudiantes', default='x')
    limitan_capacidad = CharField(max_length=5, choices=OPCIONES_ACUERDO, verbose_name=u'El computador y la Internet limitan la capacidad de creación de los estudiantes.', default='x')
    bajo_puntaje_pisa = CharField(max_length=5, choices=OPCIONES_ACUERDO, verbose_name=u'Con respecto al bajo puntaje en lectura que obtuvieron los estudiantes caleños en las pruebas PISA (398), una persona expresó lo siguiente: "Lo que encuentran por Internet son textos cortos, sin ortografía, hoy a un joven le cuesta mucho hacerse entender por escrito, hay problemas de interpretación y argumentación"', default='x')
    razon_pisa = TextField(blank=True)


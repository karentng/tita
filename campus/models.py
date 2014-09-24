
#encoding: utf-8

from django.db import models
from convocat.models import Municipio, Aspirante
from django.contrib.auth.models import User
from estudiante.models import Cargo, Grado, Asignatura, SecretariaEducacion, CertificacionTIC

"""" esto se esta usando en algun lado???
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
"""


class InstitucionEducativa(models.Model):
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return (u"%s"%self.nombre)

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



"""
#Horarios disponibles
DIAS=(
    (1, 'Lunes'),
    (2, 'Martes'),
    (3, 'Miércoles'),
    (4, 'Jueves'),
    (5, 'Viernes')
)
class HorarioClase(models.Model):
    dia = models.IntegerField(choices=DIAS, verbose_name="dia de clase")
    inicio = models.TimeField(auto_now=False)
    fin = models.TimeField(auto_now=False)
    grado = models.ForeignKey(Grado)
"""

#Corresponde a los Maestros Estudiantes 
class Estudiante(models.Model):
    
    NIVEL_EDUCATIVO = (
        (1, 'Sin título'),
        (2, 'Bachiller académico con profundización en pedagogía'),
        (3, 'Técnico o tecnólogo en educación'),
        (4, 'Técnico o tecnólogo en otras áreas'),
        (5, 'Profesional o licenciado en educación'),
        (6, 'Profesional en otras áreas, no licenciado'),
        (7, 'Postgrado en educación'),
        (8, 'Postgrado en otras áreas')
    )

    numero_documento = models.BigIntegerField(unique=True, verbose_name='número de documento de identidad *')
    #municipio_documento = models.ForeignKey(Municipio, verbose_name='municipio de expedición')
    nombre1 = models.CharField( max_length=255, verbose_name='primer nombre *')
    nombre2 = models.CharField( max_length=255, blank=True, verbose_name='segundo nombre')
    apellido1 = models.CharField( max_length=255, verbose_name='primer apellido *')
    apellido2 = models.CharField( max_length=255, blank=True, verbose_name='segundo apellido')
    sexo = models.CharField( choices=[('M','Hombre'), ('F', 'Mujer')], max_length=1, verbose_name='genero *')
    email = models.EmailField(verbose_name="email personal *")
    email_institucional = models.EmailField(blank=True, null=True)
    municipio = models.ForeignKey(Municipio, verbose_name='municipio de residencia', null=True)
    telefono = models.BigIntegerField(null=True, blank=True, verbose_name=u'teléfono fijo')
    celular = models.BigIntegerField(null=True, blank=True, verbose_name=u'número de celular')
    direccion = models.CharField(verbose_name="dirección *", max_length=100)
    nivel_educativo = models.IntegerField(choices=NIVEL_EDUCATIVO, verbose_name="último nivel educativo aprobado *")
    acta_compromiso = models.NullBooleanField()

    curso = models.ForeignKey(Curso, verbose_name='curso *', null=True, blank=True)

    aprobo = models.NullBooleanField()
    
    def __unicode__(self):
        return (u"%s %s %s %s"%(self.nombre1,self.nombre2 or '', self.apellido1, self.apellido2 or '')).strip() or "-"

    def numero_inscripcion(self):
        mihash = (self.numero_documento*44383)%1000000007
        clave = "%d-%d"%(self.id, mihash)
        return clave

"""   
class Horario(models.Model):
    DIAS = (
        (1, 'Lunes'),
        (2, 'Martes'),
        (3, 'Miércoles'),
        (4, 'Jueves'),
        (5, 'Viernes')
    )
    estudiante = models.ForeignKey(Estudiante)
    dia = models.IntegerField(choices=DIAS, verbose_name="día de la semana")
    inicio = models.TimeField(verbose_name="hora inicial")
    fin = models.TimeField(verbose_name="hora final")
    curso = models.ForeignKey(Asignatura)
"""

class Clase(models.Model):

    SEDES = (
        ('INEM JORGE ISAACS',
            ((1, 'Principal INEM JORGE ISAACS'),
            (2,  'Satelite CECILIA MUÑOZ RICAURTE'),
            (3,  'Satelite LAS AMERICAS'),
            (4,  'Satelite CAMILO TORRES'),
            (5,  'Satelite CENTRO EDUCATIVO DEL NORTE'),
            (6,  'Satelite FRAY DOMINGO DE LAS CASAS'),
            (7,  'Satelite PABLO EMILIO'))),
        ('ANTONIO JOSE CAMACHO',
            ((8, 'Principal ANTONIO JOSE CAMACHO'),
            (9, 'Satelite REPUBLICA DEL PERU'),
            (10, 'Satelite MARCO FIDEL SUAREZ'),
            (11, 'Satelite OLGA LUCIA LLOREDA'))),
        ('NORMAL. SUPERIOR SANTIAGO DE CALI',
            ((12, 'Principal NORMAL. SUPERIOR SANTIAGO DE CALI'),
            (13,  'Satelite JOAQUIN DE CAYZEDO Y CUERO'))),
        ('GOLONDRINAS PRINCIPAL',
            ((14, 'Principal GOLONDRINAS PRINCIPAL'),
            (15,  'Satelite ANTONIO BARBERENA'))),
        ('CARLOS HOLGUIN MALLARINO',
            ((16, 'Principal CARLOS HOLGUIN MALLARINO'),
            (17,  'Satelite NIÑO JESUS DE ATOCHA'),
            (18,  'Satelite MIGUEL DE POMBO'))),
        ('MANUEL MARIA MALLARINO',
            ((19, 'Principal MANUEL MARIA MALLARINO'),
            (20, 'Satelite LAURA VICUÑA'),
            (21, 'Satelite LOS PINOS'),
            (22, 'Satelite CARLOS HOLGUIN SARDI'))),
        ('EL DIAMANTE',
            ((23, 'Principal EL DIAMANTE'),
            (24, 'Satelite JUAN PABLO II'))),
        ('EUSTAQUIO PALACIOS',
            ((25, 'Principal EUSTAQUIO PALACIOS'),
            (26, 'Satelite    LUIS LOPEZ MESA'),
            (27, 'Satelite    CELANESE'),
            (28, 'Satelite    MANUEL MARIA BUENAVENTURA'),
            (29, 'Satelite    MARISCAL JORGE ROBLEDO'),
            (30, 'Satelite    MIGUEL ANTONIO CARO'),
            (31, 'Satelite    GENERAL ANZOATEGUI'),
            (32, 'Satelite    TULIO ENRIQUE TASCON'),
            (33, 'Satelite    SANTIAGO RENGIFO'),
            (34, 'Satelite    SOFIA CAMARGO'))),
        ('JOSE MARIA CARBONELL',
            ((35, 'Principal JOSE MARIA CARBONELL'),
            (36, 'Satelite HONORIO VILLEGAS'))),
        ('MARICE SINISTERRA',
            ((38, 'Principal MARICE SINISTERRA'),
            (39, 'Satelite FENALCO ASTURIAS'))),
        (37, 'Principal IE BOYACA'),
        (40, 'Principal YUMBO-IE MAYOR DE YUMBO - SEDE PRINCIPAL'),
        (41, 'Principal YUMBO-IE JOSÉ MARÍA CÓRDOBA - SEDE PRINCIPAL'),
        (42, 'Principal YUMBO-IE TITAN - SEDE PRINCIPAL'),
        (43, 'Principal YUMBO-IE CEAT GENERAL PIERO MARIOTTI - SEDE JOHN F. KENNEDY'),
        (44, 'Principal YUMBO-IE MANUEL MARÍA SÁNCHEZ - SEDE PRINCIPAL'),
        (45, 'Principal YUMBO-IE ROSA ZÁRATE DE PEÑA - SEDE PRINCIPAL'),
        (46, 'Principal VIJES')
    )

    nombre = models.CharField(max_length=255, null=True, blank=True)
    institucion = models.IntegerField(choices=SEDES, max_length=2, verbose_name="institución", null=True, blank=True)
    fecha_inicio = models.DateTimeField(verbose_name=u'fecha y hora de inicio')
    fecha_finalizacion = models.DateTimeField(verbose_name=u'fecha y hora de finalización')
    modificado = models.DateTimeField(auto_now=True)
    curso = models.ForeignKey(Curso, null=True, blank=True)
    asistentes = models.ManyToManyField(Estudiante, blank=True, verbose_name='Seleccione las personas que asistieron a la clase')
    descripcion = models.CharField( max_length=1000, null=True, blank=True, verbose_name="descripción")
    tipo = models.CharField( max_length=10) # para especificar si es de diplomado o de acompanamiento in situ
    def __unicode__(self):
        return unicode(self.nombre)

"""
class Asistencia(models.Model):
    clase = models.ForeignKey(Clase)
    estudiante = models.ForeignKey(Estudiante)
    asistio = models.BooleanField(default=False)
    modificado = models.DateTimeField(auto_now=True)
"""

class SoporteClase(models.Model):
    clase = models.ForeignKey(Clase)
    archivo = models.FileField(upload_to="soportesclases/%Y%m%d_")
    

class Actividad(models.Model):
    clase = models.ForeignKey(Clase)
    descripcion = models.CharField(max_length=100)


class CalificacionActividad(models.Model):
    class Meta:
        unique_together = [('estudiante','actividad'),]
        
    estudiante = models.ForeignKey(Estudiante)
    actividad = models.ForeignKey(Actividad)
    nota = models.FloatField()
    observacion = models.TextField()

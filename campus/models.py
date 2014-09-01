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
    ('C', 'Completa'),
    ('M', 'Mañana'),
    ('T', 'Tarde'),
    ('N', 'Nocturna')
)

class InstitucionEducativa(models.Model):
    nombre = models.CharField(max_length=100)
    rector = models.CharField(max_length=100, null=True)
    principal = models.ForeignKey("self", null=True)

    def __unicode__(self):
        return (u"%s"%self.nombre)

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

    numero_documento = models.BigIntegerField(unique=True, verbose_name='número documento')
    nombre1 = models.CharField( max_length=255, verbose_name='primer nombre')
    nombre2 = models.CharField( max_length=255, blank=True, verbose_name='segundo nombre')
    apellido1 = models.CharField( max_length=255, verbose_name='primer apellido')
    apellido2 = models.CharField( max_length=255, blank=True, verbose_name='segundo apellido')
    sexo = models.CharField( choices=[('M','Hombre'), ('F', 'Mujer')], max_length=1, verbose_name='genero')
    email = models.EmailField()
    email_institucional = models.EmailField()
    municipio = models.ForeignKey(Municipio, verbose_name='municipio de residencia', null=True)
    telefono = models.BigIntegerField(null=True, blank=True, verbose_name=u'teléfono fijo')
    celular = models.BigIntegerField(null=True, blank=True, verbose_name=u'número de celular')
    direccion = models.CharField(verbose_name="dirección", max_length=100)
    nivel_educativo = models.IntegerField(choices=NIVEL_EDUCATIVO, verbose_name="último nivel educativo aprobado")

    formador = models.ForeignKey(Formador, verbose_name='formador', null=True)
    curso = models.ForeignKey(Curso, verbose_name='curso', null=True)

    aprobo = models.NullBooleanField()
    
    def __unicode__(self):
        return (u"%s %s %s %s"%(self.nombre1,self.nombre2 or '', self.apellido1, self.apellido2 or '')).strip() or "-"

class SecretariasEducacion(models.Model):
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return (u"%s"%self.nombre)

class CertificacionTIC(models.Model):
    estudiante = models.ForeignKey(Estudiante)
    nombre = models.CharField(max_length=100, verbose_name="nombre de la certificación")
    entidad = models.CharField(max_length=100, verbose_name="entidad certificadora")
    fecha = models.DateTimeField(verbose_name="fecha de la certificación")

    def __unicode__(self):
        return (u"%s"%self.nombre)

class ProgramasTIC(models.Model):
    estudiante = models.ForeignKey(Estudiante)
    nombre = models.CharField(max_length=100, verbose_name="nombre del programa")
    fecha = models.DateTimeField(verbose_name="fecha de la participación en el programa")

    def __unicode__(self):
        return (u"%s"%self.nombre)

class DatosLaborales(models.Model):

    estudiante = models.ForeignKey(Estudiante)

    secretaria_educacion = models.ForeignKey(SecretariasEducacion)
    institucion_educativa = models.ForeignKey(InstitucionEducativa)
    cargos = models.IntegerField(choices=[(1, 'Docente'), (2, 'Directivo Docente')], verbose_name="cargo")
    sector = models.CharField( choices=[('O','Oficial'), ('N', 'No Oficial')], max_length=1, verbose_name='sector')
    zona = models.CharField( choices=[('R','Rural'), ('U', 'Urbana'), ('N', 'N.A')], max_length=1, verbose_name='zona')
    jornada = models.CharField(choices=JORNADAS, max_length=1)

    grados = models.ManyToManyField(Grado)
    asignaturas = models.ManyToManyField(Asignatura)
    decreto_docente = models.IntegerField( choices=[(1,'D.L 1278 de 2002'), (2, 'D.L 2277 de 1979')], max_length=1, verbose_name='decreto profesional docente')
    #grado escalafon
    nombramiento = models.IntegerField(choices=[(1,'Propiedad'), (2, 'Período de Prueba'), (3, 'Provisional')], max_length=1, verbose_name='tipo de nombramiento')

    etnoeducador = models.BooleanField(verbose_name="se desempeña como etnoeducador")
    tipo_etnoeducador = models.IntegerField(choices=[(1, 'Raizal'),(2, 'Afrocolombiano'),(3, 'Indígena'), (4, 'N.A')], null=True)
    poblacion_etnica = models.CharField(max_length="100", verbose_name="poblacion étnica que atiende", null=True)
    
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

class Clase(models.Model):
    fecha_programada = models.DateTimeField(verbose_name=u'fecha de realización')
    curso = models.ForeignKey(Curso)
    
class Asistencia(models.Model):
    formador = models.ForeignKey(Formador)
    estudiante = models.ForeignKey(Estudiante)
    asistio = models.BooleanField(verbose_name=u'¿Asistió?')

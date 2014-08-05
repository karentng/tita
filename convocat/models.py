#encoding:utf-8
from django.db import models

# Create your models here.

class TipoSimple(models.Model):
    class Meta:
        abstract=True

    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre


class TipoDocumento(TipoSimple):
    pass

class TipoTitulo(models.Model):
    nombre = models.CharField(max_length=100)
    puntaje = models.IntegerField()

    def __unicode__(self):
        return self.nombre

class TipoFormacion(models.Model):
    nombre = models.CharField(max_length=100)
    puntaje = models.IntegerField()

    def __unicode__(self):
        return self.nombre


class TipoConocimiento(TipoSimple):
    pass

class TipoIdioma(TipoSimple):
    pass

class TipoFormador(TipoSimple):
    pass

class RangoTiempo(TipoSimple):
    pass

class Departamento(models.Model):
    nombre = models.CharField( max_length=255, verbose_name='Nombre')
    codigo = models.CharField( max_length=10, null=True, verbose_name='Código')
    latitud = models.FloatField(null=True)
    longitud = models.FloatField(null=True)

    def __unicode__(self):
        return self.nombre

class Municipio(models.Model):
    nombre = models.CharField( max_length=255, verbose_name='Nombre')
    departamento = models.ForeignKey(Departamento, verbose_name='Departamento')
    codigo = models.CharField( max_length=10, null=True, verbose_name='Código')
    latitud = models.FloatField(null=True)
    longitud = models.FloatField(null=True)

    def __unicode__(self):
        return self.nombre

class Aspirante(models.Model):    
    tipo_documento = models.ForeignKey(TipoDocumento, verbose_name='tipo de documento')
    numero_documento = models.CharField( max_length=128, unique=True, verbose_name='número documento')
    nombre1 = models.CharField( max_length=255, verbose_name='Primer Nombre')
    nombre2 = models.CharField( max_length=255, blank=True, null=True, verbose_name='segundo nombre')
    apellido1 = models.CharField( max_length=255, verbose_name='Primer Apellido')
    apellido2 = models.CharField( max_length=255, blank=True, null=True, verbose_name='segundo apellido')
    genero = models.CharField( choices=[('M','Hombre'), ('F', 'Mujer')], max_length=1, verbose_name='sexo')
    nacionalidad = models.CharField( max_length=255, null=True, blank=True, verbose_name='nacionalidad')
    fecha_nacimiento = models.DateField(verbose_name='fecha de nacimiento')
    municipio_nacimiento = models.ForeignKey(Municipio, verbose_name='municipio de nacimiento', related_name='municipio_n')
    direccion = models.CharField( max_length=100, verbose_name='Dirección')
    municipio = models.ForeignKey(Municipio, verbose_name='municipio', null=True)
    telefono = models.IntegerField()
    celular = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    puntuacion_hv = models.IntegerField()

    def __unicode__(self):
        return (u"%s %s %s %s"%(self.nombre1,self.nombre2 or '', self.apellido1, self.apellido2 or '')).strip() or "-"

class FormacionAcademica(models.Model):
    aspirante = models.ForeignKey(Aspirante)
    modalidad = models.ForeignKey(TipoTitulo, verbose_name='título obtenido')
    numero_semestres = models.IntegerField()
    titulo = models.CharField(max_length=255, verbose_name='título')
    fecha_terminacion = models.DateField(verbose_name='fecha de finalización')
    tarjeta_profesional = models.CharField(max_length=255)

    def __unicode__(self):
        return self.titulo


class FormacionTics(models.Model):

    CURSOS_FORMACION_TICS = (
        ('40', 'Curso TIC mínimo 40 horas'),
        ('90', 'Cursos TIC  hasta 90 horas'),
        ('140', 'Cursos TIC hasta 140 horas certificados o en proceso de certificación'),
        ('141', 'Cursos TIC mas 140 horas')
    )
    aspirante = models.OneToOneField(Aspirante)
    curso = models.ForeignKey(TipoFormacion, verbose_name='título obtenido')

    def __unicode__(self):
        return self.curso

class ConocimientosEspecificos(models.Model):

    HABILIDAD_CONOCIMIENTO = (
        ('1', 'Regular'),
        ('2', 'Bueno'),
        ('3', 'Muy bueno'),
    ) 

    aspirante = models.ForeignKey(Aspirante)

    conocimiento1 = models.CharField(max_length=50, verbose_name='Conocimiento y manejo de herramientas ofimáticas', choices=HABILIDAD_CONOCIMIENTO)
    conocimiento2 = models.CharField(max_length=50, verbose_name='Conocimiento y manejo de herramientas  Web 2', choices=HABILIDAD_CONOCIMIENTO)
    conocimiento3 = models.CharField(max_length=50, verbose_name='Conocimiento herramientas de edición multimedia', choices=HABILIDAD_CONOCIMIENTO)
    conocimiento4 = models.CharField(max_length=50, verbose_name='Experiencia en desarrollo de contenidos educativos digitales', choices=HABILIDAD_CONOCIMIENTO)
    conocimiento5 = models.CharField(max_length=50, verbose_name='Experiencia en desarrollo de libros de texto digital', choices=HABILIDAD_CONOCIMIENTO)
    conocimiento6 = models.CharField(max_length=50, verbose_name='Experiencia en procesos de e-learning', choices=HABILIDAD_CONOCIMIENTO)
    conocimiento7 = models.CharField(max_length=50, verbose_name='Experiencia en gestión de proyectos educativos TIC', choices=HABILIDAD_CONOCIMIENTO)
    conocimiento8 = models.CharField(max_length=50, verbose_name='Experiencia en desarrollo de elementos de evaluación de competencias.', choices=HABILIDAD_CONOCIMIENTO)
    calificacion = models.CharField(max_length=50, verbose_name='calificación')

    def __unicode__(self):
        return self.conocimiento


class IdiomasManejados(models.Model):

    HABILIDAD_IDIOMA = (
        ('1', 'Regular'),
        ('2', 'Bueno'),
        ('3', 'Muy bueno'),
    )

    aspirante = models.OneToOneField(Aspirante)
    idioma = models.ForeignKey(TipoIdioma, verbose_name='idioma', help_text=u"Sólo se pueden ingresar un idioma diferente al español.")
    habla = models.CharField(max_length=50, verbose_name='habilidad hablando', choices=HABILIDAD_IDIOMA)
    lee = models.CharField(max_length=50, verbose_name='habilidad leyendo', choices=HABILIDAD_IDIOMA)
    escribe = models.CharField(max_length=50, verbose_name='habilidad escribiendo', choices=HABILIDAD_IDIOMA)
    calificacion = models.CharField(max_length=50, verbose_name='calificación')

    def __unicode__():
        return self.idioma

class ExperienciaFormadorTics(models.Model):
    EXP_EST = (
        ('1', 'De 1 a 2 años'),
        ('2', 'De 2 a 3  años '),
        ('3', 'De 3 a 5 años'),
        ('4', 'Más de 5 años'),
    )
    EXP_DOC = (
        ('1', 'De 80 a 200 horas'),
        ('2', 'De 200 a 300 horas'),
        ('3', 'De 300 a 450 horas'),
        ('4', 'Más de 450 horas'),
    )
    EXP_FOR = (
        ('1', 'De 80 a 120 horas'),
        ('2', 'Más de 120 horas'),
    )
    aspirante = models.ForeignKey(Aspirante)
    formador_est = models.CharField(max_length=50, verbose_name='formación tic a estudiantes', choices=EXP_EST)
    formador_doc = models.CharField(max_length=50, verbose_name='formación tic a docentes', choices=EXP_DOC)
    formador_for = models.CharField(max_length=50, verbose_name='formación tic a profesores', choices=EXP_FOR)
    calificacion = models.CharField(max_length=50, verbose_name='calificación')

    def __unicode__():
        return self.formador


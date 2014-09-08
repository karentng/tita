# encoding:utf-8
import random, string, os
from django.db import models
from dateutil.relativedelta import relativedelta
from datetime import date

class Departamento(models.Model):
    nombre = models.CharField( max_length=255, verbose_name='nombre')
    codigo = models.CharField( max_length=10, null=True, verbose_name='código')
    latitud = models.FloatField(null=True)
    longitud = models.FloatField(null=True)

    def __unicode__(self):
        return self.nombre


class Municipio(models.Model):
    nombre = models.CharField( max_length=255, verbose_name='nombre')
    departamento = models.ForeignKey(Departamento, verbose_name='departamento')
    codigo = models.CharField( max_length=10, null=True, verbose_name='código')
    latitud = models.FloatField(null=True)
    longitud = models.FloatField(null=True)

    def __unicode__(self):
        return self.nombre


class Aspirante(models.Model):    
    numero_documento = models.BigIntegerField(unique=True, verbose_name='número documento')
    nombre1 = models.CharField( max_length=255, verbose_name='primer nombre')
    nombre2 = models.CharField( max_length=255, blank=True, verbose_name='segundo nombre')
    apellido1 = models.CharField( max_length=255, verbose_name='primer apellido')
    apellido2 = models.CharField( max_length=255, blank=True, verbose_name='segundo apellido')

    sexo = models.CharField( choices=[('M','Hombre'), ('F', 'Mujer')], max_length=1, verbose_name='sexo')
    nacionalidad = models.CharField( max_length=255, blank=True, verbose_name='nacionalidad')
    fecha_nacimiento = models.DateField(verbose_name='fecha de nacimiento', help_text='Formato año-mes-día (ej: 1988-04-30)')
    municipio_nacimiento = models.ForeignKey(Municipio, null=True, blank=True, verbose_name='municipio de nacimiento', related_name='municipio_nacimiento')
    
    direccion = models.CharField( max_length=100, verbose_name='dirección')
    municipio = models.ForeignKey(Municipio, verbose_name='municipio de residencia', null=True)
    telefono = models.BigIntegerField(null=True, blank=True, verbose_name=u'teléfono fijo')
    celular = models.BigIntegerField(null=True, blank=True, verbose_name=u'número de celular')
    email = models.EmailField()
    
    puntuacion_hv = models.IntegerField(null=True, blank=True)
    aceptado = models.NullBooleanField()

    institucion_actual = models.CharField(max_length=100, null=True, verbose_name=u'Institución donde labora actualmente')
    municipio_institucion = models.ForeignKey(Municipio, null=True, verbose_name=u'Municipio de la institución donde labora', related_name='institucionaspirante')
    jornada = models.CharField(max_length=5, null=True, choices=[('M', 'Mañana'), ('T', 'Tarde'), ('MT', 'Mañana y tarde')], verbose_name='jornada de trabajo')

    modificado = models.DateTimeField(null=True, auto_now=True)

    puntuacion_final = models.IntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        debeCrearDocumentosSoporte = self.id is None
        super(Aspirante,self).save(*args, **kwargs)

        if debeCrearDocumentosSoporte:
            DocumentosSoporte.objects.create(aspirante=self)


    def __unicode__(self):
        return (u"%s %s %s %s"%(self.nombre1,self.nombre2 or '', self.apellido1, self.apellido2 or '')).strip() or "-"

    def calcular_puntaje(self):
        def maximo_puntaje(objetos):
            lista = list(objetos)
            if not lista : return 0
            return max(x.puntaje() for x in lista)

        MUNICIPIOS_ESPECIALES = (1089, 1057, 462, 279)
        punt_municipio = 10 if self.municipio_institucion_id in MUNICIPIOS_ESPECIALES else 0

        punt_academica = maximo_puntaje(self.formacionacademica_set.all())
        punt_tic = maximo_puntaje(self.formaciontics_set.all())
        punt_conocimientos = self.conocimientosespecificos.puntaje()
        punt_idioma = maximo_puntaje(self.idioma_set.all())

        punt_formador_estudiantes = maximo_puntaje(self.experienciaformador_set.filter(tipo__startswith='E'))
        punt_formador_profesores = maximo_puntaje(self.experienciaformador_set.filter(tipo__startswith='P'))
        punt_formador_formadores = maximo_puntaje(self.experienciaformador_set.filter(tipo__startswith='F'))

        return int(round(punt_municipio+punt_academica+punt_tic+punt_conocimientos+punt_idioma+
                punt_formador_estudiantes+punt_formador_profesores+punt_formador_formadores))

    def inscripcion_finalizada(self):
        return self.puntuacion_hv!=None

    def numero_inscripcion(self):
        mihash = (self.numero_documento*44383)%1000000007
        clave = "%d-%d"%(self.id, mihash)
        return clave



class FormacionAcademica(models.Model):
    NIVELES = (
        (10, 'Técnica'),
        (20, 'Tecnológica'),
        (30, 'Profesional'),
        (40, 'Especialización'),
        (50, 'Maestría'),
        (60, 'Doctorado')
    )
    aspirante = models.ForeignKey(Aspirante)

    nivel = models.IntegerField(choices=NIVELES, verbose_name='Nivel')
    titulo = models.CharField(max_length=255, verbose_name='título obtenido')
    fecha_inicio = models.DateField(verbose_name=u'fecha de inicio', help_text='Formato año-mes-día (ej: 1988-04-30)')
    fecha_terminacion = models.DateField(verbose_name='fecha de finalización')
    institucion = models.CharField(max_length=255, verbose_name=u'institución formadora')
    relacionado_pedagogia = models.BooleanField(verbose_name=u'este estudio está relacionado con la pedagogía')
    relacionado_tics = models.BooleanField(verbose_name=u'este estudio está relacionado con las TICs')
    
    def __unicode__(self):
        return self.titulo

    def puntaje(self):
        if self.nivel==60 and self.relacionado_tics : return 30 # doctorado areas afines a TIC
        if self.nivel==60 : return 28 # doctorado
        if self.nivel==50 and self.relacionado_tics : return 26 # maestria areas afines a TIC
        if self.nivel==50 : return 24 # maestria
        if self.nivel==40 and self.relacionado_tics : return 20 # especialicacion TIC
        if self.nivel==40 : return 15
        if self.nivel==30 and self.relacionado_pedagogia : return 10 # licenciatura en educacion o areas afines
        return 0


class FormacionTics(models.Model):
    DURACION_CURSO = (
        (4, 'Curso TIC mínimo 40 horas'),
        (6, 'Cursos TIC  hasta 90 horas'),
        (8, 'Cursos TIC hasta 140 horas certificados o en proceso de certificación'),
        (10, 'Cursos TIC mas 140 horas')
    )
    aspirante = models.ForeignKey(Aspirante)
    duracion = models.IntegerField(choices=DURACION_CURSO, verbose_name=u'duración del curso')
    titulo = models.CharField(max_length=255, verbose_name='título obtenido')
    fecha_inicio = models.DateField(verbose_name=u'fecha de inicio', help_text='Formato año-mes-día (ej: 1988-04-30)')
    fecha_terminacion = models.DateField(verbose_name='fecha de finalización', help_text='Formato año-mes-día (ej: 1988-04-30)')
    institucion = models.CharField(max_length=255, verbose_name=u'institución formadora')

    def __unicode__(self):
        return self.titulo

    def puntaje(self):
        return self.duracion


class ConocimientosEspecificos(models.Model):
    HABILIDAD_CONOCIMIENTO = (
        (0, 'Ninguno'),
        (1, 'Regular'),
        (2, 'Bueno'),
        (3, 'Muy bueno'),
    ) 
    aspirante = models.OneToOneField(Aspirante)
    conocimiento1 = models.IntegerField(choices=HABILIDAD_CONOCIMIENTO, verbose_name='Conocimiento y manejo de herramientas ofimáticas')
    conocimiento2 = models.IntegerField(choices=HABILIDAD_CONOCIMIENTO, verbose_name='Conocimiento y manejo de herramientas  Web 2')
    conocimiento3 = models.IntegerField(choices=HABILIDAD_CONOCIMIENTO, verbose_name='Conocimiento herramientas de edición multimedia')
    conocimiento4 = models.IntegerField(choices=HABILIDAD_CONOCIMIENTO, verbose_name='Experiencia en desarrollo de contenidos educativos digitales')
    conocimiento5 = models.IntegerField(choices=HABILIDAD_CONOCIMIENTO, verbose_name='Experiencia en desarrollo de libros de texto digital')
    conocimiento6 = models.IntegerField(choices=HABILIDAD_CONOCIMIENTO, verbose_name='Experiencia en procesos de e-learning')
    conocimiento7 = models.IntegerField(choices=HABILIDAD_CONOCIMIENTO, verbose_name='Experiencia en gestión de proyectos educativos TIC')
    conocimiento8 = models.IntegerField(choices=HABILIDAD_CONOCIMIENTO, verbose_name='Experiencia en desarrollo de elementos de evaluación de competencias.')

    def puntaje(self):
        total = 0
        for i in xrange(1,9):
            p = getattr(self, "conocimiento%d"%i)
            total += [0.0, 0.7, 1.3, 2.5][p]
        return total


class Idioma(models.Model):
    IDIOMAS = (
        ('ING', 'Inglés'),
        ('FRA', 'Francés'),
        ('ITA', 'Italiano'),
        ('ALE', 'Alemán'),
        ('POR', 'Portugués'),
        ('JAP', 'Japonés'),
    )
    HABILIDAD_IDIOMA = (
        (0, 'Nulo'),
        (1, 'Regular'),
        (2, 'Bueno'),
        (3, 'Muy bueno'),
    )

    aspirante = models.ForeignKey(Aspirante)
    idioma = models.CharField(max_length=3, choices = IDIOMAS, verbose_name=u'idioma extranjero')
    habla   = models.IntegerField(choices=HABILIDAD_IDIOMA, verbose_name='habilidad hablando')
    lee     = models.IntegerField(choices=HABILIDAD_IDIOMA, verbose_name='habilidad leyendo')
    escribe = models.IntegerField(choices=HABILIDAD_IDIOMA, verbose_name='habilidad escribiendo')

    def puntaje(self):
        punt_lee     = [0.0, 0.8, 1.5, 3][self.lee]
        punt_escribe = [0.0, 0.8, 1.5, 3][self.escribe]
        punt_habla   = [0.0, 1.0, 2.0, 4][self.habla]
        return punt_lee+punt_escribe+punt_habla

"""
class AreaEnsenanza(models.Model):
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre
"""

class ExperienciaFormador(models.Model):
    TIPOS = (
        ('Formador TIC a Estudiantes',
            (('E2', 'TIC a Estudiantes - De 1 a 2 años'),
            ('E3',  'TIC a Estudiantes - De 2 a 3 años'),
            ('E4',  'TIC a Estudiantes - De 3 a 5 años'),
            ('E5',  'TIC a Estudiantes - Más de 5 años'))),
        ('Formador TIC a Profesores',
            (('P5', 'TIC a Profesores - De 80 a 200 horas'),
            ('P10', 'TIC a Profesores - De 200 a 300 horas'),
            ('P15', 'TIC a Profesores - De 300 a 450 horas'),
            ('P20', 'TIC a Profesores - Más de 450 horas'))),
        ('Formador de Formadores TIC',
            (('F3', 'TIC a Formadores TIC - De 80 a 120 horas'),
            ('F5',  'TIC a Formadores TIC - Más de 120 horas')))
    )

    aspirante = models.ForeignKey(Aspirante)
    tipo = models.CharField(max_length=5, choices = TIPOS)
    institucion = models.CharField(max_length=255, verbose_name=u'institución')
    fecha_inicio = models.DateField(verbose_name=u'fecha de inicio', help_text='Formato año-mes-día (ej: 1988-04-30)')
    fecha_fin = models.DateField(null=True, verbose_name=u'fecha de finalización')
    #jornada = models.CharField(max_length=5, null=True, blank=True, choices=[('M', 'Mañana'), ('T', 'Tarde'), ('MT', 'Mañana y tarde'), ('N','Noche')], verbose_name='jornada de trabajo')
    descripcion = models.CharField(max_length=200, blank=True, help_text='Ingrese el área o el nombre del proyecto en el cual fue formador')

    def puntaje(self):
        return int(self.tipo[1:]) # P10 -> 10;  F3 -> 3; etc



def crear_ruta_archivo(instance, filename):
    randomstr = instance.aspirante.numero_documento*99251
    return "convocat_soportes/%s-%s/%s"%(instance.aspirante_id, randomstr, filename.encode('ascii','ignore'))

class DocumentosSoporte(models.Model):
    aspirante = models.OneToOneField(Aspirante)
    formacion_academica = models.FileField(upload_to=crear_ruta_archivo, blank=True, null=True)
    formacion_tics = models.FileField(upload_to=crear_ruta_archivo, blank=True, null=True)
    idiomas = models.FileField(upload_to=crear_ruta_archivo, blank=True, null=True)
    ensenanza_tic_estudiantes = models.FileField(upload_to=crear_ruta_archivo, blank=True, null=True)
    ensenanza_tic_profesores = models.FileField(upload_to=crear_ruta_archivo, blank=True, null=True)
    ensenanza_tic_formadores = models.FileField(upload_to=crear_ruta_archivo, blank=True, null=True)

    def tiene_soportes(self):
        return bool(self.formacion_academica or self.formacion_tics or self.idiomas or self.ensenanza_tic_estudiantes or self.ensenanza_tic_profesores or self.ensenanza_tic_formadores)
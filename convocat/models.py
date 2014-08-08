# encoding:utf-8
from django.db import models

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
    fecha_nacimiento = models.DateField(verbose_name='fecha de nacimiento')
    municipio_nacimiento = models.ForeignKey(Municipio, null=True, blank=True, verbose_name='municipio de nacimiento', related_name='municipio_nacimiento')
    
    direccion = models.CharField( max_length=100, verbose_name='dirección')
    municipio = models.ForeignKey(Municipio, verbose_name='municipio de residencia', null=True)
    telefono = models.BigIntegerField(null=True, verbose_name=u'teléfono fijo')
    celular = models.BigIntegerField(null=True, blank=True, verbose_name=u'número de celular')
    email = models.EmailField(null=True, blank=True)
    
    puntuacion_hv = models.IntegerField(null=True)

    def __unicode__(self):
        return (u"%s %s %s %s"%(self.nombre1,self.nombre2 or '', self.apellido1, self.apellido2 or '')).strip() or "-"

class FormacionAcademica(models.Model):
    NIVELES = (
        (10, 'Técnica'),
        (20, 'Tecnológica'),
        (30, 'Profesional'),
        (40, 'Especializada'),
        (50, 'Maestría'),
        (60, 'Doctorado')
    )
    aspirante = models.ForeignKey(Aspirante)

    nivel = models.IntegerField(choices=NIVELES, verbose_name='Nivel')
    titulo = models.CharField(max_length=255, verbose_name='título obtenido')
    fecha_inicio = models.DateField(verbose_name=u'fecha de inicio')
    fecha_terminacion = models.DateField(verbose_name='fecha de finalización')
    institucion = models.CharField(max_length=255, verbose_name=u'institución formadora')
    relacionado_pedagogia = models.BooleanField(verbose_name=u'este estudio está relacionado con la pedagogía')
    relacionado_tics = models.BooleanField(verbose_name=u'este estudio está relacionado con las TICs')
    
    #tarjeta_profesional = models.CharField(max_length=255)

    def __unicode__(self):
        return self.titulo


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
    fecha_inicio = models.DateField(verbose_name=u'fecha de inicio')
    fecha_terminacion = models.DateField(verbose_name='fecha de finalización')
    institucion = models.CharField(max_length=255, verbose_name=u'institución formadora')

    def __unicode__(self):
        return self.titulo


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


class AreaEnsenanza(models.Model):
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre


class ExperienciaEnsenanza(models.Model):
    aspirante = models.ForeignKey(Aspirante)
    institucion = models.CharField(max_length=255, verbose_name=u'institución')
    tipo_institucion = models.CharField(max_length=3, choices=[('PUB','Pública'), ('PRI', 'Privada')], verbose_name=u'tipo de institución')
    telefono = models.BigIntegerField(null=True, blank=True, verbose_name=u'teléfono de contacto')
    email = models.EmailField(blank=True, verbose_name=u'correo electrónico')
    fecha_inicio = models.DateField(verbose_name=u'fecha de inicio')
    fecha_fin = models.DateField(null=True, blank=True, verbose_name=u'fecha de finalización', help_text='Deje en blanco si actualmente labora allí')
    jornada = models.CharField(max_length=5, null=True, blank=True, choices=[('M', 'Mañana'), ('T', 'Tarde'), ('MT', 'Mañana y tarde'), ('N','Noche')], verbose_name='jornada de trabajo')
    areas = models.ManyToManyField(AreaEnsenanza, blank=True, verbose_name=u'Areas que enseñó o enseña en esta institución')
    

class ExperienciaOtra(models.Model):
    aspirante = models.ForeignKey(Aspirante)
    entidad = models.CharField(max_length=255, verbose_name=u'entidad')
    tipo_entidad = models.CharField(max_length=3, choices=[('PUB','Pública'), ('PRI', 'Privada')], verbose_name=u'tipo de entidad')
    telefono = models.BigIntegerField(null=True, blank=True, verbose_name=u'teléfono')
    email = models.EmailField(blank=True, verbose_name=u'correo electrónico')
    fecha_inicio = models.DateField(verbose_name=u'fecha de inicio')
    fecha_fin = models.DateField(null=True, blank=True, verbose_name=u'fecha de finalización', help_text='Deje en blanco si actualmente labora allí')
    cargo = models.CharField(max_length=100, verbose_name=u'cargo ejercidos')

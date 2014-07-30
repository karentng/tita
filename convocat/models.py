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

class TipoTitulo(TipoSimple):
    pass

class TipoConocimiento(TipoSimple):
    pass

class TipoIdioma(TipoSimple):
    pass

class TipoFormador(TipoSimple):
    pass

class RangoTiempo(TipoSimple):
    pass

class Aspirante(models.Model):    
    tipo_documento = models.ForeignKey(TipoDocumento, null=True, blank=True, verbose_name='tipo de documento')
    numero_documento = models.CharField( max_length=128, blank=True, null=True, unique=True, verbose_name=u'número documento')
    nombre1 = models.CharField( max_length=255, verbose_name=u'Primer Nombre')
    nombre2 = models.CharField( max_length=255, blank=True, null=True, verbose_name=u'segundo nombre')
    apellido1 = models.CharField( max_length=255, verbose_name=u'Primer Apellido')
    apellido2 = models.CharField( max_length=255, blank=True, null=True, verbose_name=u'segundo apellido')
    genero = models.CharField( choices=[('M','Hombre'), ('F', 'Mujer')], max_length=1, verbose_name='sexo')
    nacionalidad = models.CharField( max_length=255, null=True, blank=True, verbose_name=u'nacionalidad')
    fecha_nacimiento = models.DateField( null=True, verbose_name='fecha de nacimiento')
    puntuacion_hv = models.IntegerField()

    def __unicode__(self):
        return (u"%s %s %s %s"%(self.nombre1,self.nombre2 or '', self.apellido1, self.apellido2 or '')).strip() or "-"

class FormacionAcademica(models.Model):
    aspirante = models.ForeignKey(Aspirante)
    titulo = models.ForeignKey(TipoTitulo, null=True, verbose_name=u'título obtenido')
    fecha_terminacion = models.DateField(verbose_name=u'fecha de finalización')

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
    curso = models.CharField(max_length=3, null=True, blank=True, verbose_name=u'duración del curso', choices=CURSOS_FORMACION_TICS)

    def __unicode__(self):
        return self.curso

class ConocimientosEspecificos(models.Model):
    aspirante = models.ForeignKey(Aspirante)
    conocimiento = models.ForeignKey(TipoConocimiento, verbose_name=u'conocimiento específico')
    calificacion = models.CharField(max_length=50, verbose_name=u'calificación')

    def __unicode__(self):
        return self.conocimiento


class IdiomasManejados(models.Model):
    aspirante = models.OneToOneField(Aspirante)
    idioma = models.ForeignKey(TipoIdioma, verbose_name=u'idioma', help_text=u"Sólo se pueden ingresar un idioma diferente al español.")
    habla = models.CharField(max_length=50, verbose_name=u'habilidad hablando')
    lee = models.CharField(max_length=50, verbose_name=u'habilidad leyendo')
    escribe = models.CharField(max_length=50, verbose_name=u'habilidad escribiendo')

    def __unicode__():
        return self.idioma

class ExperienciaFormadorTics(models.Model):
    aspirante = models.ForeignKey(Aspirante)
    formador = models.ForeignKey(TipoFormador, verbose_name=u'formador de')
    rango = models.ForeignKey(RangoTiempo, verbose_name=u'rango de formación')

    def __unicode__():
        return self.formador


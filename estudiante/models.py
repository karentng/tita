#encoding: utf-8
from django.db import models


JORNADAS = (
    ('C', 'Completa'),
    ('M', 'Mañana'),
    ('T', 'Tarde'),
    ('N', 'Nocturna')
)


# Create your models here.
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

class SecretariaEducacion(models.Model):
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return (u"%s"%self.nombre)

class CertificacionTIC(models.Model):
    estudiante = models.ForeignKey('campus.Estudiante')
    nombre = models.CharField(max_length=100, verbose_name="nombre de la certificación")
    entidad = models.CharField(max_length=100, verbose_name="entidad certificadora")
    fecha = models.DateTimeField(verbose_name="fecha de la certificación")

    def __unicode__(self):
        return (u"%s"%self.nombre)

class ProgramaTIC(models.Model):
    estudiante = models.ForeignKey('campus.Estudiante')
    nombre = models.CharField(max_length=100, verbose_name="nombre del programa")
    fecha = models.DateTimeField(verbose_name="fecha de la participación en el programa")

    def __unicode__(self):
        return (u"%s"%self.nombre)


class InfoLaboral(models.Model):
    ETNOEDUCADOR = (
        (1, 'No se desempeña como etnoeducador'),
        (1, 'Raizal'),
        (1, 'Afrocolombiano'),
        (1, 'Indígena'),
        (1, 'N.A'),
    )

    estudiante = models.ForeignKey('campus.Estudiante')

    secretaria_educacion = models.ForeignKey(SecretariaEducacion)
    institucion_educativa = models.ForeignKey('campus.InstitucionEducativa')
    cargo = models.IntegerField(choices=[(1, 'Docente'), (2, 'Directivo Docente')], verbose_name="cargo")
    sector = models.CharField( choices=[('O','Oficial'), ('N', 'No Oficial')], max_length=1, verbose_name='sector')
    zona = models.CharField( choices=[('R','Rural'), ('U', 'Urbana'), ('N', 'N.A')], max_length=1, verbose_name='zona')
    jornada = models.CharField(choices=JORNADAS, max_length=1)

    grados = models.ManyToManyField(Grado)
    asignaturas = models.ManyToManyField(Asignatura)
    decreto_docente = models.IntegerField( choices=[(1,'D.L 1278 de 2002'), (2, 'D.L 2277 de 1979')], max_length=1, verbose_name='decreto profesional docente')
    #grado escalafon
    nombramiento = models.IntegerField(choices=[(1,'Propiedad'), (2, 'Período de Prueba'), (3, 'Provisional')], max_length=1, verbose_name='tipo de nombramiento')

    tipo_etnoeducador = models.IntegerField(choices=ETNOEDUCADOR)
    poblacion_etnica = models.CharField(max_length="100", verbose_name="poblacion étnica que atiende", null=True)

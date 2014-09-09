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

class Sede(models.Model):
    nombre = models.CharField(max_length=100)
    institucion = models.ForeignKey('campus.InstitucionEducativa')

    def __unicode__(self):
        return (u"%s"%self.nombre)

class InfoLaboral(models.Model):
    ETNOEDUCADOR = (
        (1, 'No se desempeña como etnoeducador'),
        (2, 'Raizal'),
        (3, 'Afrocolombiano'),
        (4, 'Indígena')
    )

    GRADO_ESCALAFON = (
        ('D.L 1278 de 2002',
            ((1, '01'),
            (2,  '02'),
            (3,  '03'),
            (4,  '04'),
            (5,  '05'),
            (6,  '06'),
            (7,  '07'),
            (8,  '08'),
            (9,  '09'),
            (10,  '10'),
            (11,  '11'),
            (12,  '12'),
            (13,  '13'),
            (14,  '14'))),
        ('D.L 2277 de 1979',
            ((15, '1A'),
            (16,  '1B'),
            (17,  '1C'),
            (18,  '1D'),
            (19,  '2A'),
            (20,  '2B'),
            (21,  '2C'),
            (22,  '2D'),
            (23,  '3A'),
            (24,  '3B'),
            (25,  '3C'),
            (26,  '3D')))
    )

    estudiante = models.ForeignKey('campus.Estudiante')

    secretaria_educacion = models.ForeignKey(SecretariaEducacion)
    institucion_educativa = models.ForeignKey('campus.InstitucionEducativa')
    sedes = models.ForeignKey(Sede)
    cargo = models.IntegerField(choices=[(1, 'Docente'), (2, 'Rector'), (3, 'Coordinador'), (4, 'Otro')], verbose_name="cargo")
    zona = models.CharField( choices=[('R','Rural'), ('U', 'Urbana'), ('N', 'N.A')], max_length=1, verbose_name='zona')
    jornada = models.CharField(choices=JORNADAS, max_length=1)
    grados = models.ManyToManyField(Grado)
    asignaturas = models.ManyToManyField(Asignatura)
    decreto_docente = models.IntegerField( choices=GRADO_ESCALAFON, max_length=1, verbose_name='decreto profesional docente')
    nombramiento = models.IntegerField(choices=[(1,'Propiedad'), (2, 'Período de Prueba'), (3, 'Provisional')], max_length=1, verbose_name='tipo de nombramiento')
    tipo_etnoeducador = models.IntegerField(choices=ETNOEDUCADOR)
    poblacion_etnica = models.CharField(max_length="100", verbose_name="poblacion étnica que atiende", null=True, blank=True)

class FormacionAcademicaME(models.Model):
    NIVELES = (
        (10, 'Técnica'),
        (20, 'Tecnológica'),
        (30, 'Profesional'),
        (40, 'Especialización'),
        (50, 'Maestría'),
        (60, 'Doctorado')
    )
    estudiante = models.ForeignKey('campus.Estudiante')

    nivel = models.IntegerField(choices=NIVELES, verbose_name='Nivel')
    titulo = models.CharField(max_length=255, verbose_name='título obtenido')
    fecha_inicio = models.DateField(verbose_name=u'fecha de inicio', help_text='Formato año-mes-día (ej: 1988-04-30)')
    fecha_terminacion = models.DateField(verbose_name='fecha de finalización')
    institucion = models.CharField(max_length=255, verbose_name=u'institución formadora')
    relacionado_pedagogia = models.BooleanField(verbose_name=u'este estudio está relacionado con la pedagogía')
    relacionado_tic = models.BooleanField(verbose_name=u'este estudio está relacionado con las TICs')
    
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

class CertificacionTIC(models.Model):
    DURACION_CURSO = (
        (4, 'Curso TIC mínimo 40 horas'),
        (6, 'Cursos TIC  hasta 90 horas'),
        (8, 'Cursos TIC hasta 140 horas certificados o en proceso de certificación'),
        (10, 'Cursos TIC mas 140 horas')
    )

    estudiante = models.ForeignKey('campus.Estudiante')
    nombre = models.CharField(max_length=100, verbose_name="nombre del programa")
    duracion = models.IntegerField(choices=DURACION_CURSO)
    entidad = models.CharField(max_length=100, verbose_name="entidad certificadora")
    fecha_inicio = models.DateField(verbose_name=u'fecha de inicio', help_text='Formato año-mes-día (ej: 1988-04-30)')
    fecha_terminacion = models.DateField(verbose_name='fecha de finalización', help_text='Formato año-mes-día (ej: 1988-04-30)')

    def __unicode__(self):
        return (u"%s"%self.nombre)
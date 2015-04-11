#encoding: utf-8

from django.db import models
from convocat.models import Municipio, Aspirante
from django.contrib.auth.models import User
from estudiante.models import Cargo, Grado, Asignatura, SecretariaEducacion, CertificacionTIC, InfoLaboral
from bilinguismo.models import Bilinguismo

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
    TUTORES=(
    ('1', 'Mentor 1: ADRIANA MARIA VELEZ JONES'),
    ('2', 'Mentor 2: ROBERTO FERRO HERRERA'),
    ('3', 'Mentor 3: KARINA SANDOVAL ZAPATA'),
    ('4', 'Mentor 4: MAYRA MOSQUERA MORALES'),
    ('5', 'Mentor 5: DIANA FERNANDA JARAMILLO ESCOBAR'),

   )

    JORNADA=(
    ('Manana', 'Mañana'),
    ('Tarde', 'Tarde'),
    ('Ambas', 'Ambas'),
   )

    nombre1 = models.CharField( max_length=255, verbose_name='nombres')
    apellido1 = models.CharField( max_length=255, verbose_name='apellidos')
    jornada = models.CharField( max_length=255, choices=JORNADA)
    tutor = models.CharField( max_length=255, choices=TUTORES, verbose_name='Mentor')
    #aspirante = models.ForeignKey(Aspirante, verbose_name='aspirante', null=True, blank=True)
    usuario = models.ForeignKey(User)
    cohorte = models.IntegerField(default=1)

    def __unicode__(self):
        return (u"%s %s"%(self.nombre1,self.apellido1))




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

    #curso = models.ForeignKey(Curso, verbose_name='curso *', null=True, blank=True)

    aprobo = models.NullBooleanField()
    cohorte = models.IntegerField(default=2) #cambiar de acuerdo al cohorte que se este realizando

    def __unicode__(self):
        return (u"%s %s %s %s"%(self.nombre1,self.nombre2 or '', self.apellido1, self.apellido2 or '')).strip() or "-"

    def nombre_completo(self):
        return (u"%s %s %s %s"%(self.nombre1,self.nombre2 or '', self.apellido1, self.apellido2 or '')).strip() or "-"

    def numero_inscripcion(self):
        mihash = (self.numero_documento*44383)%1000000007
        clave = "%d-%d"%(self.id, mihash)
        return clave

    def infoLaboral(self):
        return  InfoLaboral.objects.filter(estudiante=self).latest('id')

class Cursos(models.Model):

    SEDES = (
        ('INEM JORGE ISAACS','INEM JORGE ISAACS'),
        ('ANTONIO JOSE CAMACHO','ANTONIO JOSE CAMACHO'),
        ('NORMAL. SUPERIOR SANTIAGO DE CALI', 'NORMAL. SUPERIOR SANTIAGO DE CALI'),
        ('GOLONDRINAS PRINCIPAL','GOLONDRINAS PRINCIPAL'),
        ('CARLOS HOLGUIN MALLARINO','CARLOS HOLGUIN MALLARINO'),
        ('MANUEL MARIA MALLARINO', 'Principal MANUEL MARIA MALLARINO'),
        ('EL DIAMANTE', 'EL DIAMANTE'),
        ('EUSTAQUIO PALACIOS','EUSTAQUIO PALACIOS'),
        ('JOSE MARIA CARBONELL','JOSE MARIA CARBONELL'),
        ('MARICE SINISTERRA','MARICE SINISTERRA'),
        ('Principal IE BOYACA', 'Principal IE BOYACA'),
        ('Principal YUMBO-IE MAYOR DE YUMBO - SEDE PRINCIPAL', 'Principal YUMBO-IE MAYOR DE YUMBO - SEDE PRINCIPAL'),
        ('Principal YUMBO-IE JOSE MARIA CORDOBA - SEDE PRINCIPAL', 'Principal YUMBO-IE JOSÉ MARÍA CÓRDOBA - SEDE PRINCIPAL'),
        ('Principal YUMBO-IE TITAN - SEDE PRINCIPAL', 'Principal YUMBO-IE TITAN - SEDE PRINCIPAL'),
        ('Principal YUMBO-IE CEAT GENERAL PIERO MARIOTTI - SEDE JOHN F. KENNEDY', 'Principal YUMBO-IE CEAT GENERAL PIERO MARIOTTI - SEDE JOHN F. KENNEDY'),
        ('Principal YUMBO-IE MANUEL MARIA SANCHEZ - SEDE PRINCIPAL', 'Principal YUMBO-IE MANUEL MARÍA SÁNCHEZ - SEDE PRINCIPAL'),
        ('Principal YUMBO-IE ROSA ZARATE DE PENA - SEDE PRINCIPAL', 'Principal YUMBO-IE ROSA ZÁRATE DE PEÑA - SEDE PRINCIPAL'),
        ('Principal VIJES', 'Principal VIJES'),
        #nuevas instituciones
        ('LIBARDO MADRID VALDERRAMA','LIBARDO MADRID VALDERRAMA'),        
        ('MONTEBELLO', 'MONTEBELLO'),        
        ('MONSENOR RAMON ARCILA','MONSEÑOR RAMON ARCILA'),        
        ('JOSE MANUEL SAAVEDRA GALINDO','JOSE MANUEL SAAVEDRA GALINDO'),           
        ('PEDRO ANTONIO MOLINA','PEDRO ANTONIO MOLINA'),           
        ('MULTIPROPOSITO','MULTIPROPOSITO'),          
        ('ISAIAS GAMBOA','ISAIAS GAMBOA'),           
        ('ALFONSO LOPEZ PUMAREJO','ALFONSO LOPEZ PUMAREJO'),          
        ('IE JUAN PABLO II','IE JUAN PABLO II'),          
        ('CRISTOBAL COLON','CRISTOBAL COLON'),
         #('MARICE SINISTERRA','MARICE SINISTERRA'),
         #la cumbre
        ('Principal LA CUMBRE - IE MARIA AUXILIADORA - SEDE PRINCIPAL', 'Principal LA CUMBRE - IE MARIA AUXILIADORA - SEDE PRINCIPAL'),
        ('Principal LA CUMBRE - IE SIMÓN BOLIVAR CABECERA MUNICIPAL - SEDE PRINCIPAL', 'Principal LA CUMBRE - IE SIMÓN BOLIVAR CABECERA MUNICIPAL - SEDE PRINCIPAL'),
        #dagua
        ('Principal DAGUA - INSTITUCION EDUCATIVA DEL DAGUA - SEDE Principal', 'Principal DAGUA - INSTITUCIÓN EDUCATIVA DEL DAGUA - SEDE Principal'),
        ('Principal DAGUA - IE EL QUEREMAL - SEDE PRINCIPAL', 'Principal DAGUA - IE EL QUEREMAL - SEDE PRINCIPAL'),
        ('Principal DAGUA - IE BORRERO AYERBE - SEDE PRINCIPAL', 'Principal DAGUA - IE BORRERO AYERBE - SEDE PRINCIPAL'),
        ('Principal DAGUA - IE SANTA TERESITA DEL NIÑO JESUS - SEDE PRINCIPAL', 'Principal DAGUA - IE SANTA TERESITA DEL NIÑO JESUS - SEDE PRINCIPAL'),
        #yumbo
        ('Principal YUMBO-IE JOSE ANTONIO GALÁN - SEDE PRINCIPAL', 'Principal YUMBO-IE JOSÉ ANTONIO GALÁN - SEDE PRINCIPAL'),
        ('Principal YUMBO-IE ALBERTO MENDOZA MAYOR - SEDE LICEO COMERCIAL', 'Principal YUMBO-IE ALBERTO MENDOZA MAYOR - SEDE LICEO COMERCIAL'),
        ('Principal YUMBO-IE ANTONIA SANTOS - SEDE ELIAS QUINTERO', 'Principal YUMBO-IE ANTONIA SANTOS - SEDE ELIAS QUINTERO'),
        ('Principal YUMBO-IE JUAN XXIII - SEDE PRINCIPAL', 'Principal YUMBO-IE JUAN XXIII - SEDE PRINCIPAL'),
        ('Principal YUMBO-IE POLICARPA SALAVARRIETA - SEDE PRINCIPAL', 'Principal YUMBO-IE POLICARPA SALAVARRIETA - SEDE PRINCIPAL'),
        ('Principal IE DIEZ DE MAYO', 'Principal IE DIEZ DE MAYO'),
        ('Principal IE ALVARO ECHEVERRY PEREA', 'Principal IE ALVARO ECHEVERRY PEREA'),
        ('IE CIUDADELA DESEPAZ','IE CIUDADELA DESEPAZ'),
        ### BILINGUISMO
        ("IETI comuna 17", "IETI comuna 17"),
        ("INEM Jorge Isaacs", "INEM Jorge Isaacs"),
        ("Liceo Departamental", "Liceo Departamental"),
        ("Normal Farallones de Cali", "Normal Farallones de Cali"),
        ("Celmira Bueno de Orejuela", "Celmira Bueno de Orejuela"),
    )
    descripcion = models.CharField(max_length=255, verbose_name=u'Nombre')
    institucion = models.CharField(choices=SEDES, max_length=200, verbose_name="institución")
    formador1 = models.ForeignKey(Formador, related_name="formador1",verbose_name="formador no. 1")
    formador2 = models.ForeignKey(Formador, related_name="formador2",verbose_name="formador no. 2", blank=True, null=True)
    estudiantes = models.ManyToManyField(Estudiante, blank=True, verbose_name='Estudiantes')
    estudiantes_bilinguismo = models.ManyToManyField(Bilinguismo, blank=True, verbose_name='Estudiantes de Bilinguismo')
    cohorte = models.IntegerField(default=1)

    def __unicode__(self):
        return (u"%s - %s y %s"%(self.descripcion,self.formador1, self.formador2))

class Curso(models.Model):
    descripcion = models.CharField(max_length=255, verbose_name=u'Nombre')
    institucion = models.ForeignKey(InstitucionEducativa, verbose_name='institucion', null=True, blank=True)
    formador = models.ForeignKey(Formador)
    estudiantes = models.ManyToManyField(Estudiante, blank=True, verbose_name='Estudiantes')

    def __unicode__(self):
        return (u"Curso: %s - Formador: %s - Institución: %s"%(self.descripcion,self.formador,self.institucion))

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


'''
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
    modificado = models.DateTimeField(auto_now=True)
    duracion = models.IntegerField(help_text='Seleccione el numero de horas (ej: 1)')
    curso = models.ForeignKey(Curso, null=True, blank=True)
    asistentes = models.ManyToManyField(Estudiante, blank=True, verbose_name='Seleccione las personas que asistieron a la clase')
    descripcion = models.CharField( max_length=1000, null=True, blank=True, verbose_name="descripción")
    tipo = models.CharField( max_length=10) # para especificar si es de diplomado o de acompanamiento in situ

    def __unicode__(self):
        return unicode(self.nombre)'''


class Clase(models.Model):

    nombre = models.CharField(max_length=255, help_text='Seleccione el numero de sesión (ej: 1)')
    fecha_inicio = models.DateTimeField(verbose_name=u'fecha y hora de inicio')
    modificado = models.DateTimeField(auto_now=True)
    duracion = models.IntegerField(help_text='Seleccione el numero de horas (ej: 1)')
    curso = models.ForeignKey(Cursos)
    asistentes = models.ManyToManyField(Estudiante, blank=True, verbose_name='Seleccione las personas que asistieron a la clase')
    descripcion = models.CharField( max_length=1000, null=True, blank=True, verbose_name="descripción")

    #soportes = models.FileField(upload_to=crear_ruta_archivo, blank=True, null=True)



    def __unicode__(self):
        return unicode(self.nombre)

class AcompanamientoInSitu(models.Model):

    nombre = models.CharField(max_length=255)
    #institucion = models.IntegerField(choices=SEDES, max_length=2, verbose_name="institución", null=True, blank=True)
    fecha_inicio = models.DateTimeField(verbose_name=u'fecha y hora de inicio')
    modificado = models.DateTimeField(auto_now=True)
    duracion = models.IntegerField(help_text='Seleccione el numero de horas (ej: 1)')
    asistentes = models.ManyToManyField(Estudiante, blank=True, verbose_name='Seleccione las personas que asistieron a la clase')
    descripcion = models.CharField( max_length=1000, null=True, blank=True, verbose_name="descripción")
    curso = models.ForeignKey(Cursos)

    def __unicode__(self):
        return unicode(self.nombre)

class Clases(models.Model):


    nombre = models.CharField(max_length=255)
    fecha_inicio = models.DateTimeField(verbose_name=u'fecha y hora de inicio')
    #institucion = models.IntegerField(choices=SEDES, max_length=2, verbose_name="institución", null=True, blank=True)
    modificado = models.DateTimeField(auto_now=True)
    duracion = models.PositiveIntegerField(help_text='Seleccione el numero de horas (ej: 1)')
    curso = models.ForeignKey(Cursos)
    asistentes = models.ManyToManyField(Estudiante, verbose_name='Seleccione las personas que asistieron a la clase')
    asistentes_bilinguismo = models.ManyToManyField(Bilinguismo, blank=True, verbose_name='Asistentes de Bilinguismo')
    descripcion = models.CharField( max_length=1000, null=True, blank=True, verbose_name="descripción")
    estado = models.BooleanField(default=True)
    observacion = models.CharField( max_length=1500, null=True, blank=True, verbose_name="observaciones")

    '''
    def save(self, *args, **kwargs):
        super(Clases,self).save(*args, **kwargs)
        SoporteClases.objects.create(clase=self)
    '''


class Actividad(models.Model):
    clase = models.ForeignKey(Clases)
    nombre = models.CharField(max_length=155, blank=False, null=False)
    fecha = models.DateField()
    estudiantes = models.ManyToManyField(Estudiante, blank=True)

    def __unicode__(self):
        return (u"%s (%s)"%(self.nombre, self.fecha)).strip() or "-"



class AcompanamientoInSitus(models.Model):


    nombre = models.CharField(max_length=255)
    fecha_inicio = models.DateTimeField(verbose_name=u'fecha y hora de inicio')
    #institucion = models.IntegerField(choices=SEDES, max_length=2, verbose_name="institución", null=True, blank=True)
    modificado = models.DateTimeField(auto_now=True)
    duracion = models.PositiveIntegerField(help_text='Seleccione el numero de horas (ej: 1)')
    curso = models.ForeignKey(Cursos)
    asistentes = models.ManyToManyField(Estudiante, verbose_name='Seleccione las personas que asistieron a la clase')
    descripcion = models.CharField( max_length=1000, null=True, blank=True, verbose_name="descripción")
    estado = models.BooleanField(default=True)
    observacion = models.CharField( max_length=1500, null=True, blank=True, verbose_name="observaciones")
    '''
    def save(self, *args, **kwargs):
        super(AcompanamientoInSitus,self).save(*args, **kwargs)
        SoporteAcompanamiento.objects.create(acompanamiento=self)
    '''

class ActividadAcompanamiento(models.Model):
    clase = models.ForeignKey(AcompanamientoInSitus)
    nombre = models.CharField(max_length=155, blank=False, null=False)
    fecha = models.DateField()
    estudiantes = models.ManyToManyField(Estudiante, blank=True)

    def __unicode__(self):
        return (u"%s (%s)"%(self.nombre, self.fecha)).strip() or "-"

"""
class Asistencia(models.Model):
    clase = models.ForeignKey(Clase)
    estudiante = models.ForeignKey(Estudiante)
    asistio = models.BooleanField(default=False)
    modificado = models.DateTimeField(auto_now=True)
"""
def crear_ruta_archivo(instance, filename):
    randomstr = str(instance.clase.fecha_inicio.day)+"-"+str(instance.clase.fecha_inicio.month)+"-"+str(instance.clase.fecha_inicio.year)+""
    return "soportes_clase/%s_fecha%s/%s"%(instance.clase.nombre, randomstr, filename.encode('ascii','ignore'))

class SoporteClase(models.Model):
    clase = models.ForeignKey(Clase)
    archivo = models.FileField(upload_to=crear_ruta_archivo)

class SoporteClases(models.Model):
    clase = models.ForeignKey(Clases, primary_key=True)
    archivo = models.FileField(upload_to=crear_ruta_archivo)

class CalificacionActividad(models.Model):
    class Meta:
        unique_together = [('estudiante','actividad'),]

    estudiante = models.ForeignKey(Estudiante)
    actividad = models.ForeignKey(Actividad)
    nota = models.FloatField()
    observacion = models.TextField()

def crear_ruta_archivo2(instance, filename):
    randomstr = str(instance.acompanamiento.fecha_inicio.day)+"-"+str(instance.acompanamiento.fecha_inicio.month)+"-"+str(instance.acompanamiento.fecha_inicio.year)+""
    return "soportes_acompanamiento/%s_fecha%s/%s"%(instance.acompanamiento.nombre, randomstr, filename.encode('ascii','ignore'))

class SoporteAcompanamiento(models.Model):
    acompanamiento = models.ForeignKey(AcompanamientoInSitus, primary_key=True)
    archivo = models.FileField(upload_to=crear_ruta_archivo2)








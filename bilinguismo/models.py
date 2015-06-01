#encoding: utf-8
from django.db import models
from estudiante.models import JORNADAS, Grado, Asignatura
from convocat.models import Municipio

class Bilinguismo(models.Model):

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
    finalizada = models.BooleanField(default=False)
    cohorte = models.IntegerField(default=1)

    def __unicode__(self):
        return (u"%s %s %s %s"%(self.nombre1,self.nombre2 or '', self.apellido1, self.apellido2 or '')).strip() or "-"

    def numero_inscripcion(self):
        mihash = (self.numero_documento*44385)%1000000007
        clave = "%d-%d"%(self.id, mihash)
        return clave

    def inscripcion_finalizada(self):
    	return self.finalizada

class InfoLaboralBilinguismo(models.Model):
    ETNOEDUCADOR = (
        (1, 'No se desempeña como etnoeducador'),
        (2, 'Raizal'),
        (3, 'Afrocolombiano'),
        (4, 'Indígena')
    )

    INSTITUCIONES = (
    	(1, "IETI comuna 17"),
    	(2, "INEM Jorge Isaacs"),
    	(3, "Liceo Departamental"),
    	(4, "Normal Farallones de Cali"),
    	(5, "Celmira Bueno de Orejuela"),

        # Cohorte 2

        ('INEM JORGE ISAACS',
            ((6, 'Principal INEM JORGE ISAACS'),
            (7,  'Satelite CECILIA MUÑOZ RICAURTE'),
            (8,  'Satelite LAS AMERICAS'),
            (9,  'Satelite CAMILO TORRES'),
            (10,  'Satelite CENTRO EDUCATIVO DEL NORTE'),
            (11,  'Satelite FRAY DOMINGO DE LAS CASAS'),
            (12,  'Satelite PABLO EMILIO'))),
        ('ANTONIO JOSE CAMACHO',
            ((13, 'Principal ANTONIO JOSE CAMACHO'),
            (14, 'Satelite REPUBLICA DEL PERU'),
            (15, 'Satelite MARCO FIDEL SUAREZ'),
            (16, 'Satelite OLGA LUCIA LLOREDA'))),
        ('NORMAL. SUPERIOR SANTIAGO DE CALI',
            ((17, 'Principal NORMAL. SUPERIOR SANTIAGO DE CALI'),
            (18,  'Satelite JOAQUIN DE CAYZEDO Y CUERO'))),
        ('GOLONDRINAS PRINCIPAL',
            ((19, 'Principal GOLONDRINAS PRINCIPAL'),
            (20,  'Satelite ANTONIO BARBERENA'))),
        ('CARLOS HOLGUIN MALLARINO',
            ((21, 'Principal CARLOS HOLGUIN MALLARINO'),
            (22,  'Satelite NIÑO JESUS DE ATOCHA'),
            (23,  'Satelite MIGUEL DE POMBO'))),
        ('MANUEL MARIA MALLARINO',
            ((24, 'Principal MANUEL MARIA MALLARINO'),
            (25, 'Satelite LAURA VICUÑA'),
            (26, 'Satelite LOS PINOS'),
            (27, 'Satelite CARLOS HOLGUIN SARDI'))),
        ('EL DIAMANTE',
            ((28, 'Principal EL DIAMANTE'),
            (29, 'Satelite JUAN PABLO II'))),
        ('EUSTAQUIO PALACIOS',
            ((30, 'Principal EUSTAQUIO PALACIOS'),
            (31, 'Satelite    LUIS LOPEZ MESA'),
            (32, 'Satelite    CELANESE'),
            (33, 'Satelite    MANUEL MARIA BUENAVENTURA'),
            (34, 'Satelite    MARISCAL JORGE ROBLEDO'),
            (35, 'Satelite    MIGUEL ANTONIO CARO'),
            (36, 'Satelite    GENERAL ANZOATEGUI'),
            (37, 'Satelite    TULIO ENRIQUE TASCON'),
            (38, 'Satelite    SANTIAGO RENGIFO'),
            (39, 'Satelite    SOFIA CAMARGO'))),
        ('JOSE MARIA CARBONELL',
            ((40, 'Principal JOSE MARIA CARBONELL'),
            (41, 'Satelite HONORIO VILLEGAS'))),
        ('MARICE SINISTERRA',
            ((42, 'Principal MARICE SINISTERRA'),
            (43, 'Satelite FENALCO ASTURIAS'))),
            (44, 'Principal IE BOYACA'),
            (45, 'Principal YUMBO-IE MAYOR DE YUMBO - SEDE PRINCIPAL'),
            (46, 'Principal YUMBO-IE JOSÉ MARÍA CÓRDOBA - SEDE PRINCIPAL'),
            (47, 'Principal YUMBO-IE TITAN - SEDE PRINCIPAL'),
            (48, 'Principal YUMBO-IE CEAT GENERAL PIERO MARIOTTI - SEDE JOHN F. KENNEDY'),
            (49, 'Principal YUMBO-IE MANUEL MARÍA SÁNCHEZ - SEDE PRINCIPAL'),
            (50, 'Principal YUMBO-IE ROSA ZÁRATE DE PEÑA - SEDE PRINCIPAL'),
            (51, 'Principal VIJES'),
    )

    GRADO_ESCALAFON = (
        ('D.L 1278 de 2002',
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
            (26,  '3D'))
            ),
        ('D.L 2277 de 1979',
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
            (14,  '14')))
    )


    persona = models.ForeignKey(Bilinguismo)

    institucion = models.IntegerField(choices=INSTITUCIONES, max_length=1)
    cargo = models.IntegerField(choices=[(1, 'Docente'), (2, 'Rector'), (3, 'Coordinador'), (4, 'Otro')], verbose_name="cargo")
    zona = models.CharField( choices=[('R','Rural'), ('U', 'Urbana')], max_length=1, verbose_name='zona')
    jornada = models.CharField(choices=JORNADAS, max_length=1)
    grados = models.ManyToManyField(Grado)
    asignaturas = models.ManyToManyField(Asignatura)
    otra_asignatura = models.CharField(max_length=100, verbose_name="otra asignatura no registrada", null=True, blank=True)
    decreto_docente = models.IntegerField( choices=GRADO_ESCALAFON, max_length=1, verbose_name='decreto profesional docente')
    nombramiento = models.IntegerField(choices=[(1,'Propiedad'), (2, 'Período de Prueba'), (3, 'Provisional')], max_length=1, verbose_name='tipo de nombramiento')
    tipo_etnoeducador = models.IntegerField(choices=ETNOEDUCADOR)
    poblacion_etnica = models.CharField(max_length="100", verbose_name="poblacion étnica que atiende", null=True, blank=True)

class FormacionAcademicaBilinguismo(models.Model):
    NIVELES = (
        (10, 'Técnica'),
        (20, 'Tecnológica'),
        (30, 'Profesional'),
        (40, 'Especialización'),
        (50, 'Maestría'),
        (60, 'Doctorado')
    )
    persona = models.ForeignKey(Bilinguismo)

    nivel = models.IntegerField(choices=NIVELES, verbose_name='Nivel')
    titulo = models.CharField(max_length=255, verbose_name='título obtenido')
    institucion = models.CharField(max_length=255, verbose_name=u'institución formadora')
    relacionado_pedagogia = models.BooleanField(verbose_name=u'este estudio está relacionado con la pedagogía')
    relacionado_tic = models.BooleanField(verbose_name=u'este estudio está relacionado con las TIC')
    
    def __unicode__(self):
        return self.titulo

    '''def puntaje(self):
        if self.nivel==60 and self.relacionado_tics : return 30 # doctorado areas afines a TIC
        if self.nivel==60 : return 28 # doctorado
        if self.nivel==50 and self.relacionado_tics : return 26 # maestria areas afines a TIC
        if self.nivel==50 : return 24 # maestria
        if self.nivel==40 and self.relacionado_tics : return 20 # especialicacion TIC
        if self.nivel==40 : return 15
        if self.nivel==30 and self.relacionado_pedagogia : return 10 # licenciatura en educacion o areas afines
        return 0'''

class CertificacionBilinguismo(models.Model):
    DURACION_CURSO = (
        (40, 'Curso TIC mínimo 40 horas'),
        (90, 'Cursos TIC  hasta 90 horas'),
        (140, 'Cursos TIC hasta 140 horas certificados o en proceso de certificación'),
        (141, 'Cursos TIC mas 140 horas')
    )

    persona = models.ForeignKey(Bilinguismo)
    nombre = models.CharField(max_length=100, verbose_name="nombre del programa")
    duracion = models.IntegerField(choices=DURACION_CURSO)
    entidad = models.CharField(max_length=100, verbose_name="entidad certificadora")

    def __unicode__(self):
        return (u"%s"%self.nombre)
#encoding: utf-8
from django.db import models


JORNADAS = (
    ('C', 'Completa'),
    ('M', 'Mañana'),
    ('T', 'Tarde'),
    ('N', 'Nocturna')
)

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
    (46, 'Principal VIJES'),

    # Segunda Cohorte

    ('LIBARDO MADRID VALDERRAMA',
        ((47, 'Principal LIBARDO MADRID VALDERRAMA'),
        (48, 'Satelite ANGELICA SIERRA'),
        (49, 'Satelite PRIMERO DE MAYO'))),
    (50, 'Principal ALVARO ECHEVERRI PEREA'),
    ('MONTEBELLO',
        ((51, 'Principal MONTEBELLO'),
        (52, 'Satelite SAN PEDRO APOSTOL'))),
    ('MONSEÑOR RAMON ARCILA',
        ((53, 'Principal MONSEÑOR RAMON ARCILA'),
        (54, 'Satelite RAUL ALFONSO SILVA HOLGUIN'),
        (55, 'Satelite ALFONSO REYES ECHANDIA'),
        (56, 'Satelite PUERTA DEL SOL IV y V'))),
    (57, 'Principal DIEZ DE MAYO'),
    ('JOSE MANUEL SAAVEDRA GALINDO',
        ((58, 'Principal JOSE MANUEL SAAVEDRA GALINDO'),
        (59, 'Satelite BENJAMIN HERRERA'),
        (60, 'Satelite NUESTRA SEÑORA DE FATIMA'))),
    (61, 'Principal CIUDADELA DESEPAZ'),
    ('PEDRO ANTONIO MOLINA',
        ((62, 'Principal PEDRO ANTONIO MOLINA'),
        (63, 'Satelite SAN JORGE'))),
    ('MULTIPROPOSITO',
        ((64, 'Principal MULTIPROPOSITO'),
        (65, 'Satelite JORGE ELIECER GONZALEZ RUBIO'))),
    ('ISAIAS GAMBOA',
        ((66, 'Principal ISAIAS GAMBOA'),
        (67, 'Satelite JOSE CELESTINO MUTIS'),
        (68, 'Satelite LA INMACULADA'),
        (69, 'Satelite ISAIAS GAMBOA SEDE BAJO AGUACATAL'))),
    ('ALFONSO LOPEZ PUMAREJO',
        ((70, 'Principal ALFONSO LOPEZ PUMAREJO'),
        (71, 'Satelite LOS FARALLONES'))),
    ('IE JUAN PABLO II',
        ((72, 'Principal IE JUAN PABLO II'),
        (73, 'Satelite TEMPLO DEL SABER'),
        (74, 'Satelite ALVARO ESCOBAR NAVIA'))),
    ('CRISTOBAL COLON',
        ((75, 'Principal CRISTOBAL COLON'),
        (76, 'Satelite BIENESTAR SOCIAL'),
        (77, 'Satelite JOSE JOAQUIN JARAMILLO'))),
    ('MARICE SINISTERRA',
        ((78, 'Principal MARICE SINISTERRA'),
        (79, 'Satelite FENALCO ASTURIAS'))),
    ('YUMBO',
        ((80, 'MAYOR DE YUMBO - SEDE PRINCIPAL'),
        (81, 'JOSÉ MARÍA CÓRDOBA - SEDE PRINCIPAL'),
        (82, 'JOSÉ ANTONIO GALÁN - SEDE PRINCIPAL'),
        (83, 'ALBERTO MENDOZA MAYOR - SEDE LICEO COMERCIAL'),
        (84, 'ANTONIA SANTOS - SEDE ELIAS QUINTERO'),
        (85, 'JUAN XXIII - SEDE PRINCIPAL'),
        (86, 'POLICARPA SALAVARRIETA - SEDE PRINCIPAL'),
        (87, 'CEAT GENERAL PIERO MARIOTTI - SEDE JOHN F. KENNEDY'))),
    ('LA CUMBRE',
        ((88, 'MARIA AUXILIADORA - SEDE PRINCIPAL'),
        (89, 'SIMÓN BOLIVAR CABECERA MUNICIPAL - SEDE PRINCIPAL'))),
    ('DAGUA',
        ((90, 'INSTITUCIÓN EDUCATIVA DEL DAGUA - SEDE Principal'),
        (91, 'EL QUEREMAL - SEDE PRINCIPAL'),
        (92, 'BORRERO AYERBE - SEDE PRINCIPAL'),
        (93, 'SANTA TERESITA DEL NIÑO JESUS - SEDE PRINCIPAL'))),


    ('EUSTAQUIO PALACIOS',
        ((94, 'EUSTAQUIO PALACIOS - SEDE PRINCIPAL'),
        (95, 'GENERAL ANZOATEGUI - SEDE SATELITE'))),
    ('NORMAL SUPERIOR FARALLONES DE CALI',
        ((96, 'NORMAL SUPERIOR FARALLONES DE CALI - SEDE PRINCIPAL'),
        (97, 'MARTIN RESTREPO MEJIA - SEDE SATELITE'),
        (98, 'SALVADOR IGLESIAS - SEDE SATELITE'),
        (99, 'CLUB NOEL - SEDE SATELITE'),
        (100, 'MANUEL SINISTERRA PATIÑO - SEDE SATELITE'),
        (101, 'FRANCISCO JOSE DE CALDAS - SEDE SATELITE'),
        (102, 'MARIA PERLAZA - SEDE SATELITE'),
        (103, 'CRISTALES - SEDE SATELITE'))),

    ('LICEO DEPARTAMENTAL',
        ((104, 'LICEO DEPARTAMENTAL - SEDE PRINCIPAL'),
        (105, 'LA GRAN COLOMBIA - SEDE SATELITE'),
        (106, 'LA PRESENTACIÓN - SEDE SATELITE'))),

    ('CELMIRA BUENO DE OREJUELA',
        ((107, 'CELMIRA BUENO DE OREJUELA - SEDE PRINCIPAL'),
        (108, 'MARIANO OSPINA PEREZ - SEDE SATELITE')))
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

class InfoLaboral(models.Model):
    ETNOEDUCADOR = (
        (1, 'No se desempeña como etnoeducador'),
        (2, 'Raizal'),
        (3, 'Afrocolombiano'),
        (4, 'Indígena')
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


    estudiante = models.ForeignKey('campus.Estudiante')

    secretaria_educacion = models.ForeignKey(SecretariaEducacion)
    #institucion_educativa = models.ForeignKey('campus.InstitucionEducativa')
    sede = models.IntegerField(choices=SEDES, max_length=2)
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
    institucion = models.CharField(max_length=255, verbose_name=u'institución formadora')
    relacionado_pedagogia = models.BooleanField(verbose_name=u'este estudio está relacionado con la pedagogía')
    relacionado_tic = models.BooleanField(verbose_name=u'este estudio está relacionado con las TIC')
    
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
        (40, 'Curso TIC mínimo 40 horas'),
        (90, 'Cursos TIC  hasta 90 horas'),
        (140, 'Cursos TIC hasta 140 horas certificados o en proceso de certificación'),
        (141, 'Cursos TIC mas 140 horas')
    )

    estudiante = models.ForeignKey('campus.Estudiante')
    nombre = models.CharField(max_length=100, verbose_name="nombre del programa")
    duracion = models.IntegerField(choices=DURACION_CURSO)
    entidad = models.CharField(max_length=100, verbose_name="entidad certificadora")

    def __unicode__(self):
        return (u"%s"%self.nombre)
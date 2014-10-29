# -*- coding: utf-8 -*-
from django.db import models
from campus.models import Formador
from django.contrib.auth.models import User

class MonitorInfoPersonal(models.Model):
#datos personales
    numero_documento = models.BigIntegerField(unique=True, verbose_name='número documento')
    nombre1 = models.CharField( max_length=255, verbose_name='primer nombre')
    nombre2 = models.CharField( max_length=255, blank=True, verbose_name='segundo nombre')
    apellido1 = models.CharField( max_length=255, verbose_name='primer apellido')
    apellido2 = models.CharField( max_length=255, blank=True, verbose_name='segundo apellido')
    sexo = models.CharField( choices=[('M','Hombre'), ('F', 'Mujer')], max_length=1, verbose_name='sexo')
    fecha_nacimiento = models.DateField(verbose_name='fecha de nacimiento', help_text='Formato año-mes-día (ej: 1988-04-30)')
    barrio = models.CharField( max_length=100, verbose_name='barrio de residencia')
    direccion = models.CharField( max_length=100, verbose_name='dirección')
    estrato = models.CharField( choices=[('1','1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], max_length=1, verbose_name='estrato')
    sector = models.CharField( choices=[('1','Sur'), ('2', 'Oriente'), ('3', 'Distrito de Agua Blanca'), ('4', 'Norte Oriente'), ('5', 'Norte Occidente')], max_length=1, verbose_name='sector en que vive')
    sectordesplazamiento = models.CharField( choices=[('1','Sur'), ('2', 'Oriente'), ('3', 'Distrito de Agua Blanca'), ('4', 'Norte Oriente'), ('5', 'Norte Occidente')], max_length=1, verbose_name='sector en que estaría dispuesto a desplazarse')
    def __unicode__(self):
        return (u"%s %s %s %s"%(self.nombre1,self.nombre2 or '', self.apellido1, self.apellido2 or '')).strip() or "-"

class MonitorInfoContacto(models.Model):
    monitor = models.OneToOneField(MonitorInfoPersonal, primary_key=True)
    celularppal = models.BigIntegerField(verbose_name=u'celular principal')
    celularsec = models.BigIntegerField(null=True, blank=True, verbose_name=u'celular secundario')
    telfijoppal = models.BigIntegerField(null=True, blank=True, verbose_name=u'teléfono fijo principal')
    telfijosec = models.BigIntegerField(null=True, blank=True, verbose_name=u'teléfono fijo secundario')
    email = models.EmailField()
    twitter = models.CharField(null=True, blank=True, max_length=255, verbose_name=u'usuario de twitter')
    facebook = models.CharField( max_length=255, verbose_name=u'usuario de facebook')    
    personacontacto = models.CharField( max_length=255, verbose_name='Escriba el nombre de alguna persona que le dé información', help_text='En caso de no poder contactarnos directamente con usted.')
    numerocontacto =  models.BigIntegerField(verbose_name=u'celular persona de contacto')

    def __unicode__(self):
        return self.email

class MonitorInfoAcademica(models.Model):

    PROGRAMAS = (
        ("1", 'Arquitectura'),
        ('2', 'Comunicación Social - Periodismo'),
        ('3', 'Diseño Gráfico'),
        ('4', 'Diseño Industrial'),
        ('5', 'Licenciatura en Arte Dramático'),
        ('6', 'Licenciatura en Artes Visuales'),
        ('7', 'Licenciatura en Música'),
        ('8', 'Pregrado en Música'),
        ('9', 'Licenciatura en Danza'),
        ('10', 'Administración de Empresas'),
        ('11', 'Contaduría Pública'),
        ('12', 'Comercio Exterior'),
        ('13', 'Tecnología en Gestión Portuaria'),
        ('14', 'Tecnología en Dirección de Empresas Turísticas y Hoteleras'),
        ('15', 'Biología'),
        ('16', 'Física'),
        ('17', 'Matemáticas'),
        ('18', 'Química'),
        ('19', 'Tecnología Química'),
        ('20', 'Economía'),
        ('21', 'Sociología'),
        ('22', 'Geografía'),
        ('23', 'Historia'),
        ('24', 'Licenciatura en Ciencias Sociales'),
        ('25', 'Licenciatura en Educación Básica con Enfasis en Ciencias Sociales'),
        ('26', 'Licenciatura en Filosofía'),
        ('27', 'Licenciatura en Historia'),
        ('28', 'Licenciatura en Lenguas Extranjeras Inglés-Francés'),
        ('29', 'Licenciatura en Literatura'),
        ('30', 'Profesional en Filosofía'),
        ('31', 'Tecnología en Interpretación para Sordos y Sordociegos'),
        ('32', 'Trabajo Social'),
        ('33', 'Estadística'),
        ('34', 'Ingeniería Agrícola'),
        ('35', 'Ingeniería Civil'),
        ('36', 'Ingeniería de Alimentos'),
        ('37', 'Ingeniería de Materiales'),
        ('38', 'Ingeniería de Sistemas'),
        ('39', 'Ingeniería Electrica'),
        ('40', 'Ingeniería Electrónica'),
        ('41', 'Ingeniería Industrial'),
        ('42', 'Ingeniería Mecánica'),
        ('43', 'Ingeniería Química'),
        ('44', 'Ingeniería Sanitaria y Ambiental'),
        ('45', 'Ingeniería Topográfica'),
        ('46', 'Tecnología en Alimentos'),
        ('47', 'Tecnología en Ecología y Manejo Ambiental'),
        ('48', 'Tecnología en Electrónica'),
        ('49', 'Tecnología en Manejo y Consevación de Suelos y Aguas'),
        ('50', 'Tecnología en Sistemas de Información'),
        ('51', 'Bacteriología y Laboratorio Clínico'),
        ('52', 'Enfermería'),
        ('53', 'Fisioterapia'),
        ('54', 'Fonoaudiología'),
        ('55', 'Medicina y Cirugía'),
        ('56', 'Odontología'),
        ('57', 'Terapia Ocupacional'),
        ('58', 'Tecnología en Atención Prehospitalaria'),
        ('59', 'Licenciatura en Educación Básica en Ciencias Naturales y Educación Ambiental'),
        ('60', 'Licenciatura en Educación Básica con Enfasis en Matemáticas'),
        ('61', 'Licenciatura en Educación Física y Deporte'),
        ('62', 'Licenciatura en Educación Popular'),
        ('63', 'Licenciatura en Matemática y Física'),
        ('64', 'Profesional en Estudios Políticos y Resolución de Conflictos'),
        ('65', 'Programa Académico de Recreación'),
        ('66', 'Psicología'),
        ('67', 'Salud Ocupacional'),
    )
    
    monitor = models.OneToOneField(MonitorInfoPersonal, primary_key=True)
    programa = models.CharField( choices=PROGRAMAS, max_length=3, verbose_name='programa académico')
    jornada = models.CharField(max_length=5, null=True, choices=[('D', 'Diurna'), ('N', 'Nocturna')], verbose_name='jornada de estudio')
    semestre = models.IntegerField()
    promedioacum = models.FloatField( verbose_name='promedio acumulado')
    nummaterias = models.IntegerField(verbose_name='número de materias que está viendo según su tabulado')
    semestre = models.IntegerField(verbose_name='número de semestre en que se encuentra')
    codigo = models.BigIntegerField(verbose_name='código de estudiante')

    
    def __unicode__(self):
        return self.programa



class AreasConocimiento(models.Model):
    
    monitor = models.OneToOneField(MonitorInfoPersonal, primary_key=True)
    cienciasnaturales = models.BooleanField(verbose_name='ciencias naturales')
    fisica = models.BooleanField(verbose_name='física')
    quimica = models.BooleanField(verbose_name='química')
    biologia = models.BooleanField(verbose_name='biología')
    matematica = models.BooleanField(verbose_name='matemática')
    trigonometria = models.BooleanField(verbose_name='trigonometría')
    algebra = models.BooleanField(verbose_name='álgrebra')
    logica = models.BooleanField(verbose_name='lógica')
    geometria = models.BooleanField(verbose_name='geometría')
    electronica = models.BooleanField(verbose_name='electrónica')
    espanol = models.BooleanField(verbose_name='español')
    ingles = models.BooleanField(verbose_name='inglés')
    cienciassociales = models.BooleanField(verbose_name='ciencias sociales')
    filosofia = models.BooleanField(verbose_name='filosofía')
    artistica = models.BooleanField(verbose_name='artistica')
    etica = models.BooleanField(verbose_name='ética y valores')
    cienciaseconomicas = models.BooleanField(verbose_name='ciencias económicas')
    educacionfisica = models.BooleanField(verbose_name='educación física')
    tecnologia = models.BooleanField(verbose_name='tecnología y sistemas')
    pedagogia = models.BooleanField(verbose_name='pedagogía')
    dibujotecnico = models.BooleanField(verbose_name='dibujo técnico')

'''
class AreasConocimiento(models.Model):
    
	cienciasnaturales = models.BooleanField(verbose_name='ciencias naturales')
	fisica = models.BooleanField(verbose_name='física')
	quimica = models.BooleanField(verbose_name='química')
	biologia = models.BooleanField(verbose_name='biología')
	matematica = models.BooleanField(verbose_name='matemática')
	trigonometria = models.BooleanField(verbose_name='trigonometría')
	algebra = models.BooleanField(verbose_name='álgrebra')
	logica = models.BooleanField(verbose_name='lógica')
	geometria = models.BooleanField(verbose_name='geometría')
	electronica = models.BooleanField(verbose_name='electrónica')
	espanol = models.BooleanField(verbose_name='español')
	ingles = models.BooleanField(verbose_name='inglés')
	cienciassociales = models.BooleanField(verbose_name='ciencias sociales')
	filosofia = models.BooleanField(verbose_name='filosofía')
	artistica = models.BooleanField(verbose_name='artistica')
	etica = models.BooleanField(verbose_name='ética y valores')
	cienciaseconomicas = models.BooleanField(verbose_name='ciencias económicas')
	educacionfisica = models.BooleanField(verbose_name='educación física')
	tecnologia = models.BooleanField(verbose_name='tecnología y sistemas')
	pedagogia = models.BooleanField(verbose_name='pedagogía')
	dibujotecnico = models.BooleanField(verbose_name='dibujo técnico')'''
    

class HorariosDisponibles(models.Model):

    monitor = models.OneToOneField(MonitorInfoPersonal, primary_key=True)
    lunesmanana = models.BooleanField(verbose_name='')
    lunestarde = models.BooleanField(verbose_name='')
    martesmanana = models.BooleanField(verbose_name='')
    martestarde = models.BooleanField(verbose_name='')
    miercolesmanana = models.BooleanField(verbose_name='')
    miercolestarde = models.BooleanField(verbose_name='')
    juevesmanana = models.BooleanField(verbose_name='')
    juevestarde = models.BooleanField(verbose_name='')
    viernesmanana = models.BooleanField(verbose_name='')
    viernestarde = models.BooleanField(verbose_name='')


class Componente(models.Model):
    
    nombre = models.CharField( max_length=255)
    descripcion = models.CharField( max_length=255, null=True, blank=True)
    valoraprobadocomp = models.IntegerField(null=True, blank=True, verbose_name="valor aprobado al componente")
    persona = models.CharField( max_length=255, verbose_name="nombre de la persona que lo aprueba", null=True, blank=True)

    def __unicode__(self):
        return (u"%s %s"%(self.nombre,self.descripcion ))
    

class Requerimiento(models.Model):

    SEDES = (
        ('INEM JORGE ISAACS',
            (("INEM JORGE ISAACS - Principal INEM JORGE ISAACS" , 'Principal INEM JORGE ISAACS'),
            ('INEM JORGE ISAACS - Satelite CECILIA MUNOZ RICAURTE',  'Satelite CECILIA MUÑOZ RICAURTE'),
            ('INEM JORGE ISAACS - Satelite LAS AMERICAS',  'Satelite LAS AMERICAS'),
            ('INEM JORGE ISAACS - Satelite CAMILO TORRES',  'Satelite CAMILO TORRES'),
            ('INEM JORGE ISAACS - Satelite CENTRO EDUCATIVO DEL NORTE',  'Satelite CENTRO EDUCATIVO DEL NORTE'),
            ('INEM JORGE ISAACS - Satelite FRAY DOMINGO DE LAS CASAS',  'Satelite FRAY DOMINGO DE LAS CASAS'),
            ('INEM JORGE ISAACS - Satelite PABLO EMILIO',  'Satelite PABLO EMILIO'))),
        ('ANTONIO JOSE CAMACHO',
            (('ANTONIO JOSE CAMACHO - Principal ANTONIO JOSE CAMACHO', 'Principal ANTONIO JOSE CAMACHO'),
            ('ANTONIO JOSE CAMACHO - Satelite REPUBLICA DEL PERU', 'Satelite REPUBLICA DEL PERU'),
            ('ANTONIO JOSE CAMACHO - Satelite MARCO FIDEL SUAREZ', 'Satelite MARCO FIDEL SUAREZ'),
            ('ANTONIO JOSE CAMACHO - Satelite OLGA LUCIA LLOREDA', 'Satelite OLGA LUCIA LLOREDA'))),
        ('NORMAL. SUPERIOR SANTIAGO DE CALI ',
            (('NORMAL. SUPERIOR SANTIAGO DE CALI - Principal NORMAL. SUPERIOR SANTIAGO DE CALI', 'Principal NORMAL. SUPERIOR SANTIAGO DE CALI'),
            ('NORMAL. SUPERIOR SANTIAGO DE CALI - Satelite JOAQUIN DE CAYZEDO Y CUERO' ,  'Satelite JOAQUIN DE CAYZEDO Y CUERO'))),
        ('GOLONDRINAS PRINCIPAL',
            (('GOLONDRINAS PRINCIPAL - Principal GOLONDRINAS PRINCIPAL', 'Principal GOLONDRINAS PRINCIPAL'),
            ('GOLONDRINAS PRINCIPAL - Satelite ANTONIO BARBERENA',  'Satelite ANTONIO BARBERENA'))),
        ('CARLOS HOLGUIN MALLARINO - ',
            (('CARLOS HOLGUIN MALLARINO - Principal CARLOS HOLGUIN MALLARINO', 'Principal CARLOS HOLGUIN MALLARINO'),
            ('CARLOS HOLGUIN MALLARINO - Satelite NINO JESUS DE ATOCHA',  'Satelite NIÑO JESUS DE ATOCHA'),
            ('CARLOS HOLGUIN MALLARINO - Satelite MIGUEL DE POMBO',  'Satelite MIGUEL DE POMBO'))),
        ('MANUEL MARIA MALLARINO - ',
            (('MANUEL MARIA MALLARINO - Principal MANUEL MARIA MALLARINO', 'Principal MANUEL MARIA MALLARINO'),
            ('MANUEL MARIA MALLARINO - Satelite LAURA VICUNA', 'Satelite LAURA VICUÑA'),
            ('MANUEL MARIA MALLARINO - Satelite LOS PINOS', 'Satelite LOS PINOS'),
            ('MANUEL MARIA MALLARINO - Satelite CARLOS HOLGUIN SARDI', 'Satelite CARLOS HOLGUIN SARDI'))),
        ('EL DIAMANTE - ',
            (('EL DIAMANTE - Principal EL DIAMANTE', 'Principal EL DIAMANTE'),
            ('EL DIAMANTE - Satelite JUAN PABLO II', 'Satelite JUAN PABLO II'))),
        ('EUSTAQUIO PALACIOS - ',
            (('EUSTAQUIO PALACIOS - Principal EUSTAQUIO PALACIOS', 'Principal EUSTAQUIO PALACIOS'),
            ('EUSTAQUIO PALACIOS - Satelite    LUIS LOPEZ MESA', 'Satelite    LUIS LOPEZ MESA'),
            ('EUSTAQUIO PALACIOS - Satelite    CELANESE', 'Satelite    CELANESE'),
            ('EUSTAQUIO PALACIOS - Satelite    MANUEL MARIA BUENAVENTURA', 'Satelite    MANUEL MARIA BUENAVENTURA'),
            ('EUSTAQUIO PALACIOS - Satelite    MARISCAL JORGE ROBLEDO', 'Satelite    MARISCAL JORGE ROBLEDO'),
            ('EUSTAQUIO PALACIOS - Satelite    MIGUEL ANTONIO CARO', 'Satelite    MIGUEL ANTONIO CARO'),
            ('EUSTAQUIO PALACIOS - Satelite    GENERAL ANZOATEGUI', 'Satelite    GENERAL ANZOATEGUI'),
            ('EUSTAQUIO PALACIOS - Satelite    TULIO ENRIQUE TASCON', 'Satelite    TULIO ENRIQUE TASCON'),
            ('EUSTAQUIO PALACIOS - Satelite    SANTIAGO RENGIFO', 'Satelite    SANTIAGO RENGIFO'),
            ('EUSTAQUIO PALACIOS - Satelite    SOFIA CAMARGO', 'Satelite    SOFIA CAMARGO'))),
        ('JOSE MARIA CARBONELL - ',
            (('JOSE MARIA CARBONELL - Principal JOSE MARIA CARBONELL', 'Principal JOSE MARIA CARBONELL'),
            ('JOSE MARIA CARBONELL - Satelite HONORIO VILLEGAS', 'Satelite HONORIO VILLEGAS'))),
        ('MARICE SINISTERRA - ',
            (('MARICE SINISTERRA - Principal MARICE SINISTERRA', 'Principal MARICE SINISTERRA'),
            ('MARICE SINISTERRA - Satelite FENALCO ASTURIAS', 'Satelite FENALCO ASTURIAS'))),
        ('MARICE SINISTERRA - Principal IE BOYACA', 'Principal IE BOYACA'),
        ('MARICE SINISTERRA - Principal YUMBO-IE MAYOR DE YUMBO - SEDE PRINCIPAL', 'Principal YUMBO-IE MAYOR DE YUMBO - SEDE PRINCIPAL'),
        ('MARICE SINISTERRA - Principal YUMBO-IE JOSE MARIA CORDOBA - SEDE PRINCIPAL', 'Principal YUMBO-IE JOSÉ MARÍA CÓRDOBA - SEDE PRINCIPAL'),
        ('MARICE SINISTERRA - Principal YUMBO-IE TITAN - SEDE PRINCIPAL', 'Principal YUMBO-IE TITAN - SEDE PRINCIPAL'),
        ('MARICE SINISTERRA - Principal YUMBO-IE CEAT GENERAL PIERO MARIOTTI - SEDE JOHN F. KENNEDY', 'Principal YUMBO-IE CEAT GENERAL PIERO MARIOTTI - SEDE JOHN F. KENNEDY'),
        ('MARICE SINISTERRA - Principal YUMBO-IE MANUEL MARÍA SANCHEZ - SEDE PRINCIPAL', 'Principal YUMBO-IE MANUEL MARÍA SÁNCHEZ - SEDE PRINCIPAL'),
        ('MARICE SINISTERRA - Principal YUMBO-IE ROSA ZARATE DE PENA - SEDE PRINCIPAL', 'Principal YUMBO-IE ROSA ZÁRATE DE PEÑA - SEDE PRINCIPAL'),
        ('MARICE SINISTERRA - Principal VIJES', 'Principal VIJES')
    )
    

    estado_req = models.CharField( choices=[('A','Aprobado'), ('PA', 'Por Aprobación')], max_length=3, verbose_name='estado del requerimiento')
    fecha_rec = models.DateField(verbose_name='fecha de recibido', help_text='Formato año-mes-día (ej: 1988-04-30)')
    fecha_eje = models.DateField(verbose_name='fecha de ejecucion', help_text='Formato año-mes-día (ej: 1988-04-30)')
    fisico_fir = models.BooleanField(verbose_name='está el físico firmado?')
    componente = models.ForeignKey(Componente)
    descripcion_req = models.CharField( max_length=5000, null=True, blank=True)
    justificacion_req = models.CharField( max_length=5000, null=True, blank=True)
    no_monitores = models.IntegerField()
    lugar_req = models.CharField(choices=SEDES, max_length=1000, verbose_name="lugar requerimiento")
    valor_estimado_req = models.BigIntegerField(null=True, blank=True)
    responsable = models.CharField(max_length=255)
    email_responsable = models.EmailField(null=True, blank=True)
    celular_responsable = models.BigIntegerField(null=True, blank=True)

    def __unicode__(self):
        return (u"Requerimiento no. %s fecha: %s lugar: %s"%(self.id,self.fecha_eje,self.lugar_req ))

class Reto(models.Model):
    
    nombre = models.CharField( max_length=255)
    descripcion = models.CharField( max_length=2550, null=True, blank=True)
    valor = models.IntegerField(null=True, blank=True, verbose_name="valor (en puntos)")
    proponente = models.CharField( max_length=255, verbose_name="nombre de la persona que lo propone", null=True, blank=True)
    def __unicode__(self):
        return (u"%s %s"%(self.nombre,self.descripcion ))

class Reclamacion(models.Model):

    SEDES = (
        ('INEM JORGE ISAACS',
            (("INEM JORGE ISAACS - Principal INEM JORGE ISAACS" , 'Principal INEM JORGE ISAACS'),
            ('INEM JORGE ISAACS - Satelite CECILIA MUNOZ RICAURTE',  'Satelite CECILIA MUÑOZ RICAURTE'),
            ('INEM JORGE ISAACS - Satelite LAS AMERICAS',  'Satelite LAS AMERICAS'),
            ('INEM JORGE ISAACS - Satelite CAMILO TORRES',  'Satelite CAMILO TORRES'),
            ('INEM JORGE ISAACS - Satelite CENTRO EDUCATIVO DEL NORTE',  'Satelite CENTRO EDUCATIVO DEL NORTE'),
            ('INEM JORGE ISAACS - Satelite FRAY DOMINGO DE LAS CASAS',  'Satelite FRAY DOMINGO DE LAS CASAS'),
            ('INEM JORGE ISAACS - Satelite PABLO EMILIO',  'Satelite PABLO EMILIO'))),
        ('ANTONIO JOSE CAMACHO',
            (('ANTONIO JOSE CAMACHO - Principal ANTONIO JOSE CAMACHO', 'Principal ANTONIO JOSE CAMACHO'),
            ('ANTONIO JOSE CAMACHO - Satelite REPUBLICA DEL PERU', 'Satelite REPUBLICA DEL PERU'),
            ('ANTONIO JOSE CAMACHO - Satelite MARCO FIDEL SUAREZ', 'Satelite MARCO FIDEL SUAREZ'),
            ('ANTONIO JOSE CAMACHO - Satelite OLGA LUCIA LLOREDA', 'Satelite OLGA LUCIA LLOREDA'))),
        ('NORMAL. SUPERIOR SANTIAGO DE CALI ',
            (('NORMAL. SUPERIOR SANTIAGO DE CALI - Principal NORMAL. SUPERIOR SANTIAGO DE CALI', 'Principal NORMAL. SUPERIOR SANTIAGO DE CALI'),
            ('NORMAL. SUPERIOR SANTIAGO DE CALI - Satelite JOAQUIN DE CAYZEDO Y CUERO' ,  'Satelite JOAQUIN DE CAYZEDO Y CUERO'))),
        ('GOLONDRINAS PRINCIPAL',
            (('GOLONDRINAS PRINCIPAL - Principal GOLONDRINAS PRINCIPAL', 'Principal GOLONDRINAS PRINCIPAL'),
            ('GOLONDRINAS PRINCIPAL - Satelite ANTONIO BARBERENA',  'Satelite ANTONIO BARBERENA'))),
        ('CARLOS HOLGUIN MALLARINO - ',
            (('CARLOS HOLGUIN MALLARINO - Principal CARLOS HOLGUIN MALLARINO', 'Principal CARLOS HOLGUIN MALLARINO'),
            ('CARLOS HOLGUIN MALLARINO - Satelite NINO JESUS DE ATOCHA',  'Satelite NIÑO JESUS DE ATOCHA'),
            ('CARLOS HOLGUIN MALLARINO - Satelite MIGUEL DE POMBO',  'Satelite MIGUEL DE POMBO'))),
        ('MANUEL MARIA MALLARINO - ',
            (('MANUEL MARIA MALLARINO - Principal MANUEL MARIA MALLARINO', 'Principal MANUEL MARIA MALLARINO'),
            ('MANUEL MARIA MALLARINO - Satelite LAURA VICUNA', 'Satelite LAURA VICUÑA'),
            ('MANUEL MARIA MALLARINO - Satelite LOS PINOS', 'Satelite LOS PINOS'),
            ('MANUEL MARIA MALLARINO - Satelite CARLOS HOLGUIN SARDI', 'Satelite CARLOS HOLGUIN SARDI'))),
        ('EL DIAMANTE - ',
            (('EL DIAMANTE - Principal EL DIAMANTE', 'Principal EL DIAMANTE'),
            ('EL DIAMANTE - Satelite JUAN PABLO II', 'Satelite JUAN PABLO II'))),
        ('EUSTAQUIO PALACIOS - ',
            (('EUSTAQUIO PALACIOS - Principal EUSTAQUIO PALACIOS', 'Principal EUSTAQUIO PALACIOS'),
            ('EUSTAQUIO PALACIOS - Satelite    LUIS LOPEZ MESA', 'Satelite    LUIS LOPEZ MESA'),
            ('EUSTAQUIO PALACIOS - Satelite    CELANESE', 'Satelite    CELANESE'),
            ('EUSTAQUIO PALACIOS - Satelite    MANUEL MARIA BUENAVENTURA', 'Satelite    MANUEL MARIA BUENAVENTURA'),
            ('EUSTAQUIO PALACIOS - Satelite    MARISCAL JORGE ROBLEDO', 'Satelite    MARISCAL JORGE ROBLEDO'),
            ('EUSTAQUIO PALACIOS - Satelite    MIGUEL ANTONIO CARO', 'Satelite    MIGUEL ANTONIO CARO'),
            ('EUSTAQUIO PALACIOS - Satelite    GENERAL ANZOATEGUI', 'Satelite    GENERAL ANZOATEGUI'),
            ('EUSTAQUIO PALACIOS - Satelite    TULIO ENRIQUE TASCON', 'Satelite    TULIO ENRIQUE TASCON'),
            ('EUSTAQUIO PALACIOS - Satelite    SANTIAGO RENGIFO', 'Satelite    SANTIAGO RENGIFO'),
            ('EUSTAQUIO PALACIOS - Satelite    SOFIA CAMARGO', 'Satelite    SOFIA CAMARGO'))),
        ('JOSE MARIA CARBONELL - ',
            (('JOSE MARIA CARBONELL - Principal JOSE MARIA CARBONELL', 'Principal JOSE MARIA CARBONELL'),
            ('JOSE MARIA CARBONELL - Satelite HONORIO VILLEGAS', 'Satelite HONORIO VILLEGAS'))),
        ('MARICE SINISTERRA - ',
            (('MARICE SINISTERRA - Principal MARICE SINISTERRA', 'Principal MARICE SINISTERRA'),
            ('MARICE SINISTERRA - Satelite FENALCO ASTURIAS', 'Satelite FENALCO ASTURIAS'))),
        ('MARICE SINISTERRA - Principal IE BOYACA', 'Principal IE BOYACA'),
        ('MARICE SINISTERRA - Principal YUMBO-IE MAYOR DE YUMBO - SEDE PRINCIPAL', 'Principal YUMBO-IE MAYOR DE YUMBO - SEDE PRINCIPAL'),
        ('MARICE SINISTERRA - Principal YUMBO-IE JOSE MARIA CORDOBA - SEDE PRINCIPAL', 'Principal YUMBO-IE JOSÉ MARÍA CÓRDOBA - SEDE PRINCIPAL'),
        ('MARICE SINISTERRA - Principal YUMBO-IE TITAN - SEDE PRINCIPAL', 'Principal YUMBO-IE TITAN - SEDE PRINCIPAL'),
        ('MARICE SINISTERRA - Principal YUMBO-IE CEAT GENERAL PIERO MARIOTTI - SEDE JOHN F. KENNEDY', 'Principal YUMBO-IE CEAT GENERAL PIERO MARIOTTI - SEDE JOHN F. KENNEDY'),
        ('MARICE SINISTERRA - Principal YUMBO-IE MANUEL MARÍA SANCHEZ - SEDE PRINCIPAL', 'Principal YUMBO-IE MANUEL MARÍA SÁNCHEZ - SEDE PRINCIPAL'),
        ('MARICE SINISTERRA - Principal YUMBO-IE ROSA ZARATE DE PENA - SEDE PRINCIPAL', 'Principal YUMBO-IE ROSA ZÁRATE DE PEÑA - SEDE PRINCIPAL'),
        ('MARICE SINISTERRA - Principal VIJES', 'Principal VIJES')
    )

    colegio = models.CharField(choices=SEDES, max_length=1000, verbose_name="institución")
    jornada = models.CharField(max_length=5, null=True, choices=[('D', 'Diurna'), ('N', 'Nocturna')])
    fecha = models.DateField(verbose_name='fecha', help_text='Formato año-mes-día (ej: 1988-04-30)')
    supervisor = models.ForeignKey(MonitorInfoPersonal)
    descripcion = models.CharField( max_length=2550, null=True, blank=True)
    estado = models.CharField( choices=[('PR','Por Revisión'), ('P', 'Procede'), ('NP','No Procede')], max_length=3, verbose_name='estado',blank=True)
    def __unicode__(self):
        return (u"%s %s"%(self.colegio,self.jornada ))

def crear_ruta_archivo(instance, filename):
    randomstr = instance.monitor.numero_documento
    return "malla_soportes/%s-%s/%s"%(instance.monitor_id, randomstr, filename.encode('ascii','ignore'))

class DocumentosSoporte(models.Model):
    monitor = models.OneToOneField(MonitorInfoPersonal, primary_key=True)
    soportes = models.FileField(upload_to=crear_ruta_archivo, blank=True, null=True)


class Lista(models.Model):
    SEDES = (
        ('INEM JORGE ISAACS',
            (("INEM JORGE ISAACS - Principal INEM JORGE ISAACS" , 'Principal INEM JORGE ISAACS'),
            ('INEM JORGE ISAACS - Satelite CECILIA MUNOZ RICAURTE',  'Satelite CECILIA MUÑOZ RICAURTE'),
            ('INEM JORGE ISAACS - Satelite LAS AMERICAS',  'Satelite LAS AMERICAS'),
            ('INEM JORGE ISAACS - Satelite CAMILO TORRES',  'Satelite CAMILO TORRES'),
            ('INEM JORGE ISAACS - Satelite CENTRO EDUCATIVO DEL NORTE',  'Satelite CENTRO EDUCATIVO DEL NORTE'),
            ('INEM JORGE ISAACS - Satelite FRAY DOMINGO DE LAS CASAS',  'Satelite FRAY DOMINGO DE LAS CASAS'),
            ('INEM JORGE ISAACS - Satelite PABLO EMILIO',  'Satelite PABLO EMILIO'))),
        ('ANTONIO JOSE CAMACHO',
            (('ANTONIO JOSE CAMACHO - Principal ANTONIO JOSE CAMACHO', 'Principal ANTONIO JOSE CAMACHO'),
            ('ANTONIO JOSE CAMACHO - Satelite REPUBLICA DEL PERU', 'Satelite REPUBLICA DEL PERU'),
            ('ANTONIO JOSE CAMACHO - Satelite MARCO FIDEL SUAREZ', 'Satelite MARCO FIDEL SUAREZ'),
            ('ANTONIO JOSE CAMACHO - Satelite OLGA LUCIA LLOREDA', 'Satelite OLGA LUCIA LLOREDA'))),
        ('NORMAL. SUPERIOR SANTIAGO DE CALI ',
            (('NORMAL. SUPERIOR SANTIAGO DE CALI - Principal NORMAL. SUPERIOR SANTIAGO DE CALI', 'Principal NORMAL. SUPERIOR SANTIAGO DE CALI'),
            ('NORMAL. SUPERIOR SANTIAGO DE CALI - Satelite JOAQUIN DE CAYZEDO Y CUERO' ,  'Satelite JOAQUIN DE CAYZEDO Y CUERO'))),
        ('GOLONDRINAS PRINCIPAL',
            (('GOLONDRINAS PRINCIPAL - Principal GOLONDRINAS PRINCIPAL', 'Principal GOLONDRINAS PRINCIPAL'),
            ('GOLONDRINAS PRINCIPAL - Satelite ANTONIO BARBERENA',  'Satelite ANTONIO BARBERENA'))),
        ('CARLOS HOLGUIN MALLARINO - ',
            (('CARLOS HOLGUIN MALLARINO - Principal CARLOS HOLGUIN MALLARINO', 'Principal CARLOS HOLGUIN MALLARINO'),
            ('CARLOS HOLGUIN MALLARINO - Satelite NINO JESUS DE ATOCHA',  'Satelite NIÑO JESUS DE ATOCHA'),
            ('CARLOS HOLGUIN MALLARINO - Satelite MIGUEL DE POMBO',  'Satelite MIGUEL DE POMBO'))),
        ('MANUEL MARIA MALLARINO - ',
            (('MANUEL MARIA MALLARINO - Principal MANUEL MARIA MALLARINO', 'Principal MANUEL MARIA MALLARINO'),
            ('MANUEL MARIA MALLARINO - Satelite LAURA VICUNA', 'Satelite LAURA VICUÑA'),
            ('MANUEL MARIA MALLARINO - Satelite LOS PINOS', 'Satelite LOS PINOS'),
            ('MANUEL MARIA MALLARINO - Satelite CARLOS HOLGUIN SARDI', 'Satelite CARLOS HOLGUIN SARDI'))),
        ('EL DIAMANTE - ',
            (('EL DIAMANTE - Principal EL DIAMANTE', 'Principal EL DIAMANTE'),
            ('EL DIAMANTE - Satelite JUAN PABLO II', 'Satelite JUAN PABLO II'))),
        ('EUSTAQUIO PALACIOS - ',
            (('EUSTAQUIO PALACIOS - Principal EUSTAQUIO PALACIOS', 'Principal EUSTAQUIO PALACIOS'),
            ('EUSTAQUIO PALACIOS - Satelite    LUIS LOPEZ MESA', 'Satelite    LUIS LOPEZ MESA'),
            ('EUSTAQUIO PALACIOS - Satelite    CELANESE', 'Satelite    CELANESE'),
            ('EUSTAQUIO PALACIOS - Satelite    MANUEL MARIA BUENAVENTURA', 'Satelite    MANUEL MARIA BUENAVENTURA'),
            ('EUSTAQUIO PALACIOS - Satelite    MARISCAL JORGE ROBLEDO', 'Satelite    MARISCAL JORGE ROBLEDO'),
            ('EUSTAQUIO PALACIOS - Satelite    MIGUEL ANTONIO CARO', 'Satelite    MIGUEL ANTONIO CARO'),
            ('EUSTAQUIO PALACIOS - Satelite    GENERAL ANZOATEGUI', 'Satelite    GENERAL ANZOATEGUI'),
            ('EUSTAQUIO PALACIOS - Satelite    TULIO ENRIQUE TASCON', 'Satelite    TULIO ENRIQUE TASCON'),
            ('EUSTAQUIO PALACIOS - Satelite    SANTIAGO RENGIFO', 'Satelite    SANTIAGO RENGIFO'),
            ('EUSTAQUIO PALACIOS - Satelite    SOFIA CAMARGO', 'Satelite    SOFIA CAMARGO'))),
        ('JOSE MARIA CARBONELL - ',
            (('JOSE MARIA CARBONELL - Principal JOSE MARIA CARBONELL', 'Principal JOSE MARIA CARBONELL'),
            ('JOSE MARIA CARBONELL - Satelite HONORIO VILLEGAS', 'Satelite HONORIO VILLEGAS'))),
        ('MARICE SINISTERRA - ',
            (('MARICE SINISTERRA - Principal MARICE SINISTERRA', 'Principal MARICE SINISTERRA'),
            ('MARICE SINISTERRA - Satelite FENALCO ASTURIAS', 'Satelite FENALCO ASTURIAS'))),
        ('MARICE SINISTERRA - Principal IE BOYACA', 'Principal IE BOYACA'),
        ('MARICE SINISTERRA - Principal YUMBO-IE MAYOR DE YUMBO - SEDE PRINCIPAL', 'Principal YUMBO-IE MAYOR DE YUMBO - SEDE PRINCIPAL'),
        ('MARICE SINISTERRA - Principal YUMBO-IE JOSE MARIA CORDOBA - SEDE PRINCIPAL', 'Principal YUMBO-IE JOSÉ MARÍA CÓRDOBA - SEDE PRINCIPAL'),
        ('MARICE SINISTERRA - Principal YUMBO-IE TITAN - SEDE PRINCIPAL', 'Principal YUMBO-IE TITAN - SEDE PRINCIPAL'),
        ('MARICE SINISTERRA - Principal YUMBO-IE CEAT GENERAL PIERO MARIOTTI - SEDE JOHN F. KENNEDY', 'Principal YUMBO-IE CEAT GENERAL PIERO MARIOTTI - SEDE JOHN F. KENNEDY'),
        ('MARICE SINISTERRA - Principal YUMBO-IE MANUEL MARÍA SANCHEZ - SEDE PRINCIPAL', 'Principal YUMBO-IE MANUEL MARÍA SÁNCHEZ - SEDE PRINCIPAL'),
        ('MARICE SINISTERRA - Principal YUMBO-IE ROSA ZARATE DE PENA - SEDE PRINCIPAL', 'Principal YUMBO-IE ROSA ZÁRATE DE PEÑA - SEDE PRINCIPAL'),
        ('MARICE SINISTERRA - Principal VIJES', 'Principal VIJES')
    )

    CONDICION = (
        ('Pendiente', 'Pendiente'),
        ('Ejecutada', 'Ejecutada'),
        ('Inasistida', 'Inasistida'),
        ('Cancelada', 'Cancelada'),
        ('Excusa', 'Excusa'),
        ('Incompleta', 'Incompleta'),)

    TIPO = (
        ('Regular', 'Regular'),
        ('Supervisor', 'Supervisor'),
        ('Contingente', 'Contingente'),
        ('No programada', 'No programada'),
        ('Especial', 'Especial'),
        )

    AREAS =(
        ('Ciencias Naturales', 'Ciencias Naturales'),
        ('Fisica', 'Física'),
        ('Quimica', 'Química'),
        ('Biologia', 'Biología'),
        ('Matematica', 'Matemática'),
        ('Trigonometria', 'Trigonometría'),
        ('Algebra', 'Algebra'),
        ('Logica', 'Lógica'),
        ('Geometria', 'Geometría'),
        ('Electronica', 'Electrónica'),
        ('Espanol', 'Español'),
        ('Ingles', 'Inglés'),
        ('Ciencias Sociales', 'Ciencias Sociales'),
        ('Filosofia', 'Filosofía'),
        ('Artistica', 'Artística'),
        ('Ciencias Economicas', 'Ciencias Económicas'),
        ('Etica y Valores', 'Etica y Valores'),
        ('Educacion Fisica', 'Educación Física'),
        ('Tecnologia y Sistemas', 'Tecnología y Sistemas'),
        ('Pedagogia', 'Pedagogía'),
        ( 'Dibujo Tecnico', 'Dibujo Técnico'),)

    asignacion = models.IntegerField(verbose_name='asignación')
    requerimiento = models.ForeignKey(Requerimiento)
    fecha = models.DateField(verbose_name='fecha de nacimiento', help_text='Formato año-mes-día (ej: 1988-04-30)')
    colegio = models.CharField(choices=SEDES, max_length=1000, verbose_name="institución")
    profesor = models.ForeignKey(Formador)
    monitor = models.ForeignKey(MonitorInfoPersonal)
    materia = models.CharField(choices=AREAS, max_length=1000, verbose_name="asignatura")
    espacio = models.CharField( max_length=255, blank=True, help_text='numero de salón')
    condicion = models.CharField(choices=CONDICION, max_length=1000, verbose_name="condición")
    tipo = models.CharField(choices=TIPO, max_length=1000, verbose_name="tipo")
    idasigncancel = models.IntegerField(null = True, blank = True, verbose_name="id asignación cancelada", help_text='Éste campo solo se llena en caso de que haya otra lista de tipo "No programada", en este caso se pondría el Id de la asignación cancelada.')
    horas = models.IntegerField()
    #puntos = 
    observaciones = models.CharField( max_length=2550, blank=True)
    usuario = models.CharField( max_length=2550, blank=True)
    fecha_modificado = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return (u"%s %s"%(self.asignacion,self.requerimiento ))
    





    
	

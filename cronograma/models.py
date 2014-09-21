# encoding:utf-8
from django.db import models
from dateutil.relativedelta import relativedelta
from datetime import datetime


class EventosAcompanamiento(models.Model):

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

    institucion = models.IntegerField(choices=SEDES, max_length=2, verbose_name="institución")
    nombre = models.CharField( max_length=255, verbose_name='nombre')
    fecha_inicio = models.DateField(verbose_name=u'fecha de inicio', help_text='Formato año-mes-día (ej: 2014-09-30)')
    hora_inicio = models.TimeField(verbose_name=u'hora de inicio', help_text='Formato HH:MM (ej: 14:30)')
    fecha_finalizacion = models.DateField(verbose_name=u'fecha de finalización', help_text='Formato año-mes-día (ej: 2014-09-30)')
    hora_finalizacion = models.TimeField(verbose_name=u'hora de finalizacion', help_text='Formato HH:MM (ej: 14:30)')
    descripcion = models.CharField( max_length=1000, null=True, blank=True)

    def __unicode__(self):
        return self.nombre
        
class EventosDiplomado(models.Model):
    nombre = models.CharField( max_length=255, verbose_name='nombre')
    fecha_inicio = models.DateField(verbose_name=u'fecha de inicio', help_text='Formato año-mes-día (ej: 2014-09-30)')
    hora_inicio = models.CharField(max_length=6,verbose_name=u'hora de inicio', help_text='Formato HH:MM (ej: 14:30)')
    fecha_finalizacion = models.DateField(verbose_name=u'fecha de finalización', help_text='Formato año-mes-día (ej: 2014-09-30)')
    hora_finalizacion = models.CharField(max_length=6,verbose_name=u'hora de finalizacion', help_text='Formato HH:MM (ej: 14:30)')
    descripcion = models.CharField( max_length=1000, null=True, blank=True)

    def __unicode__(self):
        return self.nombre



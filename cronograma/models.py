# encoding:utf-8
from django.db import models
from dateutil.relativedelta import relativedelta
from datetime import datetime


class EventosAcompanamiento(models.Model):
    institucion = models.CharField( max_length=1000, null=True, blank=True)
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
    hora_inicio = models.TimeField(verbose_name=u'hora de inicio', help_text='Formato HH:MM (ej: 14:30)')
    fecha_finalizacion = models.DateField(verbose_name=u'fecha de finalización', help_text='Formato año-mes-día (ej: 2014-09-30)')
    hora_finalizacion = models.TimeField(verbose_name=u'hora de finalizacion', help_text='Formato HH:MM (ej: 14:30)')
    descripcion = models.CharField( max_length=1000, null=True, blank=True)

    def __unicode__(self):
        return self.nombre



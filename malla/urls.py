from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('malla.views',
    url(r'^malla/infobasica$', 'datosBasicos', name='datos_basicos'),
    url(r'^malla/infocontacto$', 'datosContacto', name='datos_contacto'),
    url(r'^malla/infoacademica$', 'datosAcademicos', name='datos_academicos'),
    url(r'^malla/areasconocimiento$', 'areasConocimiento', name='areas_conocimiento'),
    url(r'^malla/componente$', 'componente', name='componente'),
    url(r'^malla/requerimiento$', 'requerimiento', name='requerimiento'),
    url(r'^malla/reto$', 'reto', name='reto'),
    url(r'^malla/reclamacion$', 'reclamacion', name='reclamacion'),
    url(r'^malla/horarios$', 'horarios', name='horarios'),
    url(r'^malla/soportes$', 'soportes', name='soportes'),
    url(r'^malla/lista$', 'lista', name='lista'),
    url(r'^malla/reportelista$', 'reporte_lista', name='reporte_lista'),
)
from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('malla.views',
	url(r'^malla/contratistas$', 'inicioContratista', name='inicioContratista'),
    url(r'^malla/infobasica$', 'datosBasicos', name='datos_basicos'),
    url(r'^malla/infocontacto$', 'datosContacto', name='datos_contacto'),
    url(r'^malla/areasconocimiento$', 'areasConocimiento', name='areas_conocimiento'),
    
    url(r'^malla/reclamacion$', 'reclamacion', name='reclamacion'),
    url(r'^malla/soportes$', 'soportes', name='soportes'),
    url(r'^malla/finalizar_contratista$', 'finalizar_contratista', name='finalizar_contratista'),

    url(r'^malla/lista$', 'lista', name='lista'),
    url(r'^malla/lista/(\d+)$', 'lista', name='lista'),
    url(r'^malla/eliminar-lista/(\d+)$', 'eliminar_lista', name='eliminar_lista'),
    url(r'^malla/reportelista$', 'reporte_lista', name='reporte_lista'),
    url(r'^malla/monitor$', 'monitor', name='monitor'),

    url(r'^malla/requerimiento$', 'requerimiento', name='requerimiento'),
    url(r'^malla/requerimiento/(\d+)$', 'requerimiento', name='requerimiento'),
    url(r'^malla/eliminar_requerimiento/(\d+)$', 'eliminar_requerimiento', name='eliminar_requerimiento'),
    url(r'^malla/listar-requerimientos$', 'listar_requerimientos', name='listar_requerimientos'),
)
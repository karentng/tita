from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('malla.views',
	url(r'^malla/contratistas$', 'inicioContratista', name='inicioContratista'),
    url(r'^malla/infobasica$', 'datosBasicos', name='datos_basicos'),
    url(r'^malla/infobasica/(\d+)$', 'datosBasicos', name='datos_basicos'), # modificar aun no esta listo, falta cambiar a session
    url(r'^malla/infocontacto$', 'datosContacto', name='datos_contacto'),
    url(r'^malla/areasconocimiento$', 'areasConocimiento', name='areas_conocimiento'),
    url(r'^malla/soportes$', 'soportes', name='soportes'),
    url(r'^malla/finalizar_contratista$', 'finalizar_contratista', name='finalizar_contratista'),

    url(r'^malla/eliminar-contratista/(\d+)$', 'eliminar_contratista', name='eliminar_contratista'),
    url(r'^malla/reporte_contratistas$', 'reporte_contratistas', name='reporte_contratistas'),

    url(r'^malla/reclamacion$', 'reclamacion', name='reclamacion'),
    url(r'^malla/reclamacion_modificar/(\d+)$', 'reclamacion_modificar', name='reclamacion_modificar'),
    url(r'^malla/listar_reclamaciones$', 'listar_reclamaciones', name='listar_reclamaciones'),
    url(r'^malla/listar_reclamaciones_contratista$', 'listar_reclamaciones_contratista', name='listar_reclamaciones_contratista'),

    url(r'^malla/lista$', 'lista', name='lista'),
    url(r'^malla/lista/(\d+)$', 'lista', name='lista'),
    url(r'^malla/eliminar-lista/(\d+)$', 'eliminar_lista', name='eliminar_lista'),
    url(r'^malla/reportelista$', 'reporte_lista', name='reporte_lista'),
    url(r'^malla/reportelistacontratista$', 'lista_contratista', name='lista_contratista'),
    url(r'^malla/lista_asignaturas$', 'lista_asignaturas', name='lista_asignaturas'),

    url(r'^malla/requerimiento$', 'requerimiento', name='requerimiento'),
    url(r'^malla/requerimiento/(\d+)$', 'requerimiento', name='requerimiento'),
    url(r'^malla/eliminar_requerimiento/(\d+)$', 'eliminar_requerimiento', name='eliminar_requerimiento'),
    url(r'^malla/listar-requerimientos$', 'listar_requerimientos', name='listar_requerimientos'),

    url(r'^malla/monitor$', 'monitor', name='monitor'),
    url(r'^malla/monitor/(\d+)$', 'monitor', name='monitor'),
    url(r'^malla/eliminar-monitor/(\d+)$', 'eliminar_monitor', name='eliminar_monitor'),
    url(r'^malla/listar-monitores$', 'listar_monitores', name='listar_monitores'),

    url(r'^malla/listar-contratistas$', 'listar_contratistas', name='listar_contratistas'),
    url(r'^malla/modificar-contratista/(\d+)$', 'modificarContratista', name='modificarContratista'),

    url(r'^malla/reporte-listas-contratistas$', 'lista_reporte_contratista', name='lista_reporte_contratista'),
)
from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.contrib import admin
from django.conf import settings


urlpatterns = patterns('cronograma.views',
    url(r'^programacion/cronograma_diplomado$',      'diplomado', name='cronograma_diplomado'),
    url(r'^programacion/filtro_diplomado$',      'filtro_diplomado', name='filtro_diplomado'),
    url(r'^programacion/cronograma_diplomado_modificar$',      'diplomado_modificar', name='cronograma_diplomado_modificar'),
    url(r'^programacion/cronograma_acompanamiento_modificar$',      'acompanamiento_modificar', name='cronograma_acompanamiento_modificar'),
    url(r'^programacion/cronograma_acompanamiento$',      'cronograma', name='cronograma_acompanamiento'),
    url(r'^programacion/cronograma_diplomado_soportes$',      'subirsoportes', name='cronograma_diplomado_soportes'),
    url(r'^programacion/cronograma_acompanamiento_soportes$',      'subirsoportesacompanamiento', name='cronograma_acompanamiento_soportes'),
    url(r'^programacion/addcurso$',      'curso', name='add_curso'),
    url(r'^programacion/estudiantes_curso$',      'prev_add_curso', name='prev_add_curso'),
    url(r'^programacion/addformador$',      'formador', name='add_formador'),
    url(r'^programacion/gestioncursos$',      'reporte_cursos', name='gestion_cursos'),
    url(r'^programacion/detallecurso/(?P<id>\d+)$',      'detalle_curso', name='detalle_curso'),
    url(r'^programacion/gestionformador$',      'reporte_formadores', name='gestion_formador'),
    url(r'^programacion/detalleformador/(?P<id>\d+)$',      'detalle_formador', name='detalle_formador'),
    
    url(r'^programacion/listaestudiantes/(?P<id>\d+)$',      'lista_estudiantes', name='lista_estudiantes'),
    url(r'^programacion/listaestudiantesacompanamiento/(?P<id>\d+)$',      'lista_acompanamiento', name='lista_acompanamiento'),
    url(r'^programacion/cancelarclase/(?P<id>\d+)$',      'cancelar_clase_diplomado', name='cancelar_clase'),
    url(r'^programacion/cancelarclaseacompanamiento/(?P<id>\d+)$',      'cancelar_clase_acompanamiento', name='cancelar_clase_acompanamiento'),
    url(r'^programacion/gestion$',      'gestion', name='gestion'),
    #url(r'^programacion/controlasistencia$',      'asistencia', name='asistencia'),
    #url(r'^programacion/controlasistencia/(\d+)/clases/(\d+)/asistencia$',       'asistencia', name="asistencia"),
    url(r'programacion/(\d+)/clases/(\d+)/asistenciadiplomado$',       'asistencia', name="asistencia"),
     url(r'programacion/(\d+)/clases/(\d+)/asistenciaacompanamiento$',       'asistencia_acompanamiento', name="asistencia_acompanamiento"),

    url(r'^programacion/actividad/(?P<id>\d+)$',      'actividad', name='actividad'),
    url(r'^programacion/actividad2/(?P<id>\d+)$',      'actividadacompanamiento', name='actividad_acompanamiento'),

    url(r'programacion/actividad/asistenciaClases/(\d+)/(\d+)$', 'asistenciaClases', name="asistenciaClases"),
    url(r'programacion/actividad/asistenciaClases2/(\d+)/(\d+)$', 'asistenciaClases2', name="asistenciaClases2"),

    url(r'^programacion/reporte_curso/(?P<id>\d+)$',      'reporte_conformacion_curso', name='reporte_conformacion_curso'),
)
from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('cronograma.views',
    url(r'^programacion/cronograma_diplomado$',      'diplomado', name='cronograma_diplomado'),
    url(r'^programacion/cronograma_diplomado_modificar$',      'diplomado_modificar', name='cronograma_diplomado_modificar'),
    url(r'^programacion/cronograma_acompanamiento_modificar$',      'acompanamiento_modificar', name='cronograma_acompanamiento_modificar'),
    url(r'^programacion/cronograma_acompanamiento$',      'cronograma', name='cronograma_acompanamiento'),
    url(r'^programacion/cronograma_diplomado_soportes$',      'subirsoportes', name='cronograma_diplomado_soportes'),
    url(r'^programacion/cronograma_acompanamiento_soportes$',      'subirsoportesacompanamiento', name='cronograma_acompanamiento_soportes'),
    url(r'^programacion/curso$',      'curso', name='cronograma_curso'),
    url(r'^programacion/formador$',      'formador', name='cronograma_formador'),
    url(r'^programacion/gestioncursos$',      'reporte_cursos', name='gestion_cursos'),

    
    
)
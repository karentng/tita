from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('cronograma.views',
    url(r'^programacion/cronograma_diplomado$',      'diplomado', name='cronograma_diplomado'),
    url(r'^programacion/cronograma_diplomado_modificar$',      'diplomado_modificar', name='cronograma_diplomado_modificar'),
    url(r'^programacion/cronograma_acompanamiento$',      'cronograma', name='cronograma_acompanamiento'),
    
)
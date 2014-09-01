from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('estudiante.views',
    url(r'^estudiante/inscripcion$',      'inscripcion', name="inscripcion_DE"),
    url(r'^estudiante/datosProfesionales$',      'datosProfesionales', name="laborales_DE"),
    url(r'^estudiante/certificacionesTIC$',      'certificacionesTIC', name="certificaciones_DE"),
    url(r'^estudiante/programasTIC$',      'programasTIC', name="programas_DE"),
    url(r'^estudiante/horarios$',      'horarios', name="horarios_DE"),
)

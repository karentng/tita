from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('estudiante.views',
	url(r'^estudiante/iniciar$',      'iniciar', name="iniciar_DE"),
    url(r'^estudiante/inscripcion$',      'inscripcion', name="inscripcion_DE"),
    url(r'^estudiante/datos-profesionales$',      'datosProfesionales', name="laborales_DE"),
    url(r'^estudiante/certificaciones-tic$',      'certificacionesTIC', name="certificaciones_DE"),
    url(r'^estudiante/programas-tic$',      'programasTIC', name="programas_DE"),
    url(r'^estudiante/soportes$',      'soportes', name="soportes_DE"),
    url(r'^estudiante/acta_compromiso$',      'acta_compromiso', name="acta_compromiso_DE"),
    url(r'^estudiante/finalizar$',      'finalizar', name="finalizar_DE"),
)

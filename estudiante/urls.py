from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('estudiante.views',
    url(r'^estudiante/inscripcion$',      'inscripcion', name="inscripcion_docente_estudiante"),
)

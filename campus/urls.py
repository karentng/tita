from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('campus.views',
    url(r'calificacion/cursos$',      'listar_cursos_profesor', name="listar_cursos_profesor"),
    url(r'calificacion/clases/(\d+)$',      'listar_clases_curso', name="listar_clases_curso"),
    url(r'calificacion/estudiantes/(\d+)/(\d+)$',      'listado_estudiantes', name="listado_estudiantes"),
)
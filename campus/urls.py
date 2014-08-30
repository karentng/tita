from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('campus.views',
    url(r'^campus/calificacion$',      'calificacion', name="calificacion_estudiantes"),
)
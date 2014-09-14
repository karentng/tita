from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('cronograma.views',
    url(r'^programacion/cronograma_diplomado$',      'cronograma', name="cronograma_diplomado"),
    url(r'^programacion/cronograma_acompanamiento$',      'cronograma', name="cronograma_acompanamiento"),
)
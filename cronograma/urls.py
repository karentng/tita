from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('cronograma.views',
    url(r'^cronograma/cronograma$',      'cronograma', name="cronograma"),
)
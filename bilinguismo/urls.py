from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('bilinguismo.views',
	url(r'bilinguismo/inscripcion$',      'inicioB', name="bilinguismo_inicio"),
    url(r'bilinguismo/datos-personales$',      'inscripcionB', name="bilinguismo_inscripcionB"),
    url(r'bilinguismo/datos-profesionales$',      'datosLaboralesB', name="bilinguismo_datosLaboralesB"),
    url(r'bilinguismo/formacion-academica$',      'formacionAcademicaB', name="bilinguismo_formacionAcademicaB"),
    url(r'bilinguismo/certificacion-bilinguismo$',      'certificacionB', name="bilinguismo_certificacionB"),
    url(r'bilinguismo/finalizar-bilinguismo/(\d+)$',      'finalizarB', name="bilinguismo_finalizarB"),

    # Eliminar Formacion Academica Bilinguismo
    url(r'bilinguismo/eliminarFormacionAcademicaB/(\d+)$',      'eliminarFormacionAcademicaB', name="eliminarFormacionAcademicaB"),
	# Eliminar Certificacion Bilinguismo
	url(r'bilinguismo/eliminarCertificacionB/(\d+)$',      'eliminarCertificacionB', name="eliminarCertificacionB"),
    #Resultados de Bilinguismo
    url(r'reporte$',      'reporte', name="reporteBilinguismo"),
    #url(r'impresion/(\d+)$',      'impresion', name="impresionBilinguismo"),
)
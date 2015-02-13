from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('estudiante.views',
	url(r'^estudiante/iniciar$',      'iniciar', name="iniciar_DE"),
    url(r'^estudiante/inscripcion$',      'inscripcion', name="inscripcion_DE"),
    url(r'^estudiante/datos-profesionales$',      'datosProfesionales', name="laborales_DE"),
    url(r'^estudiante/formacion-academica$',      'formacionAcademica', name="formacion_DE"),
    url(r'^estudiante/formacion-academica/eliminar/(\d+)$',      'eliminarFormacionAcademicaDE', name="eliminarFormacionAcademicaDE"),
    url(r'^estudiante/certificaciones-tic$',      'certificacionesTIC', name="certificaciones_DE"),
    url(r'^estudiante/certificaciones-tic/eliminar/(\d+)$',      'eliminarTicDE', name="eliminarTicDE"),
    url(r'^estudiante/acta_compromiso$',      'acta_compromiso', name="acta_compromisoDE"),
    url(r'^estudiante/imprimir_acta_compromiso$',      'imprimir_actaDE', name="imprimir_actaDE"),
    url(r'^estudiante/finalizar/(\d+)$',      'finalizar', name="finalizar_DE"),
    url(r'^estudiante/numeroInscripcionEstudiante/(\d+)$',      'numeroInscripcionEstudiante', name="numeroInscripcionEstudiante"),
    
    url(r'^estudiante/cohorte1$',      'cohorte1', name="me_cohorte1"),
)

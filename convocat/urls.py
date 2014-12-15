from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('convocat.views.inscripcion',

    url(r'^inscripcion/iniciar-inscripcion$',      'iniciarInscripcion', name="iniciarInscripcion"),
    url(r'^inscripcion/datos-personales$',      'datosPersonales', name="datosPersonales"),
    url(r'^inscripcion/formacion-academica$',   'formacionAcademica', name="formacionAcademica"),
    url(r'^inscripcion/formacion-academica/eliminar/(\d+)$', 'eliminarFormacionAcademica', name="eliminarFormacionAcademica"),

    url(r'^inscripcion/formacion-tics$',        'formacionTics', name="formacionTics"),
    url(r'^inscripcion/formacion-tics/eliminar/(\d+)$', 'eliminarFormacionTics', name="eliminarFormacionTics"),

    url(r'^inscripcion/conocimientos$',         'conocimientosEspecificos', name="conocimientosEspecificos"),
    url(r'^inscripcion/idiomas$',               'idiomasManejados', name="idiomasManejados"),
    url(r'^inscripcion/idiomas/eliminar/(\d+)$', 'eliminarIdioma', name="eliminarIdioma"),

    url(r'^inscripcion/experiencia-ensenanza$',             'experienciaEnsenanza', name="experienciaEnsenanza"),
    url(r'^inscripcion/experiencia-ensenanza/eliminar/(\d+)$', 'eliminarExperienciaEnsenanza', name="eliminarExperienciaEnsenanza"),

    url(r'^inscripcion/finalizar$',      'finalizar', name="finalizar"),
    url(r'^inscripcion/finalizada$',      'finalizada', name="finalizada"),

    url(r'^inscripcion/soportes$',      'soportes', name="soportes"),

)

urlpatterns += patterns('convocat.views.dashboard',
    url(r'^resultados$',      'dashboard', name="dashboard"),
    url(r'^resultadosME$',      'reporteME', name="reporteME"),
    url(r'^impresionME/(\d+)$',      'impresionME', name="impresionME"),
    url(r'^tablero_control/(\d*)$', 'tablero_control', name="tablero_control"),
    url(r'^tablero_control/actividades/(\d*)$', 'actividades', name="tableroControlActividades"),
    url(r'^tablero_control/guardarArchivos$', 'guardarArchivo', name="tableroControlGuardarArchivo"),
    url(r'^tablero_control/guardarEstadoDeAvance$', 'guardarEstadoDeAvance', name="tableroControlGuardarEstadoDeAvance"),
    url(r'^tablero_control/guardarGrupo/(\d*)$', 'guardarGrupo', name="tableroControlGuardarGrupo"),
    url(r'^tablero_control/guardarVariablesPorAula$', 'guardarVariablesPorAula', name="tableroControlGuardarVariablesPorAula"),
    url(r'^tablero_control/guardarVariablesPorSede$', 'guardarVariablesPorSede', name="tableroControlGuardarVariablesPorSede"),
    url(r'^tablero_control/eliminarGrupo/(\d*)$', 'eliminarGrupo', name="tableroControlEliminarGrupo"),
    url(r'^tablero_control/eliminarArchivo/(\d*)$', 'eliminarArchivo', name="tableroControlEliminarArchivo"),
    url(r'^obtenerGruposPorConceptoActividad/(\d*)$', 'obtenerGruposPorConceptoActividad', name="tableroControlObtenerGruposPorConceptoActividad"),
)


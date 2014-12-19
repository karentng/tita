from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('convocat2.views.inscripcion',

    url(r'^convocat2/inscripcion/iniciar-inscripcion$',      'iniciarInscripcion', name="iniciarInscripcion"),
    url(r'^convocat2/inscripcion/datos-personales$',      'datosPersonales', name="datosPersonales"),
    url(r'^convocat2/inscripcion/formacion-academica$',   'formacionAcademica', name="formacionAcademica"),
    url(r'^convocat2/inscripcion/formacion-academica/eliminar/(\d+)$', 'eliminarFormacionAcademica', name="eliminarFormacionAcademica"),

    url(r'^convocat2/inscripcion/formacion-tics$',        'formacionTics', name="formacionTics"),
    url(r'^convocat2/inscripcion/formacion-tics/eliminar/(\d+)$', 'eliminarFormacionTics', name="eliminarFormacionTics"),

    url(r'^convocat2/inscripcion/conocimientos$',         'conocimientosEspecificos', name="conocimientosEspecificos"),
    url(r'^convocat2/inscripcion/idiomas$',               'idiomasManejados', name="idiomasManejados"),
    url(r'^convocat2/inscripcion/idiomas/eliminar/(\d+)$', 'eliminarIdioma', name="eliminarIdioma"),

    url(r'^convocat2/inscripcion/experiencia-ensenanza$',             'experienciaEnsenanza', name="experienciaEnsenanza"),
    url(r'^convocat2/inscripcion/experiencia-ensenanza/eliminar/(\d+)$', 'eliminarExperienciaEnsenanza', name="eliminarExperienciaEnsenanza"),

    url(r'^convocat2/inscripcion/finalizar$',      'finalizar', name="finalizar"),
    url(r'^convocat2/inscripcion/finalizada$',      'finalizada', name="finalizada"),

    url(r'^convocat2/inscripcion/soportes$',      'soportes', name="soportes"),

)

urlpatterns += patterns('convocat2.views.dashboard',
    url(r'^convocat2/resultados$',      'dashboard', name="dashboard2"),
    url(r'^convocat2/resultadosME$',      'reporteME', name="reporteME2"),
    url(r'^convocat2/impresionME/(\d+)$',      'impresionME', name="impresionME2"),
    url(r'^convocat2/tablero_control/(\d*)$', 'tablero_control', name="tablero_control2"),
    url(r'^convocat2/tablero_control/actividades/(\d*)$', 'actividades', name="tableroControlActividades2"),
    url(r'^convocat2/tablero_control/guardarArchivos$', 'guardarArchivo', name="tableroControlGuardarArchivo2"),
    url(r'^convocat2/tablero_control/guardarEstadoDeAvance$', 'guardarEstadoDeAvance', name="tableroControlGuardarEstadoDeAvance2"),
    url(r'^convocat2/tablero_control/guardarGrupo/(\d*)$', 'guardarGrupo', name="tableroControlGuardarGrupo2"),
    url(r'^convocat2/tablero_control/guardarVariablesPorAula$', 'guardarVariablesPorAula', name="tableroControlGuardarVariablesPorAula2"),
    url(r'^convocat2/tablero_control/guardarVariablesPorSede$', 'guardarVariablesPorSede', name="tableroControlGuardarVariablesPorSede2"),
    url(r'^convocat2/tablero_control/eliminarGrupo/(\d*)$', 'eliminarGrupo', name="tableroControlEliminarGrupo2"),
    url(r'^convocat2/tablero_control/eliminarArchivo/(\d*)$', 'eliminarArchivo', name="tableroControlEliminarArchivo2"),
    url(r'^convocat2/obtenerGruposPorConceptoActividad/(\d*)$', 'obtenerGruposPorConceptoActividad', name="tableroControlObtenerGruposPorConceptoActividad2"),
)


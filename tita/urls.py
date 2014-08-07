from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tita.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^select2/', include('django_select2.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', 'convocat.views.inscripcion.index', name="publico"),
    url(r'^$', TemplateView.as_view(template_name='info/index.html'), name='home'),
    url(r'^objetivos/$', TemplateView.as_view(template_name='info/objetivos.html'), name="info_objetivos"),
    url(r'^funciones/$', TemplateView.as_view(template_name='info/funciones.html'), name="info_funciones"),
    url(r'^requisitos/$',TemplateView.as_view(template_name='info/requisitos.html'), name="info_requisitos"),
    url(r'^registrarse/$',TemplateView.as_view(template_name='info/registrarse.html'), name="info_registrarse"),


    #url(r'^formulario/$', 'convocat.views.inscripcion.formulario', name="formulario"),#
    #url(r'^registrarse/$', 'convocat.views.inscripcion.registrarse', name="publico_registrarse"),   
    #url(r'^login/$', 'django.contrib.auth.views.login', {'template_name':'publico/login.html'}, name= 'publico_login'),
    #url(r'^cerrar/$', 'django.contrib.auth.views.logout', {'template_name':'info.html'}, name= 'logout'),
    #url(r'^guardarHV/$', 'convocat.views.guardarHV', name= 'guardarHV'),
)


urlpatterns += patterns('convocat.views.inscripcion',
    url(r'^inscripcion/datos-personales$',      'datosPersonales', name="datosPersonales"),

    url(r'^inscripcion/info-clave$',      'informarClave', name="informarClave"),

    url(r'^inscripcion/formacion-academica$',   'formacionAcademica', name="formacionAcademica"),
    url(r'^inscripcion/formacion-academica/eliminar/(\d+)$', 'eliminarFormacionAcademica', name="eliminarFormacionAcademica"),

    url(r'^inscripcion/formacion-tics$',        'formacionTics', name="formacionTics"),
    url(r'^inscripcion/formacion-tics/eliminar/(\d+)$', 'eliminarFormacionTics', name="eliminarFormacionTics"),

    url(r'^inscripcion/conocimientos$',         'conocimientosEspecificos', name="conocimientosEspecificos"),
    url(r'^inscripcion/idiomas$',               'idiomasManejados', name="idiomasManejados"),
    url(r'^inscripcion/idiomas/eliminar/(\d+)$', 'eliminarIdioma', name="eliminarIdioma"),

    url(r'^experiencia-ensenanza$',             'experienciaEnsenanza', name="experienciaEnsenanza"),
    url(r'^inscripcion/experiencia-ensenanza/eliminar/(\d+)$', 'eliminarExperienciaEnsenanza', name="eliminarExperienciaEnsenanza"),

    url(r'^experiencia-otra$',                  'experienciaOtra', name="experienciaOtra"),
    url(r'^inscripcion/experiencia-otra/eliminar/(\d+)$', 'eliminarExperienciaOtra', name="eliminarExperienciaOtra"),

)
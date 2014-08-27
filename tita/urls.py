from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()


urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # solo en servidor de desarrollo


urlpatterns += patterns('',
    url(r'^select2/', include('django_select2.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', 'convocat.views.inscripcion.index', name="publico"),
    url(r'^$', TemplateView.as_view(template_name='info/index.html'), name='home'),
     url(r'^antecedentes/$', TemplateView.as_view(template_name='info/antecedentes.html'), name="info_antecedentes"),
    url(r'^infogeneral/$', TemplateView.as_view(template_name='info/infogeneral.html'), name="info_general"),
    url(r'^calendario/$', TemplateView.as_view(template_name='info/calendario.html'), name="info_calendario"),
    url(r'^requisitos/$',TemplateView.as_view(template_name='info/requisitos.html'), name="info_requisitos"),
    url(r'^registrarse/$',TemplateView.as_view(template_name='info/registrarse.html'), name="info_registrarse"),
    url(r'^contactenos/$',TemplateView.as_view(template_name='info/contactenos.html'), name="info_contactenos"),
    
)


urlpatterns += patterns('convocat.views.inscripcion',
    
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
    url(r'^dashboard$',      'dashboard', name="dashboard"),
)


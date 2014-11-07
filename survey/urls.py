from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
#import settings

admin.autodiscover()
#media_url = settings.MEDIA_URL.lstrip('/').rstrip('/')
 
urlpatterns = patterns('',
	# Examples:
	#url(r'^$', 'survey.views.Index', name='home'),
	#url(r'^survey/(?P<id>\d+)/$', 'survey.views.SurveyDetail', name='survey_detail'),
	#url(r'^confirm/(?P<uuid>\w+)/$', 'survey.views.Confirm', name='confirmation'),
	#url(r'^privacy/$', 'survey.views.privacy', name='privacy_statement'),
    url(r'padre$', 'survey.views.encuesta_padre', name='encuesta_padre'),
    url(r'docente$', 'survey.views.encuesta_docente', name='encuesta_docente'),
    url(r'estudiante$', 'survey.views.encuesta_estudiante', name='encuesta_estudiante'),
    url(r'nuevoEstudiante$', 'survey.views.encuesta_nuevo_estudiante', name='encuesta_nuevo_estudiante'),

    url(r'finalizada$', TemplateView.as_view(template_name='finalizada.html'), name="encuesta_finalizada"),

	# Uncomment the admin/doc line below to enable admin documentation:
	#url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	#url(r'^admin/', include(admin.site.urls)),
)

# media url hackery. le sigh. 
#urlpatterns += patterns('',
#    (r'^%s/(?P<path>.*)$' % media_url, 'django.views.static.serve',
#     { 'document_root': settings.MEDIA_ROOT, 'show_indexes':True }),
#)


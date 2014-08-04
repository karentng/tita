from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tita.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'convocat.views.index', name="publico"),
    url(r'^objetivos/$', 'convocat.views.objetivos', name="publico_objetivos"),
    url(r'^funciones/$', 'convocat.views.funciones', name="publico_funciones"),
    url(r'^requisitos/$', 'convocat.views.requisitos', name="publico_requisitos"),
    url(r'^registrarse/$', 'convocat.views.registrarse', name="publico_registrarse"),
    url(r'^formulario/$', 'convocat.views.formulario', name="formulario"),
    url(r'^obtenerMunicipios/$', 'convocat.views.obtenerMunicipios', name="obtenerMunicipios"),
     url(r'^registrarse/$', 'convocat.views.registrarse', name="publico_registrarse"),   
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name':'publico/login.html'}, name= 'publico_login'),
    url(r'^cerrar/$', 'django.contrib.auth.views.logout', {'template_name':'info.html'}, name= 'logout'),
    url(r'^guardarHV/$', 'convocat.views.guardarHV', name= 'guardarHV'),
)

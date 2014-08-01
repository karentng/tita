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

)

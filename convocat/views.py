from django.shortcuts import render
from .models import Municipio, TipoTitulo
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.context_processors import csrf
from django.contrib.auth.models import User

# Create your views here.

# vistas de la parte PUBLICA
def index(request):
    return render(request, 'publico/index.html', {
        'opcion_menu': 1
    })

def objetivos(request):
    return render(request, 'publico/objetivos.html', {
        'opcion_menu': 2
    })

def funciones(request):
    return render(request, 'publico/funciones.html', {
        'opcion_menu': 3
    })

def requisitos(request):
    return render(request, 'publico/requisitos.html', {
        'opcion_menu': 4
    })

# falta por hacer
def registrarse(request):
    return render(request, 'publico/registrarse.html', {
        'opcion_menu': 5
    })
def formulario(request):

    titulos = TipoTitulo.objects.all()

    return render(request, 'publico/formulario_aspirante.html', {
        'opcion_menu': 6,
        'titulos': titulos
    })

def obtenerMunicipios(request):
    municipios = serializers.serialize('json', Municipio.objects.all())
    return HttpResponse(municipios, mimetype='application/json')

def login(request):
    
    if request.POST:

        log = request.POST['username']
        contr = request.POST['password']
 
    return render_to_response('publico/registrarse.html', RequestContext(request, {'opcion_menu': 5}))

def registrarse(request):
    
    if request.POST:
        user = request.POST['correoe']
        passw = request.POST['contrasena']
        passwver = request.POST['verificarcontra']

        try:
            usuario = User.objects.get(username=user)
        except User.DoesNotExist:
            usuario = None

        if usuario != None:
            print "El usuario "+ usuario.username+ " ya existe"
            return render_to_response('publico/registrarse.html', RequestContext(request, {'log': 1, 'usuario': usuario.username}))
        
        elif passw == passwver:
            usuario = User()
            usuario.username = user
            usuario.password = passw
            usuario.save()
            return render_to_response('publico/registrarse.html', RequestContext(request, {'log': 2, 'usuario': usuario.username}))

        else:
            print "las contrasenas no coinciden" 
            return render_to_response('publico/registrarse.html', RequestContext(request, {'log': 3}))

    return render_to_response('publico/registrarse.html', RequestContext(request, {'log': 4}))
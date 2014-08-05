from django.shortcuts import render
from .models import Municipio, TipoTitulo
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from convocat.models import Aspirante, TipoDocumento, Municipio
from django.shortcuts import redirect

from convocat.forms import DatosPersonalesForm, FormacionAcademicaForm, FormacionTicsForm

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
    datosBasicos = DatosPersonalesForm()
    formacionAcademica = FormacionAcademicaForm()
    formacionTics = FormacionTicsForm()

    return render(request, 'publico/formulario_aspirante.html', {
        'opcion_menu': 6,
        'titulos': titulos,
        'datosBasicos': datosBasicos,
        'formacionAcademica': formacionAcademica,
        'formacionTics': formacionTics,
    })

def datosPersonales(request):
    if request.method == 'POST':
        form = DatosPersonalesForm(request.POST)
        if form.is_valid():
            #form = form.cleaned_data
            objeto = form.save(commit=False)
            objeto.puntuacion_hv = 0
            objeto.save()
            return redirect('formacionAcademica', objeto.id)
    
    datosBasicos = DatosPersonalesForm()

    return render(request, 'formularioHV/datosPersonales.html', {
        'opcion_menu': 6,
        'datosBasicos': datosBasicos,
    })

def formacionAcademica(request, idnt):
    if request.method == 'POST':
        form = FormacionAcademicaForm(request.POST)
        if form.is_valid():
            #form = form.cleaned_data
            objeto = form.save(commit=False)
            objeto.aspirante_id = idnt
            objeto.save()
            return redirect('formacionTics', idnt)

    formacionAcademica = FormacionAcademicaForm()

    return render(request, 'formularioHV/formacionAcademica.html', {
        'opcion_menu': 6,
        'formacionAcademica': formacionAcademica,
    })

def formacionTics(request, idnt):
    if request.method == 'POST':
        form = FormacionTicsForm(request.POST)
        if form.is_valid():
            #form = form.cleaned_data
            objeto = form.save(commit=False)
            objeto.aspirante_id = idnt
            objeto.save()
            return redirect('publico') # cambiar al que sigue

    formacionTics = FormacionTicsForm()

    return render(request, 'formularioHV/formacionTics.html', {
        'opcion_menu': 6,
        'formacionTics': formacionTics,
    })

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

def guardarHV(request):
    if request.POST:

        # obtencion de datos
        apellido1 = request.POST['apellido1']
        apellido2 = request.POST['apellido2']
        nombre1 = request.POST['nombre1']
        nombre2 = request.POST['nombre2']
        tipo_documento = request.POST['tipo_documento']
        num_doc = request.POST['num_documento']
        genero = request.POST['genero']
        nacionalidad = request.POST['nacionalidad']
        fecha_nacimiento = request.POST['fecha_nacimiento']
        municipio_nacimiento = request.POST['municipio_nacimiento']
        fijo = request.POST['fijo']
        municipio_actual = request.POST['municipio_actual']
        direccion = request.POST['direccion']
        celular = request.POST['celular']
        email = request.POST['email']

        try:
            aspirante = Aspirante.objects.get(numero_documento=num_doc)
        except Aspirante.DoesNotExist:
            aspirante = Aspirante()
        
        #asignacion
        aspirante.tipo_documento = TipoDocumento.objects.get(nombre=tipo_documento)
        aspirante.numero_documento = num_doc
        aspirante.apellido1 = apellido1
        aspirante.apellido2 = apellido2
        aspirante.nombre1 = nombre1
        aspirante.nombre2 = nombre2
        aspirante.genero = genero
        aspirante.nacionalidad = nacionalidad
        aspirante.fecha_nacimiento = fecha_nacimiento
        aspirante.municipio_nacimiento = Municipio.objects.get(id=municipio_nacimiento)
        aspirante.direccion = direccion
        aspirante.municipio = Municipio.objects.get(id=municipio_actual)
        aspirante.telefono = 222
        aspirante.celular = 111
        aspirante.email = email
        aspirante.direccion = direccion
        aspirante.puntuacion_hv = 100
        #guardado de aspirante
        aspirante.save()

        return render_to_response('publico/objetivos.html', RequestContext(request, {'opcion_menu': 1}))
    return render_to_response('publico/index.html', RequestContext(request, {'opcion_menu': 1}))
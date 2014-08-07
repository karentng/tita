from django.shortcuts import redirect, render, render_to_response, get_object_or_404
from django.core import serializers
from django.http import HttpResponse
from convocat.models import * 
from convocat.forms import *


def aspirante_sesion(request):
    valor = request.session.get('clave_aspirante')
    print "valor encontrado en session=",valor

    if not valor :
        return None
    try :
        miid, mihash = map(int,valor.split("-"))
        asp = Aspirante.objects.get(id=miid)
        print "aspirante con ese id =>", asp
        print "clava de ese aspirante", generar_clave(asp)
        if generar_clave(asp)==valor:
            return asp
        else :
            return None
    except Exception as ex:
        print "excepcion->", ex
        return None

def generar_clave(aspirante):
    mihash = (aspirante.numero_documento*44383)%1000000007
    clave = "%d-%d"%(aspirante.id, mihash)
    return clave



def datosPersonales(request):
    aspirante = aspirante_sesion(request)
    print "aspirante actual=", aspirante
    if request.method == 'POST':
        form = DatosPersonalesForm(request.POST, instance=aspirante)
        if form.is_valid():
            objeto = form.save()
            clave = generar_clave(objeto)
            request.session['clave_aspirante'] = clave
            print "clave=",clave
            return redirect('formacionAcademica')
    else :
        form = DatosPersonalesForm(instance=aspirante)

    return render(request, 'inscripcion/datosPersonales.html', {
        'form': form,
    })



def formacionAcademica(request):
    aspirante = aspirante_sesion(request)
    if not aspirante : redirect('datosPersonales')
    
    if request.method == 'POST':
        form = FormacionAcademicaForm(request.POST)
        if form.is_valid():
            objeto = form.save(commit=False)
            objeto.aspirante_id = aspirante.id
            objeto.save()
            return redirect('formacionAcademica') #Para evitar que al recargar la pagina cree nuevamente los datos
    else:
        form = FormacionAcademicaForm()

    estudios = aspirante.formacionacademica_set.all().order_by('fecha_terminacion')

    return render(request, 'inscripcion/formacionAcademica.html', {
        'form': form,
        'estudios': estudios,
    })

def eliminarFormacionAcademica(request, formAcadId):
    aspirante = aspirante_sesion(request)
    if not aspirante : redirect('datosPersonales')

    formAcad = get_object_or_404(FormacionAcademica.objects, aspirante_id=aspirante.id, id=formAcadId)
    formAcad.delete()

    return redirect('formacionAcademica')



def formacionTics(request):
    aspirante = aspirante_sesion(request)
    if not aspirante : redirect('formacionTics')

    if request.method == 'POST':
        form = FormacionTicsForm(request.POST)
        if form.is_valid():
            objeto = form.save(commit=False)
            objeto.aspirante_id = aspirante.id
            objeto.save()
            return redirect('formacionTics')
    else:
        form = FormacionTicsForm()

    estudios_tics = aspirante.formaciontics_set.all().order_by('fecha_terminacion')

    return render(request, 'inscripcion/formacionTics.html', {
        'estudios_tics': estudios_tics,
        'form': form,
    })

def eliminarFormacionTics(request, formTicsId):
    aspirante = aspirante_sesion(request)
    if not aspirante : redirect('formacionAcademica')

    formTics = get_object_or_404(FormacionTics.objects, aspirante_id=aspirante.id, id=formTicsId)
    formTics.delete()

    return redirect('formacionTics')



def conocimientosEspecificos(request):
    aspirante = aspirante_sesion(request)
    if not aspirante : redirect('formacionTics')

    try:
        conocimiento = aspirante.conocimientosespecificos

    except:
        conocimiento = None

    if request.method == 'POST':
        form = ConocimientosEspecificosForm(request.POST, instance=conocimiento)
        if form.is_valid():
            objeto = form.save(commit=False)
            objeto.aspirante_id = aspirante.id
            objeto.save()
            return redirect('idiomasManejados')
    else:
        form = ConocimientosEspecificosForm(instance=conocimiento)

    return render(request, 'inscripcion/conocimientosEspecificos.html', {
        'form': form, 
    })



def idiomasManejados(request):
    aspirante = aspirante_sesion(request)
    if not aspirante : redirect('conocimientosEspecificos')

    if request.method == 'POST':
        form = IdiomasManejadosForm(request.POST)
        if form.is_valid():
            objeto = form.save(commit=False)
            objeto.aspirante_id = aspirante.id
            objeto.save()
            #return redirect('experienciaFormadorTics') 

    else:
        form = IdiomasManejadosForm()
    idiomas = aspirante.idioma_set.all()

    return render(request, 'inscripcion/idiomasManejados.html', {
            'form': form,
            'idiomas':idiomas,
    })

def eliminarIdioma(request, formIdiomasId):
    aspirante = aspirante_sesion(request)
    if not aspirante : redirect('conocimientosEspecificos')

    formIdiomas = get_object_or_404(Idioma.objects, aspirante_id=aspirante.id, id=formIdiomasId)
    formIdiomas.delete()

    return redirect('idiomasManejados')

def experienciaEnsenanza(request):
    aspirante = aspirante_sesion(request)
    if not aspirante : redirect('idiomasManejados')
    
    if request.method == 'POST':
        form = ExperienciaEnsenanzaForm(request.POST)
        if form.is_valid():
            objeto = form.save(commit=False)
            objeto.aspirante_id = aspirante.id
            objeto.save()
            return redirect('experienciaEnsenanza') #Para evitar que al recargar la pagina cree nuevamente los datos
    else:
        form = ExperienciaEnsenanzaForm()

    experiencia_ens = aspirante.experienciaensenanza_set.all().order_by('fecha_fin')

    return render(request, 'inscripcion/experienciaEnsenanza.html', {
        'form': form,
        'experiencia_ens': experiencia_ens,
    })

def eliminarExperienciaEnsenanza(request, ExpeId):
    aspirante = aspirante_sesion(request)
    if not aspirante : redirect('experienciaEnsenanza')

    formExperienciaEns = get_object_or_404(ExperienciaEnsenanza.objects, aspirante_id=aspirante.id, id=ExpeId)
    formExperienciaEns.delete()

    return redirect('experienciaEnsenanza')

def experienciaOtra(request):
    aspirante = aspirante_sesion(request)
    if not aspirante : redirect('experienciaEnsenanza')
    
    if request.method == 'POST':
        form = ExperienciaOtraForm(request.POST)
        if form.is_valid():
            objeto = form.save(commit=False)
            objeto.aspirante_id = aspirante.id
            objeto.save()
            return redirect('experienciaOtra') #Para evitar que al recargar la pagina cree nuevamente los datos
    else:
        form = ExperienciaOtraForm()

    experiencias = aspirante.experienciaotra_set.all().order_by('fecha_fin')

    return render(request, 'inscripcion/experienciaOtra.html', {
        'form': form,
        'experiencias': experiencias,
    })

def eliminarExperienciaOtra(request, ExpeId):
    aspirante = aspirante_sesion(request)
    if not aspirante : redirect('experienciaOtra')

    formExperienciaOtra = get_object_or_404(ExperienciaOtra.objects, aspirante_id=aspirante.id, id=ExpeId)
    formExperienciaOtra.delete()

    return redirect('experienciaOtra')


def informarClave(request):

    return render(request, 'inscripcion/informacionClave.html')

"""
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
"""
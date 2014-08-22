from django.shortcuts import redirect, render, render_to_response, get_object_or_404
from django.core import serializers
from django.http import HttpResponse
from convocat.models import * 
from convocat.forms import *

def buscar_aspirante_por_clave(valor):
    try :
        miid, mihash = map(int,valor.split("-"))
        asp = Aspirante.objects.get(id=miid)
        if asp.numero_inscripcion()==valor:
            return asp
        else :
            return None
    except Exception as ex:
        return None

def aspirante_sesion(request):
    valor = request.session.get('clave_aspirante')
    print "valor encontrado en session=",valor

    if not valor :
        return None
    
    return buscar_aspirante_por_clave(valor)


def datosPersonales(request):
    aspirante = aspirante_sesion(request)
    if not aspirante : return redirect('home')
    print "aspirante actual=", aspirante
    if request.method == 'POST':
        form = DatosPersonalesForm(request.POST, instance=aspirante)
        if form.is_valid():
            objeto = form.save()
            clave = objeto.numero_inscripcion()
            request.session['clave_aspirante'] = clave
            print "clave=",clave
            return redirect('formacionAcademica')
    else :
        form = DatosPersonalesForm(instance=aspirante)

    return render(request, 'inscripcion/datosPersonales.html', {
        'form': form,
        'solo_lectura': aspirante.inscripcion_finalizada() if aspirante else False,
    })



def formacionAcademica(request):
    aspirante = aspirante_sesion(request)
    if not aspirante : return redirect('home')
    
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
        'solo_lectura':aspirante.inscripcion_finalizada(),
    })

def eliminarFormacionAcademica(request, formAcadId):
    aspirante = aspirante_sesion(request)
    if not aspirante : return redirect('home')

    formAcad = get_object_or_404(FormacionAcademica.objects, aspirante_id=aspirante.id, id=formAcadId)
    formAcad.delete()

    return redirect('formacionAcademica')



def formacionTics(request):
    aspirante = aspirante_sesion(request)
    if not aspirante : return redirect('home')

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
        'solo_lectura': aspirante.inscripcion_finalizada(),
    })

def eliminarFormacionTics(request, formTicsId):
    aspirante = aspirante_sesion(request)
    if not aspirante : return redirect('home')

    tics = get_object_or_404(FormacionTics.objects, aspirante_id=aspirante.id, id=formTicsId)
    tics.delete()

    return redirect('formacionTics')



def conocimientosEspecificos(request):
    aspirante = aspirante_sesion(request)
    if not aspirante : return redirect('home')

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
        'solo_lectura':aspirante.inscripcion_finalizada(), 
    })



def idiomasManejados(request):
    aspirante = aspirante_sesion(request)
    if not aspirante : return redirect('home')

    if request.method == 'POST':
        form = IdiomasManejadosForm(request.POST)
        if form.is_valid():
            objeto = form.save(commit=False)
            objeto.aspirante_id = aspirante.id
            objeto.save()
            return redirect('idiomasManejados') 
    else:
        form = IdiomasManejadosForm()
        
    idiomas = aspirante.idioma_set.all()

    return render(request, 'inscripcion/idiomasManejados.html', {
            'form': form,
            'idiomas':idiomas,
            'solo_lectura':aspirante.inscripcion_finalizada(),
    })

def eliminarIdioma(request, formIdiomasId):
    aspirante = aspirante_sesion(request)
    if not aspirante : return redirect('home')

    idioma = get_object_or_404(Idioma.objects, aspirante_id=aspirante.id, id=formIdiomasId)
    idioma.delete()

    return redirect('idiomasManejados')

def experienciaEnsenanza(request):
    aspirante = aspirante_sesion(request)
    if not aspirante : return redirect('home')
    
    if request.method == 'POST':
        form = ExperienciaFormadorForm(request.POST)
        if form.is_valid():
            objeto = form.save(commit=False)
            objeto.aspirante_id = aspirante.id
            objeto.save()
            form.save_m2m() # para guardar las areas (many-to-many)
            return redirect('experienciaEnsenanza') #Para evitar que al recargar la pagina cree nuevamente los datos
    else:
        form = ExperienciaFormadorForm()

    experiencias = aspirante.experienciaformador_set.all().order_by('fecha_fin')

    return render(request, 'inscripcion/experienciaEnsenanza.html', {
        'form': form,
        'experiencias': experiencias,
        'solo_lectura': aspirante.inscripcion_finalizada(),
    })

def eliminarExperienciaEnsenanza(request, ExpeId):
    aspirante = aspirante_sesion(request)
    if not aspirante : return redirect('home')

    experiencia = get_object_or_404(ExperienciaFormador.objects, aspirante_id=aspirante.id, id=ExpeId)
    experiencia.delete()

    return redirect('experienciaEnsenanza')

"""
def experienciaOtra(request):
    aspirante = aspirante_sesion(request)
    if not aspirante : return redirect('home')
    
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
        'solo_lectura': aspirante.inscripcion_finalizada()
    })

def eliminarExperienciaOtra(request, ExpeId):
    aspirante = aspirante_sesion(request)
    if not aspirante : return redirect('home')

    experienciaOtra = get_object_or_404(ExperienciaOtra.objects, aspirante_id=aspirante.id, id=ExpeId)
    experienciaOtra.delete()

    return redirect('experienciaOtra')
"""

def finalizar(request):
    aspirante = aspirante_sesion(request)
    if not aspirante : return redirect('home')

    numero_registro = request.session['clave_aspirante']
    #del request.session['clave_aspirante']
    if request.method=='POST': # presionaron finalizar
        aspirante.puntuacion_hv = aspirante.calcular_puntaje()
        aspirante.save()
        #del request.session['clave_aspirante']
        #return render(request, 'inscripcion/mostrarPuntaje.html', {'puntaje':aspirante.puntuacion_hv})
        return redirect('finalizada')


    return render(request, 'inscripcion/finalizar.html', {
        'numero_registro' : numero_registro,
    })

def finalizada(request):
    aspirante = aspirante_sesion(request)
    if not aspirante : return redirect('home')

    del request.session['clave_aspirante']
    return render(request, 'inscripcion/mostrarPuntaje.html', {'puntaje':aspirante.puntuacion_hv})



def iniciarInscripcion(request):
    if 'clave_aspirante' in request.session:
        del request.session['clave_aspirante']

    mensaje = ""
    if request.method == 'POST':
        form = ContinuarRegistroForm(request.POST)
        if form.is_valid():
            clave = form.cleaned_data['registro']
            asp = buscar_aspirante_por_clave(clave)
            if asp:
                request.session['clave_aspirante']=clave
                return redirect('datosPersonales')
            else :
                mensaje = "Numero de registro invalido"
    else:
        form = ContinuarRegistroForm()

    return render(request, 'inscripcion/iniciarInscripcion.html', {
        'mensaje':mensaje,
        'form' : form
    })


def soportes(request):

    aspirante = aspirante_sesion(request)
    if not aspirante : return redirect('home')

    if request.method == 'POST':
        form = DocumentosSoporteForm(request.POST, request.FILES, instance = aspirante.documentossoporte)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.aspirante = aspirante
            obj.save()
            return redirect('soportes')
    else:
        form = DocumentosSoporteForm(instance = aspirante.documentossoporte)

    return render(request, 'inscripcion/soportes.html', {
        'form': form,
        
    })
    

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
    })

def eliminarFormacionTics(request, formTicsId):
    aspirante = aspirante_sesion(request)
    if not aspirante : return redirect('home')

    formTics = get_object_or_404(FormacionTics.objects, aspirante_id=aspirante.id, id=formTicsId)
    formTics.delete()

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
    if not aspirante : return redirect('home')

    formIdiomas = get_object_or_404(Idioma.objects, aspirante_id=aspirante.id, id=formIdiomasId)
    formIdiomas.delete()

    return redirect('idiomasManejados')

def experienciaEnsenanza(request):
    aspirante = aspirante_sesion(request)
    if not aspirante : return redirect('home')
    
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
    if not aspirante : return redirect('home')

    formExperienciaEns = get_object_or_404(ExperienciaEnsenanza.objects, aspirante_id=aspirante.id, id=ExpeId)
    formExperienciaEns.delete()

    return redirect('experienciaEnsenanza')

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
    })

def eliminarExperienciaOtra(request, ExpeId):
    aspirante = aspirante_sesion(request)
    if not aspirante : return redirect('home')

    formExperienciaOtra = get_object_or_404(ExperienciaOtra.objects, aspirante_id=aspirante.id, id=ExpeId)
    formExperienciaOtra.delete()

    return redirect('experienciaOtra')


def finalizar(request):
    aspirante = aspirante_sesion(request)
    if not aspirante : return redirect('home')

    numero_registro = request.session['clave_aspirante']
    del request.session['clave_aspirante']
    return render(request, 'inscripcion/finalizar.html', {
        'numero_registro' : numero_registro,
        })

#encoding: utf-8
from django.shortcuts import redirect, render, render_to_response, get_object_or_404
from django.core import serializers
from convocat.models import * 
from django.db.models import Count
import json
from estudiante.forms import EstudianteForm, InfoLaboralForm, CertificacionTICForm, ContinuarRegistroFormDE, FormacionAcademicaMEForm
from campus.models import CertificacionTIC, Asignatura, Estudiante
from estudiante.models import InfoLaboral, FormacionAcademicaME
from datetime import datetime
import json

def iniciar(request):
    if 'clave_estudiante' in request.session:
        del request.session['clave_estudiante']

    mensaje = ""
    if request.method == 'POST':
        form = ContinuarRegistroFormDE(request.POST)
        if form.is_valid():
            clave = form.cleaned_data['registro']
            asp = buscar_estudiante_por_clave(clave)
            if asp:
                request.session['clave_estudiante']=clave
                return redirect('inscripcion_DE')
            else :
                mensaje = "Numero de registro invalido"
    else:
        form = ContinuarRegistroFormDE()

    return render(request, 'inscripcion/iniciar_inscripcion.html', {
        'mensaje':mensaje,
        'form' : form
    })

def buscar_estudiante_por_clave(valor):
    try :
        miid, mihash = map(int,valor.split("-"))
        asp = Estudiante.objects.get(id=miid)

        if asp.numero_inscripcion()==valor:
            return asp
        else :
            return None
    except Exception as ex:
        return None

def estudiante_sesion(request):
    valor = request.session.get('clave_estudiante')
    print "valor encontrado en session=",valor

    if not valor :
        return None
    return buscar_estudiante_por_clave(valor)

def inscripcion(request):
    estudiante = estudiante_sesion(request)
    print "aspirante actual=", estudiante
    if request.method == 'POST':
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            objeto = form.save()
            clave = objeto.numero_inscripcion()
            request.session['clave_estudiante'] = clave
            print "clave=",clave
            return redirect('laborales_DE')
    else :
        form = EstudianteForm(instance=estudiante)
    return render(request, 'inscripcion/datosEstudiante.html', {
        'form': form,
    })

def datosProfesionales(request):
    estudiante = estudiante_sesion(request)
    if not estudiante : return redirect('home')
    try:
        datos = InfoLaboral.objects.get(estudiante=estudiante)
    except Exception as ex:
        datos = None
    print datos
    if request.method == 'POST':
        form = InfoLaboralForm(request.POST, instance=datos)
        if form.is_valid():
            objeto = form.save(commit=False)
            objeto.estudiante = estudiante
            objeto.save()
            form.save_m2m()
            return redirect('formacion_DE')
    else :
        form = InfoLaboralForm(instance=datos)

    numero_registro = request.session['clave_estudiante']

    return render(request, 'inscripcion/datosLaborales.html', {
        'form': form,
        'clave': numero_registro
    })

def formacionAcademica(request):
    estudiante = estudiante_sesion(request)
    if not estudiante : return redirect('home')
    if request.method == 'POST':
        form = FormacionAcademicaMEForm(request.POST)
        if form.is_valid():
            objeto = form.save(commit=False)
            objeto.estudiante = estudiante
            objeto.save()
            return redirect('formacion_DE')
    else :
        form = FormacionAcademicaMEForm()

    estudios = FormacionAcademicaME.objects.filter(estudiante=estudiante)

    numero_registro = request.session['clave_estudiante']

    return render(request, 'inscripcion/formacion_academica.html', {
        'form': form,
        'estudios': estudios,
        'clave': numero_registro,
        'tiene_estudios': len(estudios)
    })

def eliminarFormacionAcademicaDE(request, formAcadId):
    estudiante = estudiante_sesion(request)
    if not estudiante : return redirect('home')

    formAcad = get_object_or_404(FormacionAcademicaME.objects, estudiante=estudiante, id=formAcadId)
    formAcad.delete()

    return redirect('formacion_DE')

def certificacionesTIC(request):
    estudiante = estudiante_sesion(request)
    if not estudiante : return redirect('home')
    estudios = FormacionAcademicaME.objects.filter(estudiante=estudiante)
    if not len(estudios):
        return redirect('formacion_DE')
    error = False
    if request.method == 'POST':
        form = CertificacionTICForm(request.POST)
        if form.is_valid():
            objeto = form.save(commit=False)
            objeto.estudiante = estudiante

            dias_dif =  objeto.fecha_terminacion - objeto.fecha_inicio
            dias_dif = dias_dif.days
            if dias_dif < 0:
                error = "La fecha de terminación debe ser después de la fecha inicial"
            else:
                # se supone el hecho que se estudia 8 horas diarias
                if objeto.duracion == 40 and dias_dif < 5:
                    error = "Muy poco tiempo para realizar un curso de 40 horas, por favor revise las fechas"
                elif objeto.duracion == 90 and dias_dif < 12:
                    error = "Muy poco tiempo para realizar un curso de 90 horas, por favor revise las fechas"
                elif objeto.duracion == 140 and dias_dif < 18:
                    error = "Muy poco tiempo para realizar un curso de 140 horas, por favor revise las fechas"
                elif objeto.duracion == 141 and dias_dif < 18:
                    error = "Muy poco tiempo para realizar un curso de más de 140 horas, por favor revise las fechas"
                else:
                    objeto.save()
                    return redirect('certificaciones_DE')        
    else :
        form = CertificacionTICForm()

    certificaciones = CertificacionTIC.objects.filter(estudiante=estudiante)

    numero_registro = request.session['clave_estudiante']
    return render(request, 'inscripcion/certificaciones_DE.html', {
        'form': form,
        'certificaciones': certificaciones,
        'clave': numero_registro,
        'error': error,
    })

def eliminarTicDE(request, ticId):
    estudiante = estudiante_sesion(request)
    if not estudiante : return redirect('home')

    cerTic = get_object_or_404(CertificacionTIC.objects, estudiante=estudiante, id=ticId)
    cerTic.delete()

    return redirect('certificaciones_DE')

def acta_compromiso(request):
    estudiante = estudiante_sesion(request)
    if not estudiante : return redirect('home')

    numero_registro = request.session['clave_estudiante']
    ie = InfoLaboral.objects.get(estudiante=estudiante).get_sede_display

    return render(request, 'inscripcion/acta_compromiso.html', {
        'clave': numero_registro,
        'estudiante': estudiante,
        'ie': ie,
        'hoy': datetime.now()
    })

def imprimir_actaDE(request):
    estudiante = estudiante_sesion(request)
    if not estudiante : return redirect('home')

    ie = InfoLaboral.objects.get(estudiante=estudiante).institucion_educativa

    return render(request, 'inscripcion/imprimir_acta_compromiso.html', {
        'estudiante': estudiante,
        'ie': ie,
        'hoy': datetime.now()
    })

def finalizar(request, acta):
    estudiante = estudiante_sesion(request)
    if not estudiante : return redirect('home')

    if request.method=='POST': # presionaron finalizar
        del request.session['clave_estudiante']
        return redirect('iniciar_DE')

    estudiante.acta_compromiso = int(acta)
    estudiante.save()
    numero_registro = request.session['clave_estudiante']

    return render(request, 'inscripcion/finalizar_DE.html', {
        'estudiante': estudiante,
        'clave': numero_registro,
        'acta': acta,
    })

def programasTIC(request):
    estudiante = estudiante_sesion(request)
    if not estudiante : return redirect('home')
    if request.method == 'POST':
        form = ProgramaTICForm(request.POST)
        if form.is_valid():
            objeto = form.save(commit=False)
            objeto.estudiante = estudiante
            objeto.save()
            return redirect('programas_DE')
    else :
        form = ProgramaTICForm()

    programas = ProgramaTIC.objects.filter(estudiante = estudiante)

    numero_registro = request.session['clave_estudiante']
    return render(request, 'inscripcion/programas_DE.html', {
        'form': form,
        'programas': programas,
        'clave': numero_registro
    })

def soportes(request):
    estudiante = estudiante_sesion(request)
    if not estudiante : return redirect('home')

    try:
        soportes = estudiante.documentossoporte
    except:
        soportes = None
    if request.method == 'POST':
        form = DocumentosSoporteForm(request.POST, request.FILES, instance = soportes)
        if form.is_valid():
            objeto = form.save(commit=False)
            objeto.estudiante = estudiante
            objeto.save()
            return redirect('soportes_DE')
    else :
        form = DocumentosSoporteForm(instance = soportes)

    numero_registro = request.session['clave_estudiante']
    return render(request, 'inscripcion/soportes_DE.html', {
        'form': form,
        'clave': numero_registro
    })




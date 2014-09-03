#encoding: utf-8
from django.shortcuts import redirect, render, render_to_response, get_object_or_404
from django.core import serializers
from convocat.models import * 
from django.db.models import Count
import json
from estudiante.forms import EstudianteForm, InfoLaboralForm, CertificacionTICForm, ProgramaTICForm
from campus.models import CertificacionTIC, ProgramaTIC, Asignatura


def inscripcion(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            objeto = form.save()
            request.session['clave_estudiante'] = objeto.id
            return redirect('laborales_DE')
    else :
        form = EstudianteForm()
    return render(request, 'inscripcion/datosEstudiante.html', {
        'form': form,
    })

def datosProfesionales(request):
    if request.method == 'POST':
        form = InfoLaboralForm(request.POST)
        if form.is_valid():
            objeto = form.save(commit=False)
            objeto.estudiante_id = request.session.get('clave_estudiante')
            objeto.save()
            return redirect('certificaciones_DE')
    else :
        form = InfoLaboralForm()
    return render(request, 'inscripcion/datosLaborales.html', {
        'form': form,
    })

def certificacionesTIC(request):
    if request.method == 'POST':
        form = CertificacionTICForm(request.POST)
        if form.is_valid():
            objeto = form.save(commit=False)
            objeto.estudiante_id = request.session.get('clave_estudiante')
            objeto.save()
            return redirect('certificaciones_DE')
    else :
        form = CertificacionTICForm()

    certificaciones = CertificacionTIC.objects.filter(estudiante__id = request.session.get('clave_estudiante'))

    return render(request, 'inscripcion/certificaciones_DE.html', {
        'form': form,
        'certificaciones': certificaciones,
    })

def programasTIC(request):
    if request.method == 'POST':
        form = ProgramaTICForm(request.POST)
        if form.is_valid():
            objeto = form.save(commit=False)
            objeto.estudiante_id = request.session.get('clave_estudiante')
            objeto.save()
            return redirect('programas_DE')
    else :
        form = ProgramaTICForm()

    programas = ProgramaTIC.objects.filter(estudiante__id = request.session.get('clave_estudiante'))

    return render(request, 'inscripcion/programas_DE.html', {
        'form': form,
        'programas': programas,
    })

def horarios(request):
    if request.method == 'POST':
        form = HorarioForm(request.POST)
        if form.is_valid():
            objeto = form.save(commit=False)
            objeto.estudiante_id = request.session.get('clave_estudiante')
            objeto.save()
            return redirect('horarios_DE')
    else :
        form = HorarioForm()

    DIAS = ['Lunes','Martes','Miércoles','Jueves','Viernes']
    horarios = []
    hs = Horario.objects.filter(estudiante__id = request.session.get('clave_estudiante'))
    for i in hs:
        #nombre = unicode(Municipio.objects.get(id=i['municipio']).nombre)
        print i.dia
        horarios.append({'dia': DIAS[i.dia-1], 'inicio': i.inicio, 'fin': i.fin, 'curso': Asignatura.objects.get(id=i.curso_id).nombre})

    return render(request, 'inscripcion/horarios.html', {
        'form': form,
        'horarios': horarios,
    })


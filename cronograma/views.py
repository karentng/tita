from django.shortcuts import render
from cronograma.forms import EventosAcompanamientoForm, EventosDiplomadoForm
from campus.models import Clase
import json
from django.shortcuts import redirect, render, render_to_response
from datetime import datetime, date, timedelta
from math import ceil

def cronograma(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = EventosAcompanamientoForm(request.POST)
        form.tipo = "asa"
        
        if form.is_valid():
            objeto = Clase()
            objeto = form.save()
            objeto.tipo = "2"
            objeto.save()

            return redirect('cronograma_acompanamiento')
    else:

        form = EventosAcompanamientoForm()
        
    eventos = Clase.objects.filter(tipo="2")
    events = []
    for i in eventos:
        inicio = i.fecha_inicio
        #fin = i.fecha_finalizacion

        hora_inicio = [i.fecha_inicio.hour, i.fecha_inicio.minute, 0]
        #hora_finalizacion = [i.fecha_finalizacion.hour, i.fecha_finalizacion.minute, 0]
        hora_finalizacion = [i.fecha_inicio.hour + i.duracion, i.fecha_inicio.minute, 0]

        diasTotal = 1
        
        #diasEvento = 1
        diasEvento = []
        for j in range(0, diasTotal+1):
            aux = inicio + timedelta(days = j)
            diasEvento.append([aux.year, aux.month-1, aux.day])

        events.append({
            'id': i.id,
            'nombre': i.nombre,
            'descripcion': i.descripcion,
            'hora_inicio': hora_inicio,
            'hora_finalizacion': hora_finalizacion,
            'diasEvento': diasEvento,
            'institucion': i.get_institucion_display()
        })
    '''
    for i in eventos:
        inicio = i.fecha_inicio
        fin = i.fecha_finalizacion
        events.append({
            'nombre': i.nombre,
            'inicio': [inicio.year, inicio.month-1, inicio.day],
            'fin': [fin.year, fin.month-1, fin.day],
            'descripcion': i.descripcion
        })'''
    
    return render(request, 'cronograma.html', {
        'formAcompanamiento': form,
        'eventos': json.dumps(events)
    })

def menor10(val):
    if val < 10:
        return "0"+str(val)
    return str(val)

def diplomado(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = EventosDiplomadoForm(request.POST)
        if form.is_valid():
            objeto = Clase()
            objeto = form.save()
            objeto.tipo = "1"
            objeto.save()
            return redirect('cronograma_diplomado')
    else:
        form = EventosDiplomadoForm()

    eventos = Clase.objects.filter(tipo="1")
    events = []

    for i in eventos:
        inicio = i.fecha_inicio
        fin = i.fecha_finalizacion

        hora_inicio = [i.fecha_inicio.hour, i.fecha_inicio.minute, 0]
        #hora_finalizacion = [i.fecha_finalizacion.hour, i.fecha_finalizacion.minute, 0]

        diasTotal = (fin - inicio).days
        
        diasEvento = []
        for j in range(0, diasTotal+1):
            aux = inicio + timedelta(days = j)
            diasEvento.append([aux.year, aux.month-1, aux.day])

        events.append({
            'id': i.id,
            'nombre': i.nombre,
            'descripcion': i.descripcion,
            'hora_inicio': hora_inicio,
            'hora_finalizacion': hora_finalizacion,
            'diasEvento': diasEvento
        })
    
    return render(request, 'diplomado.html', {
        'formDiplomado': form,
        'eventos': json.dumps(events)
    })

def diplomado_modificar(request):
    idCurso = request.GET.get('idCurso')
    curso = Clase.objects.filter(id=idCurso)[0]
    if request.method == 'POST':
        form = EventosDiplomadoForm(request.POST, instance=curso)
        if form.is_valid():
            objeto = form.save()
            objeto.save()
            return redirect('cronograma_diplomado')
    else:
        form = EventosDiplomadoForm(instance=curso)

    return render(request, 'diplomado_modificar.html', {
        'form': form,
    })
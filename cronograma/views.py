from django.shortcuts import render
from cronograma.forms import EventosAcompanamientoForm, EventosDiplomadoForm
from cronograma.models import EventosAcompanamiento, EventosDiplomado
import json
from django.shortcuts import redirect, render, render_to_response

def cronograma(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = EventosAcompanamientoForm(request.POST)
        if form.is_valid():
            objeto = form.save()
            return redirect('cronograma_acompanamiento')
    else:
        form = EventosAcompanamientoForm()

    eventos = EventosAcompanamiento.objects.all()
    events = []

    for i in eventos:
        inicio = i.fecha_inicio
        fin = i.fecha_finalizacion
        events.append({
            'nombre': i.nombre,
            'inicio': [inicio.year, inicio.month-1, inicio.day],
            'fin': [fin.year, fin.month-1, fin.day],
            'descripcion': i.descripcion
        })
    
    return render(request, 'cronograma.html', {
        'formAcompanamiento': form,
        'eventos': json.dumps(events)
    })

def diplomado(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = EventosDiplomadoForm(request.POST)
        if form.is_valid():
            objeto = form.save()
            return redirect('cronograma_diplomado')
    else:
        form = EventosDiplomadoForm()

    eventos = EventosDiplomado.objects.all()
    events = []

    for i in eventos:
        inicio = i.fecha_inicio
        fin = i.fecha_finalizacion
        events.append({
            'nombre': i.nombre,
            'inicio': [inicio.year, inicio.month-1, inicio.day],
            'fin': [fin.year, fin.month-1, fin.day],
            'descripcion': i.descripcion
        })
    
    return render(request, 'diplomado.html', {
        'formDiplomado': form,
        'eventos': json.dumps(events)
    })

from django.shortcuts import render
from cronograma.forms import *
from cronograma.models import Evento
import json

def cronograma(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            objeto = form.save()
            return redirect('cronograma')
    else:
        evento = EventoForm()

    eventos = Evento.objects.all()
    events = []

    for i in eventos:
        inicio = i.fecha_inicio
        fin = i.fecha_finalizacion
        events.append({
            'nombre': i.nombre,
            'inicio': [inicio.year, inicio.month, inicio.day],
            'fin': [fin.year, fin.month, fin.day],
            'descripcion': i.descripcion
        })
    
    return render(request, 'cronograma.html', {
        'evento': evento,
        'eventos': json.dumps(events)
    })

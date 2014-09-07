from django.shortcuts import render
from cronograma.forms import *


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

    return render(request, 'cronograma.html', {
        'evento': evento,
        'eventos': eventos
    })

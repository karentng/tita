from django.shortcuts import render
from cronograma.forms import *


def cronograma(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        evento = EventoForm(request.POST)
        # check whether it's valid:
        if evento.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        evento = EventoForm()

    return render(request, 'cronograma.html', {'evento': evento})

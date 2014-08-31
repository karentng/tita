#encoding: utf-8
from django.shortcuts import redirect, render, render_to_response, get_object_or_404
from django.core import serializers
from convocat.models import * 
from django.db.models import Count
import json
from estudiante.forms import EstudianteForm


def inscripcion(request):

    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            objeto = form.save()
            return redirect('home')
    else :
        form = EstudianteForm()
    return render(request, 'inscripcion/inscripcion.html', {
        'form': form,
    })
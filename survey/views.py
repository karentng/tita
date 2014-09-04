# encoding: utf-8
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core import urlresolvers
from django.contrib import messages
import datetime
#import settings

from models import Question, Survey, Category
from forms import ResponseForm


def encuesta_padre(request):
    survey = Survey.objects.get(id=1)
    
    if request.method == 'POST':
        form = ResponseForm(request.POST, survey=survey)
        if form.is_valid():
            form.save()
            return redirect('encuesta_finalizada')
        else:
            print "error llenando", form.errors
    else :
        form = ResponseForm(survey=survey)

    # customizar form de acuerdo a la encuesta para padres
    form.fields['jornada'].label = u"Jornada en la que estudia su hijo(a)"
    form.fields['institucion'].label = u"Institución donde estudia su hijo(a)"

    camposMaterias = [form['question_%d'%x] for x in xrange(10,29) ]
    camposDispositivos = [form['question_%d'%x] for x in xrange(57,61) ]
    camposUsos = [form['question_%d'%x] for x in xrange(65,84)]
    camposHerramientas = [form['question_%d'%x] for x in xrange(37,52) ]
    camposExpectativas = [form['question_%d'%x] for x in xrange(90,98) ]
    camposLamentaria = [form['question_%d'%x] for x in xrange(100,108) ]

    return render(request, 'encuesta_padre.html', {
        'form': form,
        'camposMaterias1': camposMaterias[:10],
        'camposMaterias2': camposMaterias[10:],
        'camposDispositivos': camposDispositivos,
        'camposHerramientas' : camposHerramientas,
        'camposUsos' : camposUsos,
        'camposExpectativas' : camposExpectativas,
        'camposLamentaria' : camposLamentaria,
    })


def encuesta_docente(request):
    survey = Survey.objects.get(id=2)
    category_items = list(survey.category_set.all())    
    
    if request.method == 'POST':
        form = ResponseForm(request.POST, survey=survey)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print "error llenando", form.errors
    else :
        form = ResponseForm(survey=survey)

    #camposMaterias = [form['question_%d'%x] for x in xrange(10,29) ]

    return render(request, 'encuesta_docente.html', {
        'form': form,
        #'camposMaterias1': camposMaterias[:10],
    })

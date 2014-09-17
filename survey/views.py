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
    form.fields['jornada'].label = u"1. Jornada en la que estudia su hijo(a)"
    form.fields['nombre'].label = u"3. Nombre(s) y apellidos del padre de familia o acudiente"
    form.fields['institucion'].label = u"5. Nombre de la institución educativa en la que estudia su hijo(a)"

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
        'camposDispositivos1': camposDispositivos[:2],
        'camposDispositivos2': camposDispositivos[2:],
        'camposHerramientas1' : camposHerramientas[:7],
        'camposHerramientas2' : camposHerramientas[7:],
        'camposUsos1' : camposUsos[:10],
        'camposUsos2' : camposUsos[10:],
        'camposExpectativas1' : camposExpectativas[:4],
        'camposExpectativas2' : camposExpectativas[4:],
        'camposLamentaria1' : camposLamentaria[:4],
        'camposLamentaria2' : camposLamentaria[4:],
    })


def encuesta_docente(request):
    survey = Survey.objects.get(id=2)
    category_items = list(survey.category_set.all())    
    
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
    form.fields['jornada'].label = u"1. Jornada en la que estudias"
    form.fields['institucion'].label = u"2. Nombre de tu institución educativa"
    form.fields['nombre'].label = u"3. Nombre y apellidos"


    camposMaterias = [form['question_%d'%x] for x in xrange(118,137) ]
    camposHerramientas = [form['question_%d'%x] for x in xrange(146,175) ]
    camposDispositivos = [form['question_%d'%x] for x in xrange(187,191) ]
    camposUsos = [form['question_%d'%x] for x in xrange(195,215) ]
    camposConcurso = [form['question_%d'%x] for x in xrange(219,227) ]
    camposLamentaria = [form['question_%d'%x] for x in xrange(261,269) ]

    return render(request, 'encuesta_docente.html', {
        'form': form,
        'camposMaterias1': camposMaterias[:10],
        'camposMaterias2': camposMaterias[10:],
        'camposHerramientas1': camposHerramientas[:14],
        'camposHerramientas2': camposHerramientas[14:],
        'camposDispositivos1': camposDispositivos[:2],
        'camposDispositivos2': camposDispositivos[2:],
        'camposUsos1': camposUsos[:10],
        'camposUsos2': camposUsos[10:],
        'camposConcurso1': camposConcurso[:4],
        'camposConcurso2': camposConcurso[4:],
        'camposLamentaria1': camposLamentaria[:4],
        'camposLamentaria2': camposLamentaria[4:],
    })

def encuesta_estudiante(request):
    survey = Survey.objects.get(id=3)
    category_items = list(survey.category_set.all())    
    
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
    form.fields['jornada'].label = u"1. Jornada"
    form.fields['institucion'].label = u"2. Nombre y apellidos"
    form.fields['nombre'].label = u"3. Nombre y apellidos"


    camposMaterias = [form['question_%d'%x] for x in xrange(282,301) ]
    camposRecursos = [form['question_%d'%x] for x in xrange(305,312) ]
    camposDispositivos = [form['question_%d'%x] for x in xrange(316,320) ]
    camposInternet = [form['question_%d'%x] for x in xrange(323,341) ]
    camposDispos = [form['question_%d'%x] for x in xrange(346,354) ]
    camposLamentaria = [form['question_%d'%x] for x in xrange(356,364) ]

    return render(request, 'encuesta_estudiante.html', {
        'form': form,
        'camposMaterias1': camposMaterias[:10],
        'camposMaterias2': camposMaterias[10:],
        'camposRecursos1': camposRecursos[:4],
        'camposRecursos2': camposRecursos[4:],
        'camposDispositivos1': camposDispositivos[:2],
        'camposDispositivos2': camposDispositivos[2:],
        'camposInternet1': camposInternet[:9],
        'camposInternet2': camposInternet[9:],
        'camposDispos1': camposDispos[:4],
        'camposDispos2': camposDispos[4:],
        'camposLamentaria1': camposLamentaria[:4],
        'camposLamentaria2': camposLamentaria[4:],
    })

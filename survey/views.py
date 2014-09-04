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


def Index(request):
    return render(request, 'index.html')

def SurveyDetail(request, id):
    survey = Survey.objects.get(id=id)
    category_items = Category.objects.filter(survey=survey)
    categories = [c.name for c in category_items]
    print 'categories for this survey:'
    print categories
    if request.method == 'POST':
        form = ResponseForm(request.POST, survey=survey)
        if form.is_valid():
            response = form.save()
            return HttpResponseRedirect("/confirm/%s" % response.interview_uuid)
    else:
        form = ResponseForm(survey=survey)
        print form
        # TODO sort by category
    return render(request, 'survey.html', {'response_form': form, 'survey': survey, 'categories': categories})

def Confirm(request, uuid):
    email = settings.support_email
    return render(request, 'confirm.html', {'uuid':uuid, "email": email})

def privacy(request):
    return render(request, 'privacy.html')


def encuesta_padre(request):
    survey = Survey.objects.get(id=1)
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

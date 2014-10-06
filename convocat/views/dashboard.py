from django.shortcuts import redirect, render, render_to_response, get_list_or_404
from django.core import serializers
from convocat.models import * 
from django.db.models import Count
from campus.models import Estudiante
import json


def dashboard(request):
    mejores = Aspirante.objects.order_by('-puntuacion_final')
    if len(mejores) > 60:
        mejores = mejores[:60]

    inscritos = Aspirante.objects.all()
    total_inscritos = inscritos.count()
    aprobados = Aspirante.objects.filter(puntuacion_final = 80)
    total_aprobados = aprobados.count()
    rechazados = Aspirante.objects.filter(puntuacion_final = 0)
    if len(mejores):
        maximo = mejores[0]
    else:
        maximo = "---"

    munis = [
        {'nombre': 'Santiago de Cali', 'cantidad': 0},
        {'nombre': 'Yumbo', 'cantidad': 0},
        {'nombre': 'Vijes', 'cantidad': 0},
        {'nombre': 'La Cumbre', 'cantidad': 0},
        {'nombre': 'Dagua', 'cantidad': 0},
        {'nombre': 'Otros', 'cantidad': 0}
    ]
    
    municipios = Aspirante.objects.values('municipio').annotate(dcount=Count('municipio_institucion'))
    for i in municipios:
        id_m = i['municipio']
        if id_m == 152: # cali
            posicion = 0;
        elif id_m == 1089: # yumbo
            posicion = 1;
        elif id_m == 1057: # vijes
            posicion = 2;
        elif id_m == 462: # cumbre
            posicion = 3;
        elif id_m == 279: # dagua
            posicion = 4;
        else:
            posicion = 5;

        munis[posicion]['cantidad'] = i['dcount']
        
    return render(request, 'dashboard/dashboard.html', {
        'mejores':mejores,

        'inscritos': inscritos,
        'aprobados': aprobados,
        'rechazados': rechazados,
        'total_inscritos':total_inscritos,
        'total_aprobados':total_aprobados,
        'total_rechazados':total_inscritos - total_aprobados,
        'maximo':maximo,

        'municipios':json.dumps(munis),
    })

def reporteME(request):
    estudiantes = Estudiante.objects.all()

    return render(request, 'dashboard/reporteME.html', {
        'estudiantes': estudiantes,

        #'municipios':json.dumps(munis),
    })

def tablero_control(request):
    return render(request, 'dashboard/tablero_control.html', {
    })
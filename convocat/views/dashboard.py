from django.shortcuts import redirect, render, render_to_response, get_list_or_404, get_object_or_404
from django.core import serializers
from django.http import HttpResponse
from convocat.models import * 
from django.db.models import Count, Q
from campus.models import Estudiante
from estudiante.models import InfoLaboral, FormacionAcademicaME, CertificacionTIC
from campus.views import user_group

import json


def dashboard(request):
    grupo = user_group(request)
    if grupo == None:
        return redirect('home')
    mejores = Aspirante.objects.order_by('-puntuacion_final')
    if len(mejores) > 60:
        mejores = mejores[:60]

    inscritos = Aspirante.objects.all()
    total_inscritos = inscritos.count()
    aprobados = Aspirante.objects.filter(Q(puntuacion_final__gte = 50) & ~Q(puntuacion_final= None))
    total_aprobados = aprobados.count()
    rechazados = Aspirante.objects.filter(puntuacion_final__lt = 50)
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

    munisAprobados = [
        {'nombre': 'Santiago de Cali', 'cantidad': 0},
        {'nombre': 'Yumbo', 'cantidad': 0},
        {'nombre': 'Vijes', 'cantidad': 0},
        {'nombre': 'La Cumbre', 'cantidad': 0},
        {'nombre': 'Dagua', 'cantidad': 0},
        {'nombre': 'Otros', 'cantidad': 0}
    ]

    munisRechazados = [
        {'nombre': 'Santiago de Cali', 'cantidad': 0},
        {'nombre': 'Yumbo', 'cantidad': 0},
        {'nombre': 'Vijes', 'cantidad': 0},
        {'nombre': 'La Cumbre', 'cantidad': 0},
        {'nombre': 'Dagua', 'cantidad': 0},
        {'nombre': 'Otros', 'cantidad': 0}
    ]
    
    municipios = Aspirante.objects.values('municipio', 'puntuacion_final').annotate(dcount=Count('municipio_institucion'))
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

        print "....................................."
        print i
        if i['puntuacion_final']>= 50:
            munisAprobados[posicion]['cantidad'] = i['dcount']
        else:
            munisRechazados[posicion]['cantidad'] = i['dcount']

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
        'user_group': user_group(request),
        'municipios':json.dumps(munis),
        'municipiosA':json.dumps(munisAprobados),
        'municipiosR':json.dumps(munisRechazados),
        'opcion_menu': 1
    })

def reporteME(request):
    grupo = user_group(request)
    if grupo == None:
        return redirect('home')
    estudiantes = []
    cont = 1
    students = Estudiante.objects.filter(acta_compromiso=True).select_related('estudiante.InfoLaboral__estudiante')
    for estudiante in students:
        estudiantes.append(
            {"id": estudiante.id, "item": cont, "nombre": estudiante, "institucion":InfoLaboral.objects.get(estudiante=estudiante).get_sede_display, "nivel":estudiante.get_nivel_educativo_display}
        )
        cont = cont + 1
    print "------------------"
    print type(user_group(request))
    return render(request, 'dashboard/reporteME.html', {
        'estudiantes': estudiantes,
        'user_group': user_group(request),
        'opcion_menu': 2
        #'municipios':json.dumps(munis),
    })
    
def obtener_estudiante(valor):
    try :
        miid, mihash = map(int,valor.split("-"))
        asp = Estudiante.objects.get(id=miid)

        if asp.numero_inscripcion()==valor:
            return asp
        else :
            return None
    except Exception as ex:
        return None
    
def impresionME(request, id_estudiante):
    try :
        estudiante = Estudiante.objects.get(id=id_estudiante)
        infoLaboral = InfoLaboral.objects.get(estudiante=estudiante)
        certificacionTIC = CertificacionTIC.objects.filter(estudiante=estudiante)
        formacionAcademicaME = FormacionAcademicaME.objects.filter(estudiante=estudiante)
        
        return render(request, 'dashboard/impresionME.html', {
			'estudiante' : estudiante,
			'infoLaboral' : infoLaboral,
			'formacionAcademicaME' : formacionAcademicaME,
			'certificacionTIC' : certificacionTIC
		})
    except Exception as ex:
        return redirect('reporteME')

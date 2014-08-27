from django.shortcuts import redirect, render, render_to_response, get_object_or_404
from django.core import serializers
from convocat.models import * 
from django.db.models import Count
import json


def dashboard(request):
    mejores = Aspirante.objects.order_by('-puntuacion_hv')
    if len(mejores) > 60:
        mejores = mejores[:60]

    total_inscritos = Aspirante.objects.count()
    total_aprobados = Aspirante.objects.filter(puntuacion_hv__gt= 50).count()
    maximo = mejores[0].puntuacion_hv

    munis = []
    municipios = Aspirante.objects.values('municipio').annotate(dcount=Count('municipio'))
    for i in municipios:
        nombre = unicode(Municipio.objects.get(id=i['municipio']).nombre)
        munis.append({'nombre': nombre, 'dcount': i['dcount']})
        
    return render(request, 'dashboard/dashboard.html', {
        'mejores':mejores,

        'inscritos':total_inscritos,
        'aprobados':total_aprobados,
        'rechazados':total_inscritos - total_aprobados,
        'maximo':maximo,

        'municipios':json.dumps(munis),
    })
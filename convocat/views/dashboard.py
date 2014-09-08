from django.shortcuts import redirect, render, render_to_response, get_list_or_404
from django.core import serializers
from convocat.models import * 
from django.db.models import Count
import json


def dashboard(request):
    mejores = Aspirante.objects.order_by('-puntuacion_final')
    if len(mejores) > 60:
        mejores = mejores[:60]

    inscritos = Aspirante.objects.all()
    total_inscritos = inscritos.count()
    aprobados = Aspirante.objects.filter(puntuacion_final__gte = 50)
    total_aprobados = aprobados.count()
    rechazados = Aspirante.objects.filter(puntuacion_final__lt = 50)
    if len(mejores):
        maximo = mejores[0].puntuacion_final
    else:
        maximo = "---"

    munis = []
    municipios = Aspirante.objects.values('municipio').annotate(dcount=Count('municipio_institucion'))
    for i in municipios:
        nombre = unicode(Municipio.objects.get(id=i['municipio']).nombre)
        munis.append({'nombre': nombre, 'dcount': i['dcount']})
        
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
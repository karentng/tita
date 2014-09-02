#encoding: utf-8
from django.shortcuts import redirect, render, render_to_response, get_object_or_404
from .models import EncuestaPadreFamilia
from .forms import *

def encuesta_padre(request):

    data = request.POST or None
    
    datosBasicosForm = DatosBasicosPadreForm(data)
    frecuenciaUsoForm = FrecuenciaUsoPadreForm(data)
    
    mejoraForms = []
    for mat in Materia.objects.all():
        f = MejoraMateriaPadreForm(initial={'materia':mat})
        mejoraForms.append(f)



    if request.method == 'POST':
        pass
    
        
    return render(request, 'encuesta_padre.html', {
        'datosBasicosForm': datosBasicosForm,
        'frecuenciaUsoForm': frecuenciaUsoForm,
        'mejoraFormset': MejorasMateriaFormset(MejoraMateriaPadreForm, data)
    }) 


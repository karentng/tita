#encoding: utf-8
from django.shortcuts import redirect, render, render_to_response, get_object_or_404
from .models import EncuestaPadreFamilia
from .forms import *

def encuesta_padre(request):

    data = request.POST or None
    
    form = EncuestaPadreForm(data)
    mejoraFormset = MejorasMateriaFormset(MejoraMateriaPadreForm, data)

    campos_basicos = ( form[x] for x in  ('jornada', 'nombre', 'parentesco', 'municipio_nacimiento', 'fecha_nacimiento', 'barrio', 'institucion', 'grado', 'nivel_educativo', 'titulo', 'ocupacion'))

    if request.method == 'POST':
        pass
    
        
    return render(request, 'encuesta_padre.html', {
        'form': form,
        'campos_basicos' : campos_basicos,
        'mejoraFormset': mejoraFormset,
    }) 


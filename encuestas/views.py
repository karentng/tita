#encoding: utf-8
from django.shortcuts import redirect, render, render_to_response, get_object_or_404
from .models import EncuestaPadreFamilia
from .forms import EncuestaPadreForm

def encuesta_padre(request):

    if request.method == 'POST':
        form = EncuestaPadreForm(request.POST)
    else:
        form = EncuestaPadreForm()
        
    return render(request, 'encuesta_padre.html', {
        'form': form,
    }) 


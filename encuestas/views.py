#encoding: utf-8
from django.shortcuts import redirect, render, render_to_response, get_object_or_404
from .models import EncuestaPadreFamilia

def encuesta_padre(request):
    return render(request, 'encuesta_padre.html') 


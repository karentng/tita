from django.shortcuts import render


# Create your views here.

def calificacion(request):
    return render(request, 'calificacion.html', {
    })

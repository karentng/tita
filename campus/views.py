from django.shortcuts import render, get_list_or_404, get_object_or_404
from campus.models import *


# Create your views here.

def listar_cursos_profesor(request):
    try:
        cursos = get_list_or_404(Curso, formador_id=request.user.formador.id)
    except Curso.DoesNotExist:
        raise Http404
    return render(request,'cursos.html', {
        'cursos':cursos
        })

def listar_clases_curso(request, curso_id):
    try:
        clases = get_list_or_404(Clase, curso_id=curso_id)
        curso = get_object_or_404(Curso, id=curso_id)
    except Clase.DoesNotExist:
        raise Http404
    return render(request,'clases.html', {
        'clases':clases,
        'curso':curso
        })


def listado_estudiantes(request, curso_id, clase_id):
    try:
        curso = get_object_or_404(Curso, id=curso_id)
        clase = get_object_or_404(Clase, id=clase_id)
    except Clase.DoesNotExist:
        raise Http404
    return render(request, 'calificar.html', {
        'clase':clase,
        'curso': curso
    })






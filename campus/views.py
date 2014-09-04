from django.shortcuts import render, get_list_or_404, get_object_or_404
from campus.models import *
from campus.forms import AsistenciaForm, ActividadForm

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


def asistencia(request, curso_id, clase_id):
    curso = get_object_or_404(Curso, id=curso_id)
    clase = get_object_or_404(Clase, id=clase_id)

    form = AsistenciaForm(request.POST or None, instance=clase)

    return render(request, 'asistencia.html', {
        'clase':clase,
        'curso': curso,
        'form': form,
    })


def calificar_actividades(request, curso_id, clase_id):
    clase = get_object_or_404(Clase, id=clase_id)

    actividad_form = ActividadForm()

    if request.method=="POST":
        accion = request.POST['accion']
        if accion=='crear_actividad':
            actividad_form = ActividadForm(request.POST)
            if actividad_form.is_valid():
                actividad = actividad_form.save(commit=False)
                actividad.clase_id = clase_id
                actividad.save()
        else :
            pass

    

    return render(request, 'calificar_actividades.html', {
        'clase' : clase,
        'actividad_form' : actividad_form,
        #'curso' : curso,
    })



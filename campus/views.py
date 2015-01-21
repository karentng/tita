#encoding: utf-8
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from campus.models import *
from campus.forms import AsistenciaForm, SoportesFormset, ActividadForm

'''Función que me retorna una lista con las opciones de menu necesarias, da por sentado que cada usuario pertenece solo a un grupo'''
def user_group(request):
    if request.user.is_authenticated():
        grupo = request.user.groups.all()
        if len(grupo) > 0:
            return grupo[0].name
        else:
            None
    else:
        return None

''' Función que me envia a la página correspondiente de acuerdo al perfil de la persona logueada '''
def logged_user(request):
    grupo = user_group(request)
    if grupo == None:
        return redirect('home')
    elif grupo == 'Coordinador':
        return redirect('resumen_proyecto')
    elif grupo == 'Formador':
        return redirect('cronograma_diplomado')
    elif grupo == 'Operario_malla':
        return redirect('listar_contratistas')
    elif grupo == 'Contratista_malla':
        return redirect('lista_contratista')
    elif grupo == 'Secretaria':
        return redirect('resumen_proyecto')
    elif grupo == 'Tablero de control publico':
        return redirect('resumen_proyecto')
    elif grupo.startswith( 'Editar_Actividad' ):
        grupo_edicion_actividad = grupo.split('_');
        return redirect('tablero_control/' + grupo_edicion_actividad[2])

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
    curso = get_object_or_404(Cursos, id=curso_id)
    clase = get_object_or_404(Clases, id=clase_id)

    if request.method=='POST':
        form = AsistenciaForm(request.POST, instance=clase)
        #soportesFormset = SoportesFormset(request.POST, request.FILES, instance=clase)
        #advertencia: no trate de copiar este codigo, trabaja de manera inusual
        if form.is_valid() :
            form.save()
        #if soportesFormset.is_valid() :
            #result = soportesFormset.save()
            #print "result=",result

        #print "valido1=", form.is_valid(), "valido2=", soportesFormset.is_valid()

        #if form.is_valid() and soportesFormset.is_valid():
            #return redirect('asistencia', curso_id, clase_id)
            return redirect('home')


    else :
        form = AsistenciaForm(instance=clase)
        #soportesFormset = SoportesFormset(instance=clase)

    return render(request, 'asistencia.html', {
        'clase':clase,
        'curso': curso,
        'form': form,
        #'soportesFormset' : soportesFormset,
    })
'''
def actividades(request, curso_id, clase_id):
    curso = get_object_or_404(Cursos, id=curso_id)
    clase = get_object_or_404(Clases, id=clase_id)

<<<<<<< HEAD
    grupo = user_group(request)
    if grupo == None:
        return redirect('home')
=======
    if request.method=='POST':
        form = ActividadForm(request.POST, instance=clase)
        #soportesFormset = SoportesFormset(request.POST, request.FILES, instance=clase)
        #advertencia: no trate de copiar este codigo, trabaja de manera inusual
        if form.is_valid() :
            form.save()
        #if soportesFormset.is_valid() :
            #result = soportesFormset.save()
            #print "result=",result

        #print "valido1=", form.is_valid(), "valido2=", soportesFormset.is_valid()
>>>>>>> 6046c5ec159e61d1d7f631f5d74718878928761b

    if request.method == 'POST':

        form = ActividadForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.clase = clase
            obj.save()

            return redirect('cronograma_diplomado')

    else:


        form = ActividadForm()

    return render(request, 'calificar_actividades.html', {
        'clase':clase,
        'curso': curso,
        'form': form,
        #'soportesFormset' : soportesFormset,
    })
'''

def calificar_actividades(request, curso_id, clase_id):
    clase = get_object_or_404(Clase, id=clase_id)

    actividad_form = ActividadForm()

    if request.method=="POST":
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



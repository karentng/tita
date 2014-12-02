from django.shortcuts import redirect, render, render_to_response, get_list_or_404, get_object_or_404
from django.core import serializers
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, QueryDict
from convocat.models import *
from convocat.forms import *
from django.db.models import Count, Q
from campus.models import Estudiante
from estudiante.models import InfoLaboral, FormacionAcademicaME, CertificacionTIC
from campus.views import user_group


import json, datetime

def retornar_datos_reporte_convocatoria_1():
    mejores = Aspirante.objects.order_by('-puntuacion_hv')
    if len(mejores) > 60:
        mejores = mejores[:60]

    inscritos = Aspirante.objects.all()
    total_inscritos = inscritos.count()
    aprobados = Aspirante.objects.filter(Q(puntuacion_final__gte = 99) & ~Q(puntuacion_final= None))
    total_aprobados = aprobados.count()
    rechazados = Aspirante.objects.filter(puntuacion_final__lt = 1)
    if len(mejores):
        maximo = mejores[0]
    else:
        maximo = "---"

    munis = [
        {'nombre': 'Santiago de Cali', 'cantidad': 0},
        {'nombre': 'Yumbo', 'cantidad': 0},
        {'nombre': 'Vijes', 'cantidad': 0},
        {'nombre': 'La Cumbre', 'cantidad': 0},
        {'nombre': 'Dagua', 'cantidad': 0},
        {'nombre': 'Otros', 'cantidad': 0}
    ]

    munisAprobados = [
        {'nombre': 'Santiago de Cali', 'cantidad': 0},
        {'nombre': 'Yumbo', 'cantidad': 0},
        {'nombre': 'Vijes', 'cantidad': 0},
        {'nombre': 'La Cumbre', 'cantidad': 0},
        {'nombre': 'Dagua', 'cantidad': 0},
        {'nombre': 'Otros', 'cantidad': 0}
    ]

    municipios = Aspirante.objects.values('municipio_institucion', 'puntuacion_final').annotate(dcount=Count('municipio_institucion'))
    for i in municipios:
        id_m = i['municipio_institucion']
        if id_m == 152: # cali
            posicion = 0;
        elif id_m == 1089: # yumbo
            posicion = 1;
        elif id_m == 1057: # vijes
            posicion = 2;
        elif id_m == 462: # cumbre
            posicion = 3;
        elif id_m == 279: # dagua
            posicion = 4;
        else:
            posicion = 5;

        if i['puntuacion_final']>= 99:
            munisAprobados[posicion]['cantidad'] = i['dcount']

        munis[posicion]['cantidad'] = i['dcount']

    return {
        'mejores':mejores,

        'inscritos': inscritos,
        'aprobados': aprobados,
        'rechazados': rechazados,
        'total_inscritos':total_inscritos,
        'total_aprobados':total_aprobados,
        'total_rechazados':total_inscritos - total_aprobados,
        'maximo':maximo,
        'municipios':json.dumps(munis),
        'municipiosA':json.dumps(munisAprobados),
        'opcion_menu': 1
    }

def dashboard(request):
    grupo = user_group(request)
    if grupo == None:
        return redirect('home')

    datos_convocatoria_1 = retornar_datos_reporte_convocatoria_1()
    datos_convocatoria_1['user_group'] = user_group(request)

    return render(request, 'dashboard/dashboard.html', datos_convocatoria_1)

def listaMaestrosEstudiantesInscritos():
    estudiantes = []
    cont = 1
    students = Estudiante.objects.filter(acta_compromiso=True).select_related('estudiante.InfoLaboral__estudiante')
    for estudiante in students:
        jornada = ""
        institucion = ""
        try:
            il = InfoLaboral.objects.get(estudiante=estudiante)
            try:
                jornada = il.get_jornada_display
            except Exception:
                jornada = "---"
            try:
                institucion = il.get_sede_display
            except Exception:
                institucion = "---"
        except Exception:
            jornada = "---"
            institucion = "---"
        estudiantes.append(
            {"id": estudiante.id,
            "item": cont,
            "nombre": estudiante,
            "cedula": estudiante.numero_documento,
            "jornada": jornada,
            "institucion": institucion,
            }
        )
        cont = cont + 1

    return estudiantes

def reporteME(request):
    grupo = user_group(request)
    if grupo == None:
        return redirect('home')
    estudiantes = listaMaestrosEstudiantesInscritos()
    print "------------------"
    print type(user_group(request))

    return render(request, 'dashboard/reporteME.html', {
        'estudiantes': estudiantes,
        'user_group': user_group(request),
        'opcion_menu': 2
    })

def obtener_estudiante(valor):
    try :
        miid, mihash = map(int,valor.split("-"))
        asp = Estudiante.objects.get(id=miid)

        if asp.numero_inscripcion()==valor:
            return asp
        else :
            return None
    except Exception as ex:
        return None

def impresionME(request, id_estudiante):
    try :
        estudiante = Estudiante.objects.get(id=id_estudiante)
        infoLaboral = InfoLaboral.objects.filter(estudiante=estudiante)
        print(infoLaboral)
        if len(infoLaboral) > 0:
            infoLaboral = infoLaboral[0]
        certificacionTIC = CertificacionTIC.objects.filter(estudiante=estudiante)
        formacionAcademicaME = FormacionAcademicaME.objects.filter(estudiante=estudiante)

        return render(request, 'dashboard/impresionME.html', {
			'estudiante' : estudiante,
			'infoLaboral' : infoLaboral,
			'formacionAcademicaME' : formacionAcademicaME,
			'certificacionTIC' : certificacionTIC
		})
    except Exception as ex:
        print(ex)
        return redirect('reporteME')

def actividades(request, id_actividad):
    if id_actividad=='':
        id_actividad=1

    actividad = Actividad.objects.get(id=id_actividad)
    concepto = Concepto.objects.get(id=1)
    request.session['actividad_tablero_control']=id_actividad
    print(actividad)
    print(concepto)

    concepto_por_actividad = ConceptoPorActividad.objects.get(actividad=actividad, concepto=concepto)
    print(concepto_por_actividad)

    return render(request, 'dashboard/actividades.html', {
        'concepto_por_actividad' : concepto_por_actividad,
        'actividad' : actividad,
        'formArchivo': ArchivoForm(),
        'formGrupo': GrupoForm()
    })

def validar_grupo_coordinador_secretaria(request):
    grupo = user_group(request)
    if grupo == 'Coordinador' or grupo == 'Secretaria' or grupo == 'Tablero de control publico':
        return True
    else:
        return False

def tablero_control(request, id_actividad):
    if validar_grupo_coordinador_secretaria(request) == False:
        return redirect('home')

    if id_actividad=='':
        id_actividad=1

    request.session['actividad_tablero_control'] = id_actividad

    actividad_seleccionada = Actividad.objects.get(id=id_actividad)
    actividades = Actividad.objects.all().order_by('id')

    estado_de_avance = EstadoDeAvance.objects.filter(actividad=actividad_seleccionada)

    if len(estado_de_avance) > 0:
        estado_de_avance = estado_de_avance.latest('id')

    nuevo_estado_de_avance = estado_de_avance.__dict__.copy()
    nuevo_estado_de_avance['fecha'] = datetime.datetime.now()

    grupo_de_usuario = user_group(request)
    print(grupo_de_usuario)
    usuario_puede_editar = False

    usuario_puede_editar = ((grupo_de_usuario == 'Coordinador' and int(id_actividad) < 14) or (grupo_de_usuario == 'Secretaria' and int(id_actividad) > 13))

    estudiantes = Estudiante.objects.all()
    #estudiantesPaginator = Paginator(estudiantes, 5)

    datos_tablero_control = {
        'actividades' : actividades,
        'estudiantes' : estudiantes,#estudiantesPaginator.page(1),
        'actividad_seleccionada' : actividad_seleccionada,
        'estado_de_avance' : estado_de_avance,
        'estado_avance_form' : EstadoDeAvanceForm(initial=nuevo_estado_de_avance),
        'formArchivo': ArchivoForm(),
        'formGrupo': GrupoForm(),
        'usuario_puede_editar': usuario_puede_editar,
        'user_group': user_group(request),
    }

    datos_tablero_control.update(retornar_datos_reporte_convocatoria_1())

    return render(request, 'dashboard/tablero_control.html', datos_tablero_control)

def guardarArchivo(request):
    if validar_grupo_coordinador_secretaria(request) == False:
        return redirect('home')

    form = ArchivoForm(request.POST, request.FILES)
    if form.is_valid():
        archivo = form.save(commit=False)
        archivo.usuario = request.user
        archivo.save()

    return HttpResponseRedirect(str(request.session['actividad_tablero_control']))

def guardarEstadoDeAvance(request):
    if validar_grupo_coordinador_secretaria(request) == False:
        return redirect('home')

    actividad = Actividad.objects.get(id=request.session['actividad_tablero_control'])
    print(actividad)
    form = EstadoDeAvanceForm(request.POST)
    if form.is_valid():
        estado_de_avance = form.save(commit=False)
        estado_de_avance.actividad = actividad
        estado_de_avance.usuario = request.user
        estado_de_avance.save()

    return HttpResponseRedirect( str(request.session['actividad_tablero_control']))

def eliminarGrupo(request, id_grupo):
    if validar_grupo_coordinador_secretaria(request) == False:
        return redirect('home')

    grupo = Grupo.objects.get(id=id_grupo)
    grupo.activo = False
    grupo.save()

    return HttpResponseRedirect( '../' + str(request.session['actividad_tablero_control']))

def eliminarArchivo(request, id_archivo):
    if validar_grupo_coordinador_secretaria(request) == False:
        return redirect('home')

    archivo = Archivo.objects.get(id=id_archivo)
    archivo.activo = False
    archivo.save()
    historico_de_archivo = HistoricoDeArchivo()
    historico_de_archivo.archivo = archivo
    historico_de_archivo.usuario = request.user
    historico_de_archivo.save()

    return HttpResponseRedirect( '../' + str(request.session['actividad_tablero_control']))

def guardarGrupo(request, id_concepto_por_actividad):
    if validar_grupo_coordinador_secretaria(request) == False:
        return redirect('home')

    form = GrupoForm(request.POST, request.FILES)
    concepto_por_actividad = ConceptoPorActividad.objects.get(id=id_concepto_por_actividad)

    if form.is_valid():
        grupo = form.save(commit=False)
        grupo.concepto_por_actividad = concepto_por_actividad
        grupo.usuario = request.user
        grupo.save()

    return HttpResponseRedirect( '../' + str(request.session['actividad_tablero_control']))

def obtenerGruposPorConceptoActividad(request, id_concepto_por_actividad):
    if validar_grupo_coordinador_secretaria(request) == False:
        return redirect('home')

    concepto_por_actividad = ConceptoPorActividad.objects.get(id=id_concepto_por_actividad)
    grupos = Grupo.objects.filter(concepto_por_actividad=concepto_por_actividad)

    out = []
    out.append('<option selected="selected" value="">---------</option>')

    for grupo in grupos:
        out.append("<option value='" + str(grupo.id) + "'>" + str(grupo) + "</option>")

    return HttpResponse(' '.join(out))


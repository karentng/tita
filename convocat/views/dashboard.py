# -*- coding: utf-8 -*-

from django.shortcuts import redirect, render, render_to_response, get_list_or_404, get_object_or_404
from django.core import serializers
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, QueryDict
from convocat.models import *
from convocat2.models import Aspirante as Aspirante2
from convocat.forms import *
from django.db.models import Count, Q
from campus.models import Estudiante, Cursos, Clases, SoporteClases
from estudiante.models import InfoLaboral, FormacionAcademicaME, CertificacionTIC
from campus.views import user_group, user_groups

import json, datetime, xlwt

def retornar_datos_reporte_convocatoria_1():
    mejores = Aspirante.objects.order_by('-puntuacion_hv')
    if len(mejores) > 60:
        mejores = mejores[:60]

    inscritos = Aspirante.objects.all()
    total_inscritos = inscritos.count()
    aprobados = Aspirante.objects.filter(Q(puntuacion_final = 100) & ~Q(puntuacion_final= None))
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

def buscarEstudiante(lista, estudiante):
    for i in lista:
        if i == estudiante:
            return True
    return False

def listaMaestrosEstudiantesInscritos(cohorte):
    estudiantes = []
    cont = 1
    #students = Estudiante.objects.filter(acta_compromiso=True).select_related('estudiante.InfoLaboral__estudiante').select_related('Cursos__estudiantes')
    students = Estudiante.objects.filter(cohorte=cohorte, acta_compromiso=True).select_related('estudiante.InfoLaboral__estudiante').select_related('Cursos__estudiantes')
    c = 0
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

        try:

            curso = Cursos.objects.filter(estudiantes=estudiante)
            clases = Clases.objects.filter(asistentes=estudiante, curso=curso)
            horas = 0

            sesionesProgramadas = clases.count()
            sesionesConSoporte = 0
            horasAsistidasConSoporte = 0
            horasAsistidasSinSoporte = 0

            for clase in clases:
                asistioAClase = buscarEstudiante(clase.asistentes.all(), estudiante)

                try:
                    SoporteClases.objects.get(clase=clase)
                    sesionesConSoporte += 1
                    horas = horas + 5
                    if asistioAClase == True: # Asistio a la clase
                        horasAsistidasConSoporte += 5 # Son horas
                except Exception:
                    if asistioAClase == True: # Asistio a la clase
                        horasAsistidasSinSoporte += 5 # Son horas
                    
        except Exception:
            curso = "---"
            horas = "---"
            sesionesProgramadas = "---"
            sesionesConSoporte = "---"
            horasAsistidasConSoporte = "---"
            horasAsistidasSinSoporte = "---"

        try:
            curso = curso[0].descripcion
        except Exception:
            curso = "---"

        estudiantes.append(
            {"id": estudiante.id,
            "item": cont,
            "nombre": estudiante,
            "cedula": estudiante.numero_documento,
            "jornada": jornada,
            "institucion": institucion,
            "curso": curso,
            "horas": horas,

            "sesionesProgramadas": sesionesProgramadas,
            "sesionesConSoporte": sesionesConSoporte,
            "horasAsistidasConSoporte": horasAsistidasConSoporte,
            "horasAsistidasSinSoporte": horasAsistidasSinSoporte,
            }
        )
        cont = cont + 1
    return estudiantes

def reporteME(request, cohorte=None):
    valor = request.session.get('cohorte_me')
    if valor:
        cohorte = valor
        del request.session['cohorte_me']
    elif cohorte:
        request.session['cohorte_me'] = cohorte
        return redirect('reporteME')
    else:
        cohorte = 1 # valor por defecto

    grupo = user_group(request)
    if grupo == None:
        return redirect('home')
    estudiantes = listaMaestrosEstudiantesInscritos(cohorte)

    return render(request, 'dashboard/reporteME.html', {
        'estudiantes': estudiantes,
        'user_group': user_group(request),
        'opcion_menu': 2,
        'cohorte': cohorte
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

    concepto_por_actividad = ConceptoPorActividad.objects.get(actividad=actividad, concepto=concepto)

    return render(request, 'dashboard/actividades.html', {
        'concepto_por_actividad' : concepto_por_actividad,
        'actividad' : actividad,
        'formArchivo': ArchivoForm(),
        'formGrupo': GrupoForm()
    })

def validar_grupo_coordinador_secretaria(request):
    grupo = user_group(request)
    if grupo == 'Coordinador' or grupo == 'Secretaria' or grupo == 'Tablero de control publico' or grupo.startswith( 'Editar_Actividad' ) or grupo.startswith( 'Lectura_Actividad' ):
        return True
    else:
        return False

def acta_seguimiento(request):
    acta_seguimiento_all = ActaDeSeguimiento.objects.filter(activo=True).order_by('-id')

    grupo_de_usuario = user_group(request)
    usuario_puede_editar = grupo_de_usuario == 'Secretaria' or 'Coordinador'

    return render(request, 'dashboard/acta_seguimiento.html', {
        'acta_seguimiento_all' : acta_seguimiento_all,
        'actaDeSeguimientoForm' : ActaDeSeguimientoForm(),
        'opcion_menu' : 24,
        'user_group': user_group(request),
        'usuario_puede_editar' : usuario_puede_editar,
        'form_edit': None,
        'id_acta': None
    })

def editarActaSeguimiento(request, id_acta):
    acta_seguimiento = ActaDeSeguimiento.objects.get(id=id_acta);

    form_edit = ActaDeSeguimientoForm(instance=acta_seguimiento)

    return render(request, 'dashboard/acta_seguimiento.html', {
        'acta_seguimiento_all' : None,
        'actaDeSeguimientoForm' : None,
        'opcion_menu' : 24,
        'user_group': user_group(request),
        'usuario_puede_editar' : None,
        'form_edit': form_edit,
        'id_acta':id_acta
    })

def guardarActaSeguimiento(request, id_acta):
    if validar_grupo_coordinador_secretaria(request) == False:
        return redirect('home')

    if id_acta:
        acta_seguimiento = ActaDeSeguimiento.objects.get(id=id_acta);
        form = ActaDeSeguimientoForm(request.POST, request.FILES, instance=acta_seguimiento)
    else:
        form = ActaDeSeguimientoForm(request.POST, request.FILES)

    if form.is_valid():
        actaSeguimiento = form.save(commit=False)
        actaSeguimiento.usuario = request.user
        actaSeguimiento.save()
        return redirect('acta_seguimiento')
    else:
        return redirect('home')

def eliminarActaSeguimiento(request, id_acta):
    if validar_grupo_coordinador_secretaria(request) == False:
        return redirect('home')

    actaDeSeguimiento = ActaDeSeguimiento.objects.get(id=id_acta)
    actaDeSeguimiento.activo = False
    actaDeSeguimiento.save()

    historicoActaDeSeguimiento = HistoricoActaDeSeguimiento()
    historicoActaDeSeguimiento.usuario = request.user
    historicoActaDeSeguimiento.fecha = datetime.datetime.now()
    historicoActaDeSeguimiento.actaDeSeguimiento = actaDeSeguimiento
    historicoActaDeSeguimiento.observacion = request.POST.get("observacion")
    historicoActaDeSeguimiento.save()

    return redirect('acta_seguimiento')

def resumen_proyecto(request):
    resumen_proyecto_all = ResumenProyecto.objects.filter().order_by('-fecha')

    if len(resumen_proyecto_all) > 0:
        resumen_proyecto = resumen_proyecto_all.latest('id')
        nuevo_resumen_proyecto = resumen_proyecto.__dict__.copy()
    else:
        resumen_proyecto = ResumenProyecto()
        resumen_proyecto.fecha = None
        nuevo_resumen_proyecto = ResumenProyecto().__dict__.copy()

    nuevo_resumen_proyecto['fecha'] = datetime.datetime.now()

    grupo_de_usuario = user_group(request)
    usuario_puede_editar = grupo_de_usuario == 'Secretaria'

    return render(request, 'dashboard/resumen_proyecto.html', {
        'form_editable' : False,
        'resumen_proyecto' : resumen_proyecto,
        'nuevo_resumen_proyecto' : nuevo_resumen_proyecto,
        'resumen_proyecto_all' : resumen_proyecto_all,
        'resumenProyectoForm' : ResumenProyectoForm(),
        'opcion_menu' : 23,
        'user_group': user_group(request),
        'usuario_puede_editar' : usuario_puede_editar
    })

def guardarResumenProyecto(request):
    if validar_grupo_coordinador_secretaria(request) == False:
        return redirect('home')

    form = ResumenProyectoForm(request.POST)
    if form.is_valid():
        resumenProyecto = form.save(commit=False)
        resumenProyecto.usuario = request.user
        resumenProyecto.save()
        return redirect('resumen_proyecto')
    else:
        return redirect('home')

def tablero_control(request, id_actividad):
    if validar_grupo_coordinador_secretaria(request) == False:
        return redirect('home')

    if id_actividad=='':
        id_actividad='1'

    request.session['actividad_tablero_control'] = id_actividad

    actividad_seleccionada = Actividad.objects.get(id=id_actividad)
    actividades = Actividad.objects.all().order_by('id')

    estado_de_avance = EstadoDeAvance.objects.filter(actividad=actividad_seleccionada)

    if len(estado_de_avance) > 0:
        estado_de_avance = estado_de_avance.latest('id')

    nuevo_estado_de_avance = estado_de_avance.__dict__.copy()
    nuevo_estado_de_avance['fecha'] = datetime.datetime.now()

    grupo_de_usuario = user_group(request)
    grupos_de_usuario = user_groups(request)
    actividades_permitidas = []

    for grupo in grupos_de_usuario:
        if grupo.startswith( 'Editar_Actividad' ) or grupo.startswith( 'Lectura_Actividad' ):
            grupo_acceso_actividad = grupo.split('_');
            actividades_permitidas.append(grupo_acceso_actividad[2])

    print actividades_permitidas

    usuario_puede_editar_actividad = 'Editar_Actividad_' + id_actividad in grupos_de_usuario

    usuario_puede_editar = ((grupo_de_usuario == 'Coordinador' and int(id_actividad) < 14) or (grupo_de_usuario == 'Secretaria') or usuario_puede_editar_actividad)

    estudiantesMulti = Estudiante.objects.filter(acta_compromiso=True, cohorte=1).select_related('estudiante.InfoLaboral__estudiante').select_related('Cursos__estudiantes') if id_actividad == '4' else []
    estudiantesMulti2 = Estudiante.objects.filter(acta_compromiso=True, cohorte=2).select_related('estudiante.InfoLaboral__estudiante').select_related('Cursos__estudiantes') if id_actividad == '4' else []
    aspirantesMulti = Aspirante.objects.all() if id_actividad == '1' else []
    aspirantesMulti2 = Aspirante2.objects.all() if id_actividad == '1' else []
    variablesPorSede = VariablePorSede.objects.all() if id_actividad == '15' else []
    variablesPorAula = VariablePorAula.objects.all() if id_actividad == '15' else []
    estudiantes = listaMaestrosEstudiantesInscritos(1) if id_actividad == '4' else []

    datos_tablero_control = {
        'actividades_permitidas' : actividades_permitidas,
        'actividades' : actividades,
        'estudiantes' : estudiantes,
        'estudiantesMulti' : estudiantesMulti,
        'estudiantesMulti2' : estudiantesMulti2,
        'aspirantesMulti' : aspirantesMulti,
        'aspirantesMulti2' : aspirantesMulti2,
        'variablesPorSede' : variablesPorSede,
        'variablesPorAula' : variablesPorAula,
        'actividad_seleccionada' : actividad_seleccionada,
        'estado_de_avance' : estado_de_avance,
        'estado_avance_form' : EstadoDeAvanceForm(initial=nuevo_estado_de_avance),
        'formArchivo': ArchivoForm(),
        'formGrupo': GrupoForm(),
        'formVariablesPorAula' : VariablePorAulaForm(),
        'formVariablesPorSede' : VariablePorSedeForm(),
        'usuario_puede_editar': usuario_puede_editar,
        'user_group': user_group(request),
        'usuario_puede_editar_actividad': usuario_puede_editar_actividad
    }

    datos_tablero_control.update(retornar_datos_reporte_convocatoria_1())
    datos_tablero_control['opcion_menu'] = 13

    return render(request, 'dashboard/tablero_control.html', datos_tablero_control)

def guardarVariablesPorSede(request):
    if validar_grupo_coordinador_secretaria(request) == False:
        return redirect('home')

    form = VariablePorSedeForm(request.POST, request.FILES)
    if form.is_valid():
        variablePorSede = form.save(commit=False)
        variablePorSede.usuario = request.user
        variablePorSede.save()

    return HttpResponseRedirect(str(request.session['actividad_tablero_control']))

def guardarVariablesPorAula(request):
    if validar_grupo_coordinador_secretaria(request) == False:
        return redirect('home')

    form = VariablePorAulaForm(request.POST, request.FILES)
    if form.is_valid():
        variablePorAula = form.save(commit=False)
        variablePorAula.usuario = request.user
        variablePorAula.save()

    return HttpResponseRedirect(str(request.session['actividad_tablero_control']))

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
    historico_de_archivo.observacion = request.POST.get("observacion")
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
    grupos = Grupo.objects.filter(concepto_por_actividad=concepto_por_actividad, activo=True)

    out = []
    out.append('<option selected="selected" value="">---------</option>')

    for grupo in grupos:
        out.append("<option value='" + str(grupo.id) + "'>" + str(grupo) + "</option>")

    return HttpResponse(' '.join(out))

def descarga_convocatoria_xls(request, convocatoria):
    response = HttpResponse(mimetype='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=convocatoria_' + convocatoria + '.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet("Hoja1")

    row_num = 0

    columns = [
        (u"Nombres y Apellidos", 4000),
        (u"Cédula", 4000),
        (u"Genero", 4000),
        (u"Nacionalidad", 4000),
        (u"Fecha de Nacimiento", 4000),
        (u"Municipio de Nacimiento", 4000),
        (u"Dirección", 4000),
        (u"Municipio", 4000),
        (u"Teléfono", 4000),
        (u"Celular", 4000),
        (u"Email", 4000),
        (u"Aceptado", 4000),
        (u"Institucion Actual", 4000),
        (u"Municipio Institución", 4000),
        (u"Jornada", 4000),
        (u"Conocimiento y manejo de herramientas ofimáticas", 4000),
        (u"Conocimiento y manejo de herramientas  Web 2", 4000),
        (u"Conocimiento herramientas de edición multimedia", 4000),
        (u"Experiencia en desarrollo de contenidos educativos digitales", 4000),
        (u"Experiencia en desarrollo de libros de texto digital", 4000),
        (u"Experiencia en procesos de e-learning", 4000),
        (u"Experiencia en gestión de proyectos educativos TIC", 4000),
        (u"Experiencia en desarrollo de elementos de evaluación de competencias", 4000),
    ]

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    for col_num in xrange(len(columns)):
        ws.write(row_num, col_num, columns[col_num][0], font_style)
        ws.col(col_num).width = columns[col_num][1]

    font_style = xlwt.XFStyle()
    font_style.alignment.wrap = 1

    maestros_aspirantes = Aspirante.objects.all() if convocatoria == '1' else Aspirante2.objects.all()

    for obj in maestros_aspirantes:
        row_num += 1

        conocimientosEspecificos = ConocimientosEspecificos.objects.filter(aspirante=obj)

        if(conocimientosEspecificos.count() > 0):
            conocimientosEspecificos = conocimientosEspecificos.latest('id')

        row = [
            obj.nombreCompleto().upper(),
            obj.numero_documento,
            obj.get_sexo_display(),
            obj.nacionalidad.capitalize(),
            obj.fecha_nacimiento,
            obj.municipio_nacimiento.nombre if obj.municipio_nacimiento != None else '-',
            obj.direccion,
            obj.municipio.nombre  if obj.municipio != None else '-',
            obj.telefono,
            obj.celular,
            obj.email,
            'SI' if obj.puntuacion_final == 100 else 'NO',
            obj.institucion_actual,
            obj.municipio_institucion.nombre if obj.municipio_institucion != None else '-',
            obj.get_jornada_display(),
            conocimientosEspecificos.get_conocimiento1_display() if hasattr(conocimientosEspecificos, 'get_conocimiento1_display') else '-',
            conocimientosEspecificos.get_conocimiento2_display() if hasattr(conocimientosEspecificos, 'get_conocimiento2_display') else '-',
            conocimientosEspecificos.get_conocimiento3_display() if hasattr(conocimientosEspecificos, 'get_conocimiento3_display') else '-',
            conocimientosEspecificos.get_conocimiento4_display() if hasattr(conocimientosEspecificos, 'get_conocimiento4_display') else '-',
            conocimientosEspecificos.get_conocimiento5_display() if hasattr(conocimientosEspecificos, 'get_conocimiento5_display') else '-',
            conocimientosEspecificos.get_conocimiento6_display() if hasattr(conocimientosEspecificos, 'get_conocimiento6_display') else '-',
            conocimientosEspecificos.get_conocimiento7_display() if hasattr(conocimientosEspecificos, 'get_conocimiento7_display') else '-',
            conocimientosEspecificos.get_conocimiento8_display() if hasattr(conocimientosEspecificos, 'get_conocimiento8_display') else '-',

        ]
        for col_num in xrange(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

def descarga_cohorte_xls(request, cohorte):
    response = HttpResponse(mimetype='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=cohorte_' + cohorte + '.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet("Hoja1")

    row_num = 0

    columns = [
        (u"Nombres y Apellidos", 4000),
        (u"Cédula", 4000),
        (u"Institución Educativa", 4000),
        (u"Jornada", 4000),
        (u"Genero", 4000),
        (u"Email", 4000),
        (u"Email institucional", 4000),
        (u"Municipio de residencia", 4000),
        (u"Dirección", 4000),
        (u"Teléfono fijo", 4000),
        (u"Número de celular", 4000),
        (u"Último nivel educativo aprobado", 4000),
        (u"Secretaria educacion", 4000),
        (u"Sede", 4000),
        (u"Cargo", 4000),
        (u"Zona", 4000),
        (u"Decreto profesional docente", 4000),
        (u"Grados", 4000),
        (u"Poblacion étnica que atiende", 4000),
        (u"Tipo de nombramiento", 4000),
        (u"Tipo etnoeducador", 4000),
        (u"Asignaturas", 4000),
    ]

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    for col_num in xrange(len(columns)):
        ws.write(row_num, col_num, columns[col_num][0], font_style)
        ws.col(col_num).width = columns[col_num][1]

    font_style = xlwt.XFStyle()
    font_style.alignment.wrap = 1

    maestros_estudiantes = Estudiante.objects.filter(acta_compromiso=True, cohorte=1).select_related('estudiante.InfoLaboral__estudiante').select_related('Cursos__estudiantes') if cohorte == '1' else Estudiante.objects.filter(acta_compromiso=True, cohorte=2).select_related('estudiante.InfoLaboral__estudiante').select_related('Cursos__estudiantes')

    for obj in maestros_estudiantes:
        row_num += 1

        infoLaboral = InfoLaboral.objects.filter(estudiante=obj)
        grados = ''
        asignaturas = ''

        if(infoLaboral.count() > 0):
            infoLaboral = infoLaboral.latest('id')


        for grado in infoLaboral.grados.all():
            grados += grado.nombre + '. '

        for asignatura in infoLaboral.asignaturas.all():
            asignaturas += asignatura.nombre + '. '

        row = [
            obj.nombre_completo().upper(),
            obj.numero_documento,
            infoLaboral.get_sede_display(),
            infoLaboral.get_jornada_display(),
            obj.get_sexo_display(),
            obj.email,
            obj.email_institucional,
            obj.municipio.nombre,
            obj.direccion,
            obj.telefono,
            obj.celular,
            obj.get_nivel_educativo_display(),
            infoLaboral.secretaria_educacion.nombre,
            infoLaboral.get_sede_display(),
            infoLaboral.get_cargo_display(),
            infoLaboral.get_zona_display(),
            infoLaboral.get_decreto_docente_display(),
            grados,
            infoLaboral.poblacion_etnica,
            infoLaboral.get_nombramiento_display(),
            infoLaboral.get_tipo_etnoeducador_display(),
            asignaturas
        ]
        for col_num in xrange(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

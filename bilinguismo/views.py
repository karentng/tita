#encoding: utf-8
from django.shortcuts import redirect, render, render_to_response, get_object_or_404
from bilinguismo.models import * 
from bilinguismo.forms import *
from estudiante.forms import ContinuarRegistroFormDE
from campus.views import user_group

def buscar_bilinguismo_por_clave(valor):
    try :
        miid, mihash = map(int,valor.split("-"))
        asp = Bilinguismo.objects.get(id=miid)
        if asp.numero_inscripcion()==valor:
            return asp
        else :
            return None
    except Exception as ex:
        return None

def bilinguismo_sesion(request):
    valor = request.session.get('bilinguismo')
    print "valor encontrado en session=",valor

    if not valor :
        return None
    return buscar_bilinguismo_por_clave(valor)

def inicioB(request):
    if 'bilinguismo' in request.session:
        del request.session['bilinguismo']

    mensaje = ""
    if request.method == 'POST':
        form = ContinuarRegistroFormDE(request.POST)
        if form.is_valid():
            clave = form.cleaned_data['registro']
            asp = buscar_bilinguismo_por_clave(clave)
            if asp:
                if asp.finalizada == True:
                    mensaje = "Usted ya finalizó el formulario"
                else:
                    request.session['bilinguismo']=clave
                    return redirect('bilinguismo_inscripcionB')
            else :
                mensaje = "Número de registro invalido"
    else:
        form = ContinuarRegistroFormDE()

    return render(request, 'inscripcion/iniciar_inscripcionB.html', {
        'mensaje':mensaje,
        'form' : form,
        'opcion_menu' : 0,
    })

def inscripcionB(request):
    persona = bilinguismo_sesion(request)
    #if not aspirante : return redirect('home')
    print "aspirante actual=", persona
    if request.method == 'POST':
        form = BilinguismoForm(request.POST, instance=persona)
        if form.is_valid():
            objeto = form.save()
            objeto.nombre1 = objeto.nombre1.upper()
            objeto.nombre2 = objeto.nombre2.upper()
            objeto.apellido1 = objeto.apellido1.upper()
            objeto.apellido2 = objeto.apellido2.upper()
            objeto.direccion = objeto.direccion.upper()
            objeto.cohorte = 2
            objeto.save()
            clave = objeto.numero_inscripcion()
            request.session['bilinguismo'] = clave
            print "clave=",clave
            return redirect('bilinguismo_datosLaboralesB')
    else :
        form = BilinguismoForm(instance=persona)

    return render(request, 'inscripcion/datosPersonalesB.html', {
        'form': form,
        'solo_lectura': persona.inscripcion_finalizada() if persona else False,
    })

def datosLaboralesB(request):
    persona = bilinguismo_sesion(request)
    if not persona : return redirect('bilinguismo_inicio')
    try:
        laboral = InfoLaboralBilinguismo.objects.get(persona=persona)
    except Exception as ex:
        laboral = None

    if request.method == 'POST':
        form = InfoLaboralBilinguismoForm(request.POST, instance=laboral)
        if form.is_valid():
            objeto = form.save(commit=False)
            objeto.persona = persona
            objeto.save()
            form.save_m2m()
            return redirect('bilinguismo_formacionAcademicaB')
    else :
        form = InfoLaboralBilinguismoForm(instance=laboral)

    numero_registro = request.session['bilinguismo']

    return render(request, 'inscripcion/datosLaboralesB.html', {
        'form': form,
        'clave': numero_registro
    })

def formacionAcademicaB(request):
    persona = bilinguismo_sesion(request)
    if not persona : return redirect('bilinguismo_inicio')
    if request.method == 'POST':
        form = FormacionAcademicaBilinguismoForm(request.POST)
        if form.is_valid():
            objeto = form.save(commit=False)
            objeto.persona = persona
            objeto.save()
            return redirect('bilinguismo_formacionAcademicaB')
    else :
        form = FormacionAcademicaBilinguismoForm()

    estudios = FormacionAcademicaBilinguismo.objects.filter(persona=persona)

    numero_registro = request.session['bilinguismo']

    return render(request, 'inscripcion/formacionAcademicaB.html', {
        'form': form,
        'estudios': estudios,
        'clave': numero_registro,
        'tiene_estudios': len(estudios)
    })

def eliminarFormacionAcademicaB(request, idF):
    persona = bilinguismo_sesion(request)
    if not persona : return redirect('bilinguismo_inicio')

    formAcad = get_object_or_404(FormacionAcademicaBilinguismo.objects, persona=persona, id=idF)
    formAcad.delete()

    return redirect('bilinguismo_formacionAcademicaB')

def certificacionB(request):
    persona = bilinguismo_sesion(request)
    if not persona : return redirect('bilinguismo_inicio')
    estudios = FormacionAcademicaBilinguismo.objects.filter(persona=persona)
    if not len(estudios):
        return redirect('bilinguismo_formacionAcademicaB')

    if request.method == 'POST':
        form = CertificacionBilinguismoForm(request.POST)
        if form.is_valid():
            objeto = form.save(commit=False)
            objeto.persona = persona
            objeto.save()
            return redirect('bilinguismo_certificacionB')        
    else :
        form = CertificacionBilinguismoForm()

    certificaciones = CertificacionBilinguismo.objects.filter(persona=persona)

    numero_registro = request.session['bilinguismo']
    return render(request, 'inscripcion/certificacionesB.html', {
        'form': form,
        'certificaciones': certificaciones,
        'clave': numero_registro,
    })

def eliminarCertificacionB(request, idC):
    persona = bilinguismo_sesion(request)
    if not persona : return redirect('bilinguismo_inicio')

    cerTic = get_object_or_404(CertificacionBilinguismo.objects, persona=persona, id=idC)
    cerTic.delete()

    return redirect('bilinguismo_certificacionB')

def finalizarB(request, tipo):
    persona = bilinguismo_sesion(request)
    if not persona : return redirect('bilinguismo_inicio')

    if tipo == "1": # finalizar por completo
        persona.finalizada = True
        persona.save()
    return redirect("bilinguismo_inicio")

def listaBilinguismo(cohorte):
    estudiantes = []
    cont = 1
    students = Bilinguismo.objects.filter(finalizada=True, cohorte=cohorte).select_related('bilinguismo.InfoLaboralBilinguismo__persona')
    c = 0
    for estudiante in students:
        jornada = ""
        institucion = ""
        try:
            il = InfoLaboralBilinguismo.objects.get(persona=estudiante)
            try:
                jornada = il.get_jornada_display
            except Exception:
                jornada = "---"
            try:
                institucion = il.get_institucion_display
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
            "celular": estudiante.celular,
            }
        )
        cont = cont + 1
    return estudiantes

def reporte(request, cohorte=2):
    grupo = user_group(request)
    if grupo == None:
        return redirect('home')

    personas = listaBilinguismo(cohorte)

    return render(request, 'reportes/registrados.html', {
        'personas': personas,
        'user_group': user_group(request),
        'opcion_menu': 10+int(cohorte),
    })
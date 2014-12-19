from django.shortcuts import redirect, render, render_to_response, get_object_or_404
from malla.forms import *
from django.http import HttpResponse, HttpResponseRedirect
from malla.models import *
from django.core.management import call_command
from django.core.files import File 
from malla.management.commands.lista_contratista import Command

def inicioContratista(request):
    return render(request, 'inicioContratista.html', {'user_group': user_group(request),'opcion_menu': 2,
    })

def get_contratista(request):
    valor = request.session.get('id_contratista')
    try:
        valor = Contratista.objects.get(id=valor)
    except Exception:
        return None
    return valor

def datosBasicos(request):
    contratista = get_contratista(request)

    if request.method == 'POST':
        form = InformacionBasicaForm(request.POST, instance=contratista)
        if form.is_valid():
            objeto = form.save()
            ide = objeto.id
            request.session['id_contratista'] = ide
                       
            return HttpResponseRedirect('infocontacto')
    else :
        form = InformacionBasicaForm(instance=contratista)

    return render(request, 'datosbasicos.html', {
        'form': form,
        'user_group': user_group(request),
        'opcion_menu': 2,
    })

def datosContacto(request):
    monitor = get_contratista(request)
    if not monitor:
        return redirect('inicioContratista')

    try:
        datos = ContratistaInfoContacto.objects.get(monitor=monitor)
    except Exception:
        datos = None

    if request.method == 'POST':
        form = InformacionContactoForm(request.POST, instance=datos)
        if form.is_valid():
            objeto = form.save(commit=False)
            objeto.monitor = monitor
            objeto.save()

            return HttpResponseRedirect('areasconocimiento')
    else :
        form = InformacionContactoForm(instance=datos)

    return render(request, 'datoscontacto.html', {
        'form': form,
        'user_group': user_group(request),
        'opcion_menu': 2,
    })

def areasConocimiento(request):
    monitor = get_contratista(request)
    if not monitor:
        return redirect('inicioContratista')

    try:
        datos = ContratistaAreasConocimiento.objects.get(monitor=monitor)
    except Exception:
        datos = None

    if request.method == 'POST':
        form =AreasConocimientoForm(request.POST, instance=datos)
        if form.is_valid():
            objeto = form.save(commit=False)
            objeto.monitor = monitor
            objeto.save()
            
            return HttpResponseRedirect('soportes')
    else :
        form = AreasConocimientoForm(instance=datos)

    return render(request, 'areasconocimiento.html', {
        'form': form,
        'user_group': user_group(request),
        'opcion_menu': 2,
    })

def requerimiento(request, id=None):
    grupo = user_group(request)
    if grupo == None:
        return redirect('home')
    try:
        requerimiento = Requerimiento.objects.get(id=id)
    except Exception:
        requerimiento = None

    if request.method == 'POST':
        form = RequerimientoForm(request.POST, instance=requerimiento)
        if form.is_valid():
            objeto = form.save()
            objeto.save()
            
            return redirect('listar_requerimientos')
    else :
        form = RequerimientoForm(instance=requerimiento)

    return render(request, 'requerimiento.html', {
        'form': form,
        'user_group': user_group(request),
        'opcion_menu': 4,
    })

def listar_requerimientos(request):
    requerimientos = Requerimiento.objects.all()
    return render(request, 'listar_requerimientos.html', {
        'requerimientos': requerimientos,
        'user_group': user_group(request),
        'opcion_menu': 4,
    })

def eliminar_requerimiento(request, id):
    req = Requerimiento.objects.get(id=id)
    req.delete()
    return redirect('listar_requerimientos')

def reclamacion(request, id=None):
    grupo = user_group(request)
    if grupo == None:
        return redirect('home')

    numero_documento = request.user.username
    contratista = Contratista.objects.get(numero_documento=numero_documento)

    if request.method == 'POST':
        form = ReclamacionForm(request.POST)
        if form.is_valid():
            objeto = form.save(commit=False)
            objeto.persona = contratista
            
            objeto.estado = 'PR'
            objeto.save()
            
            return redirect('listar_reclamaciones')
    else :
        form = ReclamacionForm()

    return render(request, 'reclamacion.html', {
        'form': form,
        'user_group': user_group(request),
        'opcion_menu': 5,
    })

def reclamacion_modificar(request, id):
    grupo = user_group(request)
    if grupo == None:
        return redirect('home')

    #numero_documento = request.user.username
    #contratista = Contratista.objects.get(numero_documento=numero_documento)
    reclamacion = Reclamacion.objects.get(id = id)

    if request.method == 'POST':
        form = ReclamacionModificarForm(request.POST, instance=reclamacion)
        if form.is_valid():
            objeto = form.save(commit=False)
            #objeto.persona = contratista
            #if objecto.estado != None:
            #    objeto.estado = 'PR'
            objeto.save()
            
            return redirect('listar_reclamaciones')
    else :
        form = ReclamacionModificarForm(instance=reclamacion)

    return render(request, 'reclamacion.html', {
        'form': form,
        'user_group': user_group(request),
        'opcion_menu': 6,
    })

def soportes(request):
    monitor = get_contratista(request)
    if not monitor:
        return redirect('inicioContratista')

    if request.method == 'POST':
        form = DocumentosSoporteForm(request.POST, request.FILES)
        
        if form.is_valid():
            obj = form.save(commit=False)
            obj.monitor = monitor
            obj.save()
            return redirect('finalizar_contratista')

    else:
        form = DocumentosSoporteForm()

    return render(request, 'soportes.html', {
        'form': form,
        'user_group': user_group(request),
        'opcion_menu': 2,
    })

def finalizar_contratista(request):
    monitor = get_contratista(request)
    if not monitor:
        return redirect('inicioContratista')

    monitor.finalizado = True
    monitor.save()
    del request.session['id_contratista']

    return render(request, 'finalizar_contratista.html', {
        'user_group': user_group(request),
        'opcion_menu': 1,
    })

def lista_asignaturas(request):
    if request.method == 'POST':
        idProfesor = request.POST.get('idProfesor')
        profesor = Formador.objects.get(idProfesor)
        return []
    else:
        return redirect('lista');

def lista(request, id=None):
    grupo = user_group(request)
    if grupo == None:
        return redirect('home')
    try:
        lista_obj = Lista.objects.get(id=id)
    except Exception:
        lista_obj = None

    username = ""
    if request.user.is_authenticated():
        global username 
        username = request.user.username

    if request.method == 'POST':
        form = ListaForm(request.POST, instance=lista_obj)
        if form.is_valid():
            objeto = form.save(commit=False)
            objeto.usuario = username
            objeto.save()
            
            return redirect('reporte_lista')
    else :
        form = ListaForm(instance=lista_obj)

    return render(request, 'lista.html', {
        'form': form,
        'user_group': user_group(request),
        'opcion_menu': 5,
    })
def eliminar_lista(request, id):
    lista = Lista.objects.get(id=id)
    lista.delete()
    return redirect('reporte_lista')

def modificar_lista(request, id):
    print id


def reporte_lista(request, limit=100):
    grupo = user_group(request)
    if grupo == None:
        return redirect('home')

    lista_list = Lista.objects.all() 
    form = FiltroReporte() 

    if request.method == 'POST':
        form = FiltroReporte(request.POST)
        if form.is_valid():
            fi = form.cleaned_data['fecha_inicial']
            ff = form.cleaned_data['fecha_final']

            response = redirect('lista_reporte_contratista')
            response['Location'] += "?fi="+str(fi)+'&ff='+str(ff)
            return response
        else:
            return redirect('reporte_lista')    
     
    
    return render(request, 'reportelista.html', {'lista_list': lista_list, 'user_group': user_group(request),
        'opcion_menu': 5, 'form':form})

def lista_contratista(request, limit=100):
    grupo = user_group(request)
    if grupo == None:
        return redirect('home')

    numero_documento = request.user.username

    contratista = Contratista.objects.get(numero_documento=numero_documento)
    try:
        lista_list = Lista.objects.filter(contratista=contratista)
    except:
        lista_list = []
    
    return render(request, 'reportelista.html', {'lista_list': lista_list, 'user_group': user_group(request),
        'opcion_menu': 1,})

def monitor(request, id=None):
    grupo = user_group(request)
    if grupo == None:
        return redirect('home')

    try:
        monitor_obj = Monitor.objects.get(id=id)
    except Exception:
        monitor_obj = None

    if request.method == 'POST':
        form = MonitorForm(request.POST, instance=monitor_obj)
        if form.is_valid():
            objeto = form.save()
            ide = objeto.id
            ide = "?v="+str(ide)
                       
            return redirect('listar_monitores')
    else :
        form = MonitorForm(instance=monitor_obj)

    return render(request, 'monitor.html', {
        'form': form, 'user_group': user_group(request),
        'opcion_menu': 3,
    })

def listar_monitores(request):
    monitores = Monitor.objects.all()
    return render(request, 'listar_monitores.html', {
        'monitores': monitores,
        'user_group': user_group(request),
        'opcion_menu': 3,
    })

def eliminar_monitor(request, id):
    monitor = Monitor.objects.get(id=id)
    monitor.delete()
    return redirect('listar_monitores')

def listar_contratistas(request):
    contratistas = Contratista.objects.all()
    return render(request, 'listar_contratistas.html', {
        'contratistas': contratistas,
        'user_group': user_group(request),
        'opcion_menu': 2,
    })

def modificarContratista(request, id):
    request.session['id_contratista'] = id
    return redirect('datos_basicos')

def eliminar_contratista(request, id):
    contratista = Contratista.objects.get(id=id)
    contratista.delete()
    return redirect('listar_contratistas')

def listar_reclamaciones(request):
    contratistas = Reclamacion.objects.all()

    return render(request, 'listar_reclamaciones.html', {
        'contratistas': contratistas,
        'user_group': user_group(request),
        'opcion_menu': 6,
    })

def listar_reclamaciones_contratista(request):

    numero_documento = request.user.username
    contratista = Contratista.objects.get(numero_documento=numero_documento)
    try:
        contratistas = Reclamacion.objects.filter(contratista=contratista)
    except:
        contratistas = []

    return render(request, 'listar_reclamaciones.html', {
        'contratistas': contratistas,
        'user_group': user_group(request),
        'opcion_menu': 2,
    })

def lista_reporte_contratista(request):
    # descomentar  linea 380 y 381 (2 de abajo) para que genere el archivo y luego lo descargue. Hacer que si ya existe, lo elimine antes.
    
    if request.method == 'GET' and 'fi' in request.GET and 'ff' in request.GET:
        fi = request.GET.get('fi')
        ff = request.GET.get('ff')

    c = Command()
    c.handle(fi,ff)

    archivo = open('ReporteListaContratistas.csv', "r") 
    archivo = File(archivo) 

    response = HttpResponse(archivo, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="ReporteListaContratistas.csv"'
    return response


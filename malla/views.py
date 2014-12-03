from django.shortcuts import redirect, render, render_to_response, get_object_or_404
from malla.forms import *
from django.http import HttpResponse, HttpResponseRedirect
from malla.models import *

def inicioContratista(request):
    return render(request, 'inicioContratista.html', {
    })

def get_contratista(request):
    valor = request.session.get('id_contratista')
    try:
        valor = ContratistaInfoPersonal.objects.get(id=valor)
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
            
            return redirect('home')
    else :
        form = RequerimientoForm(instance=requerimiento)

    return render(request, 'requerimiento.html', {
        'form': form,
    })

def listar_requerimientos(request):
    requerimientos = Requerimiento.objects.all()
    return render(request, 'listar_requerimientos.html', {
        'requerimientos': requerimientos,
    })

def eliminar_requerimiento(request, id):
    req = Requerimiento.objects.get(id=id)
    req.delete()
    return redirect('listar_requerimientos')

def reclamacion(request):
    grupo = user_group(request)
    if grupo == None:
        return redirect('home')

    if request.method == 'POST':
        form = ReclamacionForm(request.POST)
        if form.is_valid():
            objeto = form.save()
            objeto.save()
            
            return redirect('home')
    else :
        form = ReclamacionForm()

    return render(request, 'reclamacion.html', {
        'form': form,
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
    })

def finalizar_contratista(request):
    monitor = get_contratista(request)
    if not monitor:
        return redirect('inicioContratista')

    monitor.finalizado = True
    monitor.save()
    del request.session['id_contratista']

    return render(request, 'finalizar_contratista.html', {
    })

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
            
            return redirect('home')
    else :
        form = ListaForm(instance=lista_obj)

    return render(request, 'lista.html', {
        'form': form,
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
    
    return render(request, 'reportelista.html', {'lista_list': lista_list})

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
                       
            return redirect('home')
    else :
        form = MonitorForm(instance=monitor_obj)

    return render(request, 'monitor.html', {
        'form': form,
    })

def listar_monitores(request):
    monitores = Monitor.objects.all()
    return render(request, 'listar_monitores.html', {
        'monitores': monitores,
    })

def eliminar_monitor(request, id):
    monitor = Monitor.objects.get(id=id)
    monitor.delete()
    return redirect('listar_monitores')

def listar_contratistas(request):
    contratistas = ContratistaInfoPersonal.objects.all()
    return render(request, 'listar_contratistas.html', {
        'contratistas': contratistas,
    })

def modificarContratista(request, id):
    request.session['id_contratista'] = id
    return redirect('datos_basicos')

def eliminar_contratista(request, id):
    contratista = ContratistaInfoPersonal.objects.get(id=id)
    contratista.delete()
    return redirect('listar_contratistas')
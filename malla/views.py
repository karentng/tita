from django.shortcuts import redirect, render, render_to_response, get_object_or_404
from malla.forms import *
from django.http import HttpResponse, HttpResponseRedirect
from malla.models import *

def inicioContratista(request):
    return render(request, 'inicioContratista.html', {
    })

def datosBasicos(request):
    if request.method == 'POST':
        form = InformacionBasicaForm(request.POST)
        if form.is_valid():
            objeto = form.save()
            ide = objeto.id
            ide = "?v="+str(ide)
                       
            return HttpResponseRedirect('infocontacto%s' % ide)
    else :
        form = InformacionBasicaForm()

    return render(request, 'datosbasicos.html', {
        'form': form,
    })

def datosContacto(request):
    identificador = request.GET['v']
    monitor = ContratistaInfoPersonal.objects.get(id=identificador)

    if request.method == 'POST':
        form = InformacionContactoForm(request.POST)
        if form.is_valid():
            objeto = form.save(commit=False)
            objeto.monitor = monitor
            objeto.save()
            ide = "?v="+str(monitor.id)

            return HttpResponseRedirect('areasconocimiento%s' % ide)
    else :
        form = InformacionContactoForm()

    return render(request, 'datoscontacto.html', {
        'form': form,
    })

def areasConocimiento(request):
    identificador = request.GET['v']
    monitor = ContratistaInfoPersonal.objects.get(id=identificador)

    if request.method == 'POST':
        form =AreasConocimientoForm(request.POST)
        if form.is_valid():
            objeto = form.save(commit=False)
            objeto.monitor = monitor
            objeto.save()
            ide = "?v="+str(monitor.id)
            
            return HttpResponseRedirect('soportes%s' % ide)
    else :
        form = AreasConocimientoForm()

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

    identificador = request.GET['v']
    monitor = ContratistaInfoPersonal.objects.get(id=identificador)

    if request.method == 'POST':
        print "as"
        form = DocumentosSoporteForm(request.POST, request.FILES)
        
        if form.is_valid():
            obj = form.save(commit=False)
            obj.monitor = monitor
            obj.save()
            print "sdfs"
            return redirect('finalizar_contratista')

    else:
        print "asdafdsa"
        form = DocumentosSoporteForm()

        
    return render(request, 'soportes.html', {
        'form': form,
    })

def finalizar_contratista(request):
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

def monitor(request):
    grupo = user_group(request)
    if grupo == None:
        return redirect('home')

    if request.method == 'POST':
        form = MonitorForm(request.POST)
        if form.is_valid():
            objeto = form.save()
            ide = objeto.id
            ide = "?v="+str(ide)
                       
            return HttpResponseRedirect('home')
    else :
        form = MonitorForm()

    return render(request, 'monitor.html', {
        'form': form,
    })

from django.shortcuts import redirect, render, render_to_response, get_object_or_404
from malla.forms import *
from django.http import HttpResponse, HttpResponseRedirect
from malla.models import *

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
    monitor = MonitorInfoPersonal.objects.get(id=identificador)

    if request.method == 'POST':
        form = InformacionContactoForm(request.POST)
        if form.is_valid():
            objeto = form.save(commit=False)
            objeto.monitor = monitor
            objeto.save()
            ide = "?v="+str(monitor.id)

            return HttpResponseRedirect('infoacademica%s' % ide)
    else :
        form = InformacionContactoForm()

    return render(request, 'datoscontacto.html', {
        'form': form,
    })

def datosAcademicos(request):
    identificador = request.GET['v']
    monitor = MonitorInfoPersonal.objects.get(id=identificador)

    if request.method == 'POST':
        form = InformacionAcademicaForm(request.POST)
        if form.is_valid():
            objeto = form.save(commit=False)
            objeto.monitor = monitor
            objeto.save()
            ide = "?v="+str(monitor.id)
            
            return HttpResponseRedirect('areasconocimiento%s' % ide)
    else :
        form = InformacionAcademicaForm()

    return render(request, 'datosacademicos.html', {
        'form': form,
    })


def areasConocimiento(request):
    identificador = request.GET['v']
    monitor = MonitorInfoPersonal.objects.get(id=identificador)

    if request.method == 'POST':
        form =AreasConocimientoForm(request.POST)
        if form.is_valid():
            objeto = form.save(commit=False)
            objeto.monitor = monitor
            objeto.save()
            ide = "?v="+str(monitor.id)
            
            return HttpResponseRedirect('horarios%s' % ide)
    else :
        form = AreasConocimientoForm()

    return render(request, 'areasconocimiento.html', {
        'form': form,
    })

def horarios(request):
    identificador = request.GET['v']
    monitor = MonitorInfoPersonal.objects.get(id=identificador)
    if request.method == 'POST':
        form =HorariosDisponiblesForm(request.POST)
        if form.is_valid():
            objeto = form.save(commit=False)
            objeto.monitor = monitor
            objeto.save()
            ide = "?v="+str(monitor.id)
            
            return HttpResponseRedirect('soportes%s' % ide)
    else :
        form = HorariosDisponiblesForm()

    return render(request, 'horarios_disponibilidad.html', {
        'form': form,
    })


def componente(request):
    if request.method == 'POST':
        form = ComponenteForm(request.POST)
        if form.is_valid():
            objeto = form.save()
            objeto.save()
            
            return redirect('home')
    else :
        form = ComponenteForm()

    return render(request, 'componente.html', {
        'form': form,
    })

def requerimiento(request):
    if request.method == 'POST':
        form = RequerimientoForm(request.POST)
        if form.is_valid():
            objeto = form.save()
            objeto.save()
            
            return redirect('home')
    else :
        form = RequerimientoForm()

    return render(request, 'requerimiento.html', {
        'form': form,
    })

def reto(request):
    if request.method == 'POST':
        form = RetoForm(request.POST)
        if form.is_valid():
            objeto = form.save()
            objeto.save()
            
            return redirect('home')
    else :
        form = RetoForm()

    return render(request, 'reto.html', {
        'form': form,
    })

def reclamacion(request):
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
    monitor = MonitorInfoPersonal.objects.get(id=identificador)

    if request.method == 'POST':
        print "as"
        form = DocumentosSoporteForm(request.POST, request.FILES)
        
        if form.is_valid():
            obj = form.save(commit=False)
            obj.monitor = monitor
            obj.save()
            print "sdfs"
            return redirect('home')

    else:
        print "asdafdsa"
        form = DocumentosSoporteForm()

        
    return render(request, 'soportes.html', {
        'form': form,
    })

def lista(request):

    username = ""
    if request.user.is_authenticated():
        global username 
        username = request.user.username

    if request.method == 'POST':
        form = ListaForm(request.POST)
        if form.is_valid():
            objeto = form.save(commit=False)
            objeto.usuario = username
            objeto.save()
            
            return redirect('home')
    else :
        form = ListaForm()

    return render(request, 'lista.html', {
        'form': form,
    })

def reporte_lista(request, limit=100):
    lista_list = Lista.objects.all()    
    
    return render(request, 'reportelista.html', {'lista_list': lista_list})

def modificar_lista(request, limit=100):
    lista_list = Lista.objects.all()    
    
    return render(request, 'reportelista.html', {'lista_list': lista_list})

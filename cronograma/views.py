from django.shortcuts import render
from cronograma.forms import *
from campus.forms import ActividadForm
from campus.models import Clases, AcompanamientoInSitus, Estudiante, Cursos
import json
from django.shortcuts import redirect, render, render_to_response
from datetime import datetime, date, timedelta
from math import ceil
import datetime 
from campus.views import user_group

def cronograma(request):
    # if this is a POST request we need to process the form data
    grupo = user_group(request)
    if grupo == None:
        return redirect('home')

    if request.method == 'POST':
        form = EventosAcompanamientoForm(request.POST)
                
        if form.is_valid():
            objeto = AcompanamientoInSitus()
            objeto = form.save()
            objeto.nombre="Sesion"+str(objeto.nombre)
            #objeto.tipo = "2"
            objeto.save()

            postFormatoDict = request.POST.dict() #obtuvimos el post
            post = str(postFormatoDict)

            repetir_hasta = datetime.datetime.now()
                
            if 'repetir-'in post: 

                global repetir_hasta
                repetir_fecha = request.POST['repetirfecha']
                repetir_fecha = str(repetir_fecha)
                repetir_hasta = datetime.datetime(int(repetir_fecha[0:4]),int(repetir_fecha[5:7]),int(repetir_fecha[8:10]))

                repetir = request.POST['repetir-']
                fecha = objeto.fecha_inicio
                #fecha = fecha.toordinal()

                mes = int(fecha.month)
                dia = int(fecha.day)
                ano = int(fecha.year)
                                
                if repetir == "1":
                    for i in range(1, int((repetir_hasta - fecha).days + 2)):
                        if ((dia + 1) > 31) and (mes == 1):
                            global mes, dia, ano
                            #global dia
                            dia = (dia + 1) - 31
                            mes = mes + 1
                            nueva_fecha = datetime.datetime(ano, mes, dia, fecha.hour, fecha.minute, 00, 000000)
                           
                        elif ((dia + 1) > 31) and (mes == 12):
                            global mes, dia, ano
                            #global dia
                            dia = (dia + 1) - 31
                            mes = (mes + 1) -12
                            ano = ano + 1
                            nueva_fecha = datetime.datetime(ano, mes, dia, fecha.hour, fecha.minute, 00, 000000)
                        elif ((dia + 1) > 31) and (mes == 3):
                            global mes, dia
                            #global dia
                            dia = (dia + 1) - 31
                            mes = mes + 1
                            nueva_fecha = datetime.datetime(ano, mes, dia, fecha.hour, fecha.minute, 00, 000000)
                        elif ((dia + 1) > 31) and (mes == 5):
                            global mes, dia
                            #global dia
                            dia = (dia + 1) - 31
                            mes = mes + 1
                            nueva_fecha = datetime.datetime(ano, mes, dia, fecha.hour, fecha.minute, 00, 000000)
                        elif ((dia + 1) > 31) and (mes == 7):
                            global mes, dia
                            #global dia
                            dia = (dia + 1) - 31
                            mes = mes + 1
                            nueva_fecha = datetime.datetime(ano, mes, dia, fecha.hour, fecha.minute, 00, 000000)
                        elif ((dia + 1) > 31) and (mes == 8):
                            global mes, dia
                            #global dia
                            dia = (dia + 1) - 31
                            mes = mes + 1
                            nueva_fecha = datetime.datetime(ano, mes, dia, fecha.hour, fecha.minute, 00, 000000)
                        elif ((dia + 1) > 31) and (mes == 10):
                            global mes, dia
                            #global dia
                            dia = (dia + 1) - 31
                            mes = mes + 1
                            nueva_fecha = datetime.datetime(ano, mes, dia, fecha.hour, fecha.minute, 00, 000000)
                        elif ((dia + 1) > 30) and (mes == 4):
                            global mes, dia
                            #global dia
                            dia = (dia + 1) - 30
                            mes = mes + 1
                            nueva_fecha = datetime.datetime(ano, mes, dia, fecha.hour, fecha.minute, 00, 000000)
                        elif ((dia + 1) > 30) and (mes == 6):
                            global mes, dia
                            #global dia
                            dia = (dia + 1) - 30
                            mes = mes + 1
                            nueva_fecha = datetime.datetime(ano, mes, dia, fecha.hour, fecha.minute, 00, 000000)
                        elif ((dia + 1) > 30) and (mes == 9):
                            global mes, dia
                            #global dia
                            dia = (dia + 1) - 30
                            mes = mes + 1
                            nueva_fecha = datetime.datetime(ano, mes, dia, fecha.hour, fecha.minute, 00, 000000)
                        elif ((dia + 1) > 30) and (mes == 11):
                            global mes, dia
                            #global dia
                            dia = (dia + 1) - 30
                            mes = mes + 1
                            nueva_fecha = datetime.datetime(ano, mes, dia, fecha.hour, fecha.minute, 00, 000000)
                        elif ((dia + 1) > 28) and (mes == 2): 
                            global mes, dia
                            #global dia
                            dia = (dia + 1) - 28
                            mes = mes + 1
                            nueva_fecha = datetime.datetime(ano, mes, dia, fecha.hour, fecha.minute, 00, 000000)
                        else:
                            global dia
                            dia = dia + 1
                            nueva_fecha = datetime.datetime(ano, mes, dia, fecha.hour, fecha.minute, 00, 000000)
                            
                        objetoi = AcompanamientoInSitus()
                        objetoi.curso=objeto.curso
                        objetoi.nombre="Sesion"+str(objeto.nombre)
                        objetoi.fecha_inicio=nueva_fecha
                        objetoi.duracion=objeto.duracion
                        objetoi.descripcion=objeto.descripcion
                        
                        objetoi.save()
                                                   

                if repetir == "2":
                    for i in range(1, (int((repetir_hasta - fecha).days + 2)/7)+1):
                        if ((dia + 7) > 31) and (mes == 1):
                            global mes, dia, ano
                            #global dia
                            dia = (dia + 7) - 31
                            mes = mes + 1
                            nueva_fecha = datetime.datetime(ano, mes, dia, fecha.hour, fecha.minute, 00, 000000)
                           
                        elif ((dia + 7) > 31) and (mes == 12):
                            global mes, dia, ano
                            #global dia
                            dia = (dia + 7) - 31
                            mes = (mes + 1) - 12
                            ano = ano + 1
                            nueva_fecha = datetime.datetime(ano, mes, dia, fecha.hour, fecha.minute, 00, 000000)
                        elif ((dia + 7) > 31) and (mes == 3):
                            global mes, dia, ano
                            #global dia
                            dia = (dia + 7) - 31
                            mes = mes + 1
                            nueva_fecha = datetime.datetime(ano, mes, dia, fecha.hour, fecha.minute, 00, 000000)
                        elif ((dia + 7) > 31) and (mes == 5):
                            global mes, dia, ano
                            #global dia
                            dia = (dia + 7) - 31
                            mes = mes + 1
                            nueva_fecha = datetime.datetime(ano, mes, dia, fecha.hour, fecha.minute, 00, 000000)
                        elif ((dia + 7) > 31) and (mes == 7):
                            global mes, dia, ano
                            #global dia
                            dia = (dia + 7) - 31
                            mes = mes + 1
                            nueva_fecha = datetime.datetime(ano, mes, dia, fecha.hour, fecha.minute, 00, 000000)
                        elif ((dia + 7) > 31) and (mes == 8):
                            global mes, dia, ano
                            #global dia
                            dia = (dia + 7) - 31
                            mes = mes + 1
                            nueva_fecha = datetime.datetime(ano, mes, dia, fecha.hour, fecha.minute, 00, 000000)
                        elif ((dia + 7) > 31) and (mes == 10):
                            global mes, dia, ano
                            #global dia
                            dia = (dia + 7) - 31
                            mes = mes + 1
                            nueva_fecha = datetime.datetime(ano, mes, dia, fecha.hour, fecha.minute, 00, 000000)
                        elif ((dia + 7) > 30) and (mes == 4):
                            global mes, dia, ano
                            #global dia
                            dia = (dia + 7) - 30
                            mes = mes + 1
                            nueva_fecha = datetime.datetime(ano, mes, dia, fecha.hour, fecha.minute, 00, 000000)
                        elif ((dia + 7) > 30) and (mes == 6):
                            global mes, dia, ano
                            #global dia
                            dia = (dia + 7) - 30
                            mes = mes + 1
                            nueva_fecha = datetime.datetime(ano, mes, dia, fecha.hour, fecha.minute, 00, 000000)
                        elif ((dia + 7) > 30) and (mes == 9):
                            global mes, dia, ano
                            #global dia
                            dia = (dia + 7) - 30
                            mes = mes + 1
                            nueva_fecha = datetime.datetime(ano, mes, dia, fecha.hour, fecha.minute, 00, 000000)
                        elif ((dia + 7) > 30) and (mes == 11):
                            global mes, dia, ano
                            #global dia
                            dia = (dia + 7) - 30
                            mes = mes + 1
                            nueva_fecha = datetime.datetime(ano, mes, dia, fecha.hour, fecha.minute, 00, 000000)
                        elif ((dia + 7) > 28) and (mes == 2): 
                            global mes, dia, ano
                            #global dia
                            dia = (dia + 7) - 28
                            mes = mes + 1
                            nueva_fecha = datetime.datetime(ano, mes, dia, fecha.hour, fecha.minute, 00, 000000)
                        else:
                            global dia
                            dia = dia + 7
                            nueva_fecha = datetime.datetime(ano, mes, dia, fecha.hour, fecha.minute, 00, 000000)
                            
                        objetoi = AcompanamientoInSitus()
                        objetoi.curso=objeto.curso
                        objetoi.nombre="Sesion"+str(objeto.nombre)
                        objetoi.fecha_inicio=nueva_fecha
                        objetoi.duracion=objeto.duracion
                        objetoi.descripcion=objeto.descripcion
                        
                        objetoi.save()
                
                if repetir == "3":

                    meses_entre_anos = 0

                    if((int(repetir_hasta.year)-int(fecha.year))>0):
                        global meses_entre_anos
                        meses_entre_anos = ((int(repetir_hasta.year)-int(fecha.year))*12)
                    
                    else:
                        global meses_entre_anos
                        meses_entre_anos=0


                    numero_meses = ((12 - int(fecha.month))+meses_entre_anos) - (12 - int(repetir_hasta.month)) + 1

                    global numero_meses

                    for i in range(1, numero_meses ):
                        if mes == 12:
                            global mes, ano
                            mes = (mes + 1)-12
                            ano = ano + 1
                            nueva_fecha = datetime.datetime(ano, mes, dia, fecha.hour, fecha.minute, 00, 000000)
                           
                        else:
                            global mes, ano
                            mes = mes + 1
                            nueva_fecha = datetime.datetime(ano, mes, dia, fecha.hour, fecha.minute, 00, 000000)
                            
                        objetoi = AcompanamientoInSitus()
                        objetoi.curso=objeto.curso
                        objetoi.nombre="Sesion"+str(objeto.nombre)
                        objetoi.fecha_inicio=nueva_fecha
                        objetoi.duracion=objeto.duracion
                        objetoi.descripcion=objeto.descripcion
                        
                        objetoi.save()

            
            

            return redirect('cronograma_acompanamiento')
    else:

        form = EventosAcompanamientoForm()

    eventos = AcompanamientoInSitus.objects.all()

    events = []

    for i in eventos:
        inicio = i.fecha_inicio
        #fin = i.fecha_finalizacion

        hora_inicio = [i.fecha_inicio.hour, i.fecha_inicio.minute, 0]
        #hora_finalizacion = [i.fecha_finalizacion.hour, i.fecha_finalizacion.minute, 0]
        hora_finalizacion = [i.fecha_inicio.hour + i.duracion, i.fecha_inicio.minute, 0]

        diasTotal = 0
        
        #diasEvento = 1
        diasEvento = []
        for j in range(0, diasTotal+1):
            aux = inicio + timedelta(days = j)
            diasEvento.append([aux.year, aux.month-1, aux.day])

        events.append({
            'id': i.id,
            'nombre': i.nombre,
            'descripcion': i.descripcion,
            'hora_inicio': hora_inicio,
            'hora_finalizacion': hora_finalizacion,
            'diasEvento': diasEvento,
            
        })
    '''
    for i in eventos:
        inicio = i.fecha_inicio
        fin = i.fecha_finalizacion
        events.append({
            'nombre': i.nombre,
            'inicio': [inicio.year, inicio.month-1, inicio.day],
            'fin': [fin.year, fin.month-1, fin.day],
            'descripcion': i.descripcion
        })'''
    
    return render(request, 'cronograma.html', {
        'formAcompanamiento': form,
        'eventos': json.dumps(events),
        'user_group': user_group(request),
        'opcion_menu': 4,
    })


def menor10(val):
    if val < 10:
        return "0"+str(val)
    return str(val)


def diplomado(request):
    # if this is a POST request we need to process the form data
    grupo = user_group(request)
    if grupo == None:
        return redirect('home')

    if request.method == 'POST':
        form = EventosDiplomadoForm(request.POST)
        if form.is_valid():
            objeto = Clases()
            
            objeto = form.save()
            
            #objeto.tipo = "1"
            objeto.save()

            postFormatoDict = request.POST.dict() #obtuvimos el post
            post = str(postFormatoDict)

            repetir_hasta = datetime.datetime.now()
                
            if 'repetir-'in post: 

                global repetir_hasta
                repetir_fecha = request.POST['repetirfecha']
                repetir_fecha = str(repetir_fecha)
                repetir_hasta = datetime.datetime(int(repetir_fecha[0:4]),int(repetir_fecha[5:7]),int(repetir_fecha[8:10]))

                repetir = request.POST['repetir-']
                fecha = objeto.fecha_inicio
                #fecha = fecha.toordinal()

                mes = int(fecha.month)
                dia = int(fecha.day)
                ano = int(fecha.year)
                                
                if repetir == "1":
                    for i in range(1, int((repetir_hasta - fecha).days + 2)):
                        if ((dia + 1) > 31) and (mes == 1):
                            global mes, dia, ano
                            #global dia
                            dia = (dia + 1) - 31  
                            mes = mes + 1
                            nueva_fecha = datetime.datetime(ano, mes, dia, fecha.hour, fecha.minute, 00, 000000)
                           
                        elif ((dia + 1) > 31) and (mes == 12):
                            global mes, dia, ano
                            #global dia
                            dia = (dia + 1) - 31
                            mes = (mes + 1) -12
                            ano = ano + 1
                            nueva_fecha = datetime.datetime(ano, mes, dia, fecha.hour, fecha.minute, 00, 000000)
                        elif ((dia + 1) > 31) and (mes == 3):
                            global mes, dia
                            #global dia
                            dia = (dia + 1) - 31
                            mes = mes + 1
                            nueva_fecha = datetime.datetime(ano, mes, dia, fecha.hour, fecha.minute, 00, 000000)
                        elif ((dia + 1) > 31) and (mes == 5):
                            global mes, dia
                            #global dia
                            dia = (dia + 1) - 31
                            mes = mes + 1
                            nueva_fecha = datetime.datetime(ano, mes, dia, fecha.hour, fecha.minute, 00, 000000)
                        elif ((dia + 1) > 31) and (mes == 7):
                            global mes, dia
                            #global dia
                            dia = (dia + 1) - 31
                            mes = mes + 1
                            nueva_fecha = datetime.datetime(ano, mes, dia, fecha.hour, fecha.minute, 00, 000000)
                        elif ((dia + 1) > 31) and (mes == 8):
                            global mes, dia
                            #global dia
                            dia = (dia + 1) - 31
                            mes = mes + 1
                            nueva_fecha = datetime.datetime(ano, mes, dia, fecha.hour, fecha.minute, 00, 000000)
                        elif ((dia + 1) > 31) and (mes == 10):
                            global mes, dia
                            #global dia
                            dia = (dia + 1) - 31
                            mes = mes + 1
                            nueva_fecha = datetime.datetime(ano, mes, dia, fecha.hour, fecha.minute, 00, 000000)
                        elif ((dia + 1) > 30) and (mes == 4):
                            global mes, dia
                            #global dia
                            dia = (dia + 1) - 30
                            mes = mes + 1
                            nueva_fecha = datetime.datetime(ano, mes, dia, fecha.hour, fecha.minute, 00, 000000)
                        elif ((dia + 1) > 30) and (mes == 6):
                            global mes, dia
                            #global dia
                            dia = (dia + 1) - 30
                            mes = mes + 1
                            nueva_fecha = datetime.datetime(ano, mes, dia, fecha.hour, fecha.minute, 00, 000000)
                        elif ((dia + 1) > 30) and (mes == 9):
                            global mes, dia
                            #global dia
                            dia = (dia + 1) - 30
                            mes = mes + 1
                            nueva_fecha = datetime.datetime(ano, mes, dia, fecha.hour, fecha.minute, 00, 000000)
                        elif ((dia + 1) > 30) and (mes == 11):
                            global mes, dia
                            #global dia
                            dia = (dia + 1) - 30
                            mes = mes + 1
                            nueva_fecha = datetime.datetime(ano, mes, dia, fecha.hour, fecha.minute, 00, 000000)
                        elif ((dia + 1) > 28) and (mes == 2): 
                            global mes, dia
                            #global dia
                            dia = (dia + 1) - 28
                            mes = mes + 1
                            nueva_fecha = datetime.datetime(ano, mes, dia, fecha.hour, fecha.minute, 00, 000000)
                        else:
                            global dia
                            dia = dia + 1
                            nueva_fecha = datetime.datetime(ano, mes, dia, fecha.hour, fecha.minute, 00, 000000)
                            
                        objetoi = Clases()
                        objetoi.curso=objeto.curso
                        objetoi.nombre="Sesion"+str(objeto.nombre)
                        objetoi.fecha_inicio=nueva_fecha
                        objetoi.duracion=objeto.duracion
                        objetoi.descripcion=objeto.descripcion
                        #objetoi.tipo=objeto.tipo
                        objetoi.save()
                                                   

                if repetir == "2":
                    for i in range(1, (int((repetir_hasta - fecha).days + 2)/7)+1):
                        if ((dia + 7) > 31) and (mes == 1):
                            global mes, dia, ano
                            #global dia
                            dia = (dia + 7) - 31
                            mes = mes + 1
                            nueva_fecha = datetime.datetime(ano, mes, dia, fecha.hour, fecha.minute, 00, 000000)
                           
                        elif ((dia + 7) > 31) and (mes == 12):
                            global mes, dia, ano
                            #global dia
                            dia = (dia + 7) - 31
                            mes = (mes + 1) - 12
                            ano = ano + 1
                            nueva_fecha = datetime.datetime(ano, mes, dia, fecha.hour, fecha.minute, 00, 000000)
                        elif ((dia + 7) > 31) and (mes == 3):
                            global mes, dia, ano
                            #global dia
                            dia = (dia + 7) - 31
                            mes = mes + 1
                            nueva_fecha = datetime.datetime(ano, mes, dia, fecha.hour, fecha.minute, 00, 000000)
                        elif ((dia + 7) > 31) and (mes == 5):
                            global mes, dia, ano
                            #global dia
                            dia = (dia + 7) - 31
                            mes = mes + 1
                            nueva_fecha = datetime.datetime(ano, mes, dia, fecha.hour, fecha.minute, 00, 000000)
                        elif ((dia + 7) > 31) and (mes == 7):
                            global mes, dia, ano
                            #global dia
                            dia = (dia + 7) - 31
                            mes = mes + 1
                            nueva_fecha = datetime.datetime(ano, mes, dia, fecha.hour, fecha.minute, 00, 000000)
                        elif ((dia + 7) > 31) and (mes == 8):
                            global mes, dia, ano
                            #global dia
                            dia = (dia + 7) - 31
                            mes = mes + 1
                            nueva_fecha = datetime.datetime(ano, mes, dia, fecha.hour, fecha.minute, 00, 000000)
                        elif ((dia + 7) > 31) and (mes == 10):
                            global mes, dia, ano
                            #global dia
                            dia = (dia + 7) - 31
                            mes = mes + 1
                            nueva_fecha = datetime.datetime(ano, mes, dia, fecha.hour, fecha.minute, 00, 000000)
                        elif ((dia + 7) > 30) and (mes == 4):
                            global mes, dia, ano
                            #global dia
                            dia = (dia + 7) - 30
                            mes = mes + 1
                            nueva_fecha = datetime.datetime(ano, mes, dia, fecha.hour, fecha.minute, 00, 000000)
                        elif ((dia + 7) > 30) and (mes == 6):
                            global mes, dia, ano
                            #global dia
                            dia = (dia + 7) - 30
                            mes = mes + 1
                            nueva_fecha = datetime.datetime(ano, mes, dia, fecha.hour, fecha.minute, 00, 000000)
                        elif ((dia + 7) > 30) and (mes == 9):
                            global mes, dia, ano
                            #global dia
                            dia = (dia + 7) - 30
                            mes = mes + 1
                            nueva_fecha = datetime.datetime(ano, mes, dia, fecha.hour, fecha.minute, 00, 000000)
                        elif ((dia + 7) > 30) and (mes == 11):
                            global mes, dia, ano
                            #global dia
                            dia = (dia + 7) - 30
                            mes = mes + 1
                            nueva_fecha = datetime.datetime(ano, mes, dia, fecha.hour, fecha.minute, 00, 000000)
                        elif ((dia + 7) > 28) and (mes == 2): 
                            global mes, dia, ano
                            #global dia
                            dia = (dia + 7) - 28
                            mes = mes + 1
                            nueva_fecha = datetime.datetime(ano, mes, dia, fecha.hour, fecha.minute, 00, 000000)
                        else:
                            global dia
                            dia = dia + 7
                            nueva_fecha = datetime.datetime(ano, mes, dia, fecha.hour, fecha.minute, 00, 000000)
                            
                        objetoi = Clases()
                        objetoi.curso=objeto.curso

                        objetoi.nombre="Sesion"+str(objeto.nombre)
                        objetoi.fecha_inicio=nueva_fecha
                        objetoi.duracion=objeto.duracion
                        objetoi.descripcion=objeto.descripcion
                        #objetoi.tipo=objeto.tipo
                        objetoi.save()
                
                if repetir == "3":

                    meses_entre_anos = 0

                    if((int(repetir_hasta.year)-int(fecha.year))>0):

                        global meses_entre_anos
                        meses_entre_anos = (int(repetir_hasta.year)-int(fecha.year))*12
                        #print "meses entre anos "+str(meses_entre_anos)
                    
                    else:
                        global meses_entre_anos
                        #print "no hay entre anos"
                        meses_entre_anos=0


                    numero_meses = ((12 - int(fecha.month))+meses_entre_anos) - (12 - int(repetir_hasta.month)) + 1

                    global numero_meses

                    for i in range(1, numero_meses ):
                        if mes == 12:
                            global mes, ano
                            mes = (mes + 1)-12
                            ano = ano + 1
                            nueva_fecha = datetime.datetime(ano, mes, dia, fecha.hour, fecha.minute, 00, 000000)
                           
                        else:
                            global mes, ano
                            mes = mes + 1
                            nueva_fecha = datetime.datetime(ano, mes, dia, fecha.hour, fecha.minute, 00, 000000)
                            
                        objetoi = Clases()
                        objetoi.curso=objeto.curso
                        objetoi.nombre="Sesion"+str(objeto.nombre)
                        objetoi.fecha_inicio=nueva_fecha
                        objetoi.duracion=objeto.duracion
                        objetoi.descripcion=objeto.descripcion
                        #objetoi.tipo=objeto.tipo
                        objetoi.save()



            return redirect('cronograma_diplomado')
    else:
        form = EventosDiplomadoForm() 

    eventos = Clases.objects.all()
    events = []
    for i in eventos:
        inicio = i.fecha_inicio
        #fin = i.fecha_finalizacion

        hora_inicio = [i.fecha_inicio.hour, i.fecha_inicio.minute, 0]
        #hora_finalizacion = [i.fecha_finalizacion.hour, i.fecha_finalizacion.minute, 0]
        hora_finalizacion = [i.fecha_inicio.hour + i.duracion, i.fecha_inicio.minute, 0]

        diasTotal = 0
        
        #diasEvento = 1
        diasEvento = []
        for j in range(0, diasTotal+1):
            aux = inicio + timedelta(days = j)
            diasEvento.append([aux.year, aux.month-1, aux.day])

        events.append({
            'id': i.id,
            'nombre': i.nombre,
            'descripcion': i.descripcion,
            'hora_inicio': hora_inicio,
            'hora_finalizacion': hora_finalizacion,
            'diasEvento': diasEvento,
            
        })
    
    return render(request, 'diplomado.html', {
        'formDiplomado': form,
        'eventos': json.dumps(events),
        'user_group': user_group(request),
        'opcion_menu': 3,
    })

def diplomado_modificar(request):

    grupo = user_group(request)
    if grupo == None:
        return redirect('home')

    idCurso = request.GET.get('idCurso')
    curso = Clases.objects.filter(id=idCurso)[0]
    
    if request.method == 'POST':

        get = request.POST['boton']
        
        if get == "0":

            form = EventosDiplomadoForm(request.POST, instance=curso)
            if form.is_valid():
                objeto = form.save()
                objeto.save()
                return redirect('cronograma_diplomado')

        if get == "1":
            form = EventosDiplomadoForm(instance=curso)

        if get == "2":
            idCurso = request.GET.get('idCurso')
            curso = Clases.objects.filter(id=idCurso)[0]
            curso.delete()
            return redirect('cronograma_diplomado')
    else:
        form = EventosDiplomadoForm(instance=curso)

    var = curso.id

    return render(request, 'diplomado_modificar.html', {
        'form': form, 
        'user_group': user_group(request),
        'opcion_menu': 3, 'curso': var
    })

def acompanamiento_modificar(request):

    grupo = user_group(request)
    if grupo == None:
        return redirect('home')

    idCurso = request.GET.get('idCurso')
    curso = AcompanamientoInSitus.objects.filter(id=idCurso)[0]
    if request.method == 'POST':

        get = request.POST['boton']
        
        if get == "0":

            form = EventosAcompanamientoForm(request.POST, instance=curso)
            if form.is_valid():
                objeto = form.save()
                objeto.save()
                return redirect('cronograma_acompanamiento')

        if get == "1":
            form = EventosAcompanamientoForm(instance=curso)

        if get == "2":
            idCurso = request.GET.get('idCurso')
            curso = AcompanamientoInSitus.objects.filter(id=idCurso)[0]
            curso.delete()
            return redirect('cronograma_acompanamiento')
    else:
        form = EventosAcompanamientoForm(instance=curso)

    return render(request, 'acompanamiento_modificar.html', {
        'form': form, 
        'user_group': user_group(request),
        'opcion_menu': 4,
        'curso':idCurso
    })

def subirsoportes(request):

    grupo = user_group(request)
    if grupo == None:
        return redirect('home')

    identificador = request.GET['v']
    clase = Clases.objects.get(id=identificador)

    if request.method == 'POST':
        
        form = DocumentosSoporteForm(request.POST, request.FILES)
        
        if form.is_valid():
            obj = form.save(commit=False)
            obj.clase = clase
            obj.save()
            
            return redirect('cronograma_diplomado')

    else:
        

        form = DocumentosSoporteForm()

        
    return render(request, 'diplomado_soportes.html', {
        'form': form,
        'user_group': user_group(request),
        'opcion_menu': 3,
        'clase' : clase.id,
    })

def subirsoportesacompanamiento(request):

    grupo = user_group(request)
    if grupo == None:
        return redirect('home')

    identificador = request.GET['v']
    acompanamiento= AcompanamientoInSitus.objects.get(id=identificador)

    if request.method == 'POST':
       
        form = DocumentosSoporteAcompanamientoForm(request.POST, request.FILES)
        
        if form.is_valid():
            obj = form.save(commit=False)
            obj.acompanamiento = acompanamiento
            obj.save()
            
            return redirect('cronograma_acompanamiento')

    else:
        
        form = DocumentosSoporteAcompanamientoForm()

        
    return render(request, 'diplomado_soportes.html', {
        'form': form,
        'user_group': user_group(request),
        'opcion_menu': 4,
    })

def curso(request):

    grupo = user_group(request)
    if grupo == None:
        return redirect('home')

    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            objeto = form.save()
            
            return redirect('gestion_cursos')
    else :
        form = CursoForm()

    return render(request, 'curso.html', {
        'form': form,
        'user_group': user_group(request),
        'opcion_menu': 5,
    })

def formador(request):

    grupo = user_group(request)
    if grupo == None:
        return redirect('home')

    if request.method == 'POST':
        form = FormadorForm(request.POST)
        if form.is_valid():
            objeto = form.save()
            
            return redirect('home')
    else :
        form = FormadorForm()

    return render(request, 'formador.html', {
        'form': form,
        'user_group': user_group(request),
        'opcion_menu': 5,
    })

def reporte_cursos(request, limit=100):
    curso_list = Cursos.objects.all() 
    #estudiante_list = [curso_list.lenght]
    #estudiante_list = curso_list[0].estudiantes.all()
    #estudiante_list = [curso_list.lenght]
    #for i in range(0, curso_list.lenght - 1 ):
    #    estudiante_list[i] = curso_list[i].estudiantes.all()
             
    
    return render(request, 'gestion.html', {'curso_list': curso_list,  'user_group': user_group(request),
        'opcion_menu': 5, },
        )

def reporte_formadores(request, limit=100):
    formador_list = Formador.objects.all() 
    #estudiante_list = [curso_list.lenght]
    #estudiante_list = curso_list[0].estudiantes.all()
    #estudiante_list = [curso_list.lenght]
    #for i in range(0, curso_list.lenght - 1 ):
    #    estudiante_list[i] = curso_list[i].estudiantes.all()
             
    
    return render(request, 'gestion_formador.html', {'formador_list': formador_list,  'user_group': user_group(request),
        'opcion_menu': 5, },
        )
def lista_estudiantes(request, id):
    grupo = user_group(request)
    if grupo == None:
        return redirect('home')

    clase = Clases.objects.get(id=id)
    curso = clase.curso
    clasenombre = clase.nombre
    cursonombre = curso.descripcion
    estudiante_list = curso.estudiantes.all()
    
    return render(request, 'lista_estudiantes.html', {'estudiante_list': estudiante_list,  'user_group': user_group(request),
        'opcion_menu': 5, 'curso':cursonombre, 'clase':clasenombre},
        )
'''
def detalle_curso(request, id, limit=100):

    curso = Cursos.objects.get(id=id)
    estudiante_list = curso.estudiantes.all()
    
    return render(request, 'detalles_curso.html', { 'user_group': user_group(request),
        'opcion_menu': 5, 'curso':curso, 'estudiante_list':estudiante_list},
        )'''

def detalle_curso(request, id):

    grupo = user_group(request)
    if grupo == None:
        return redirect('home')

    curso = Cursos.objects.get(id=id)


    if request.method == 'POST':

        get = request.POST['boton']
        print "!!!!!!!!!!!!!!!!"+str(get)
        
        if get == "0":

            form = CursoForm(request.POST, instance=curso)
            if form.is_valid():
                objeto = form.save()
                objeto.save()
                return redirect('gestion_cursos')

        if get == "2":
            form = CursoForm(instance=curso)

        if get == "1":
            curso = Cursos.objects.get(id=id)
            curso.delete()
            return redirect('gestion_cursos')
    else:
        form = CursoForm(instance=curso)

    return render(request, 'detalles_curso.html', {
        'form': form, 
        'user_group': user_group(request),
        'opcion_menu': 4,
    })

def detalle_formador(request, id):

    grupo = user_group(request)
    if grupo == None:
        return redirect('home')

    curso = Formador.objects.get(id=id)


    if request.method == 'POST':

        get = request.POST['boton']
        
        
        if get == "0":

            form = FormadorForm(request.POST, instance=curso)
            if form.is_valid():
                objeto = form.save()
                objeto.save()
                return redirect('gestion_formador')

        if get == "2":
            form = FormadorForm(instance=curso)

        if get == "1":
            formador = Formador.objects.get(id=id)
            print "!!!!!!!!!!!!!!!!!!"+str(formador.nombre1)
            formador.delete()
            return redirect('gestion_cursos')
    else:
        form = FormadorForm(instance=curso)

    return render(request, 'detalles_formador.html', {
        'form': form, 
        'user_group': user_group(request),
        'opcion_menu': 4,
    })

def actividad(request, id):

    grupo = user_group(request)
    if grupo == None:
        return redirect('home')

    clase = Clases.objects.get(id=id)
    curso = clase.curso
    #clase = Clases.objects.get(id=cursoid)
    estudiante_list = curso.estudiantes.all()

    if request.method == 'POST':
        form = ActividadForm(request.POST)
        if form.is_valid():
            print "es valido"
            objeto = form.save(commit=False)
            objeto.clase = clase
            objeto.save()
            
            return redirect('gestion_cursos')
    else :
        form = ActividadForm()
        print " no es valido"

    return render(request, 'actividadesyasistencia.html', {
        'form': form,
        'user_group': user_group(request),
        'opcion_menu': 5,
        'estudiante_list':estudiante_list,
    })

def cancelar_clase_acompanamiento(request, id):
    grupo = user_group(request)
    if grupo == None:
        return redirect('home')

    postFormatoDict = request.POST.dict() #obtuvimos el post
    post = str(postFormatoDict)

    motivos = ""
    if "motivos" in post:
        global motivos
        motivos = request.POST['motivos']
                   
        clase = AcompanamientoInSitus.objects.get(id=id)
        clase.nombre = "CANCELADA "+clase.nombre
        clase.descripcion = motivos + clase.descripcion
        clase.estado = False
        clase.save()
        return redirect('cronograma_acompanamiento')
    
    return render(request, 'cancelarsesion.html', {'user_group': user_group(request),
        'opcion_menu': 5,},
        )

def cancelar_clase_diplomado(request, id):
    grupo = user_group(request)
    if grupo == None:
        return redirect('home')

    postFormatoDict = request.POST.dict() #obtuvimos el post
    post = str(postFormatoDict)

    motivos = ""
    if "motivos" in post:
        global motivos
        motivos = request.POST['motivos']
                   
        clase = Clases.objects.get(id=id)
        clase.nombre = "CANCELADA "+clase.nombre
        clase.descripcion = motivos 
        clase.estado = False
        clase.save()
        return redirect('cronograma_diplomado')
    
    return render(request, 'cancelarsesion.html', {'user_group': user_group(request),
        'opcion_menu': 5,},
        )

def gestion(request):
    grupo = user_group(request)
    if grupo == None:
        return redirect('home')

    curso_list = Cursos.objects.all()
    formador_list = Formador.objects.all()
    
    return render(request, 'contenidogestion.html', {'user_group': user_group(request),
        'opcion_menu': 5, 'curso_list':curso_list, 'formador_list': formador_list,},
        )


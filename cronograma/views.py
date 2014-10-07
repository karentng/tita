from django.shortcuts import render
from cronograma.forms import EventosAcompanamientoForm, EventosDiplomadoForm
from campus.models import Clase
import json
from django.shortcuts import redirect, render, render_to_response
from datetime import datetime, date, timedelta
from math import ceil
import datetime 

def cronograma(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = EventosAcompanamientoForm(request.POST)
                
        if form.is_valid():
            objeto = Clase()
            objeto = form.save()

            objeto.tipo = "2"
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
                            
                        objetoi = Clase()
                        objetoi.institucion=objeto.institucion
                        objetoi.nombre=objeto.nombre
                        objetoi.fecha_inicio=nueva_fecha
                        objetoi.duracion=objeto.duracion
                        objetoi.descripcion=objeto.descripcion
                        objetoi.tipo=objeto.tipo
                        objetoi.save()
                                                   

                if repetir == "2":
                    for i in range(1, int((repetir_hasta - fecha).days + 2)/7):
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
                            
                        objetoi = Clase()
                        objetoi.institucion=objeto.institucion
                        objetoi.nombre=objeto.nombre
                        objetoi.fecha_inicio=nueva_fecha
                        objetoi.duracion=objeto.duracion
                        objetoi.descripcion=objeto.descripcion
                        objetoi.tipo=objeto.tipo
                        objetoi.save()
                
                if repetir == "3":

                    meses_entre_anos = 0

                    if((int(repetir_hasta.year)-int(fecha.year))>0):
                        global meses_entre_anos
                        meses_entre_anos = (int(repetir_hasta.year)-int(fecha.year))*12
                    
                    else:
                        global meses_entre_anos
                        meses_entre_anos=0


                    numero_meses = ((12 - int(fecha.month))+meses_entre_anos) - (12 - int(repetir_hasta.month))

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
                            
                        objetoi = Clase()
                        objetoi.institucion=objeto.institucion
                        objetoi.nombre=objeto.nombre
                        objetoi.fecha_inicio=nueva_fecha
                        objetoi.duracion=objeto.duracion
                        objetoi.descripcion=objeto.descripcion
                        objetoi.tipo=objeto.tipo
                        objetoi.save()

            
            

            return redirect('cronograma_acompanamiento')
    else:

        form = EventosAcompanamientoForm()

    eventos = Clase.objects.filter(tipo="2")

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
            'institucion': i.get_institucion_display()
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
        'eventos': json.dumps(events)
    })



def menor10(val):
    if val < 10:
        return "0"+str(val)
    return str(val)


def diplomado(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = EventosDiplomadoForm(request.POST)
        if form.is_valid():
            objeto = Clase()
            
            objeto = form.save()
            
            objeto.tipo = "1"
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
                            
                        objetoi = Clase()
                        objetoi.institucion=objeto.institucion
                        objetoi.nombre=objeto.nombre
                        objetoi.fecha_inicio=nueva_fecha
                        objetoi.duracion=objeto.duracion
                        objetoi.descripcion=objeto.descripcion
                        objetoi.tipo=objeto.tipo
                        objetoi.save()
                                                   

                if repetir == "2":
                    for i in range(1, int((repetir_hasta - fecha).days + 2)/7):
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
                            
                        objetoi = Clase()
                        objetoi.institucion=objeto.institucion
                        objetoi.nombre=objeto.nombre
                        objetoi.fecha_inicio=nueva_fecha
                        objetoi.duracion=objeto.duracion
                        objetoi.descripcion=objeto.descripcion
                        objetoi.tipo=objeto.tipo
                        objetoi.save()
                
                if repetir == "3":

                    meses_entre_anos = 0

                    if((int(repetir_hasta.year)-int(fecha.year))>0):

                        global meses_entre_anos
                        meses_entre_anos = (int(repetir_hasta.year)-int(fecha.year))*12
                        print "meses entre anos "+str(meses_entre_anos)
                    
                    else:
                        global meses_entre_anos
                        print "no hay entre anos"
                        meses_entre_anos=0


                    numero_meses = ((12 - int(fecha.month))+meses_entre_anos) - (12 - int(repetir_hasta.month))

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
                            
                        objetoi = Clase()
                        objetoi.institucion=objeto.institucion
                        objetoi.nombre=objeto.nombre
                        objetoi.fecha_inicio=nueva_fecha
                        objetoi.duracion=objeto.duracion
                        objetoi.descripcion=objeto.descripcion
                        objetoi.tipo=objeto.tipo
                        objetoi.save()



            return redirect('cronograma_diplomado')
    else:
        form = EventosDiplomadoForm() 

    eventos = Clase.objects.filter(tipo="1")
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
            'institucion': i.get_institucion_display()
        })
    
    return render(request, 'diplomado.html', {
        'formDiplomado': form,
        'eventos': json.dumps(events)
    })

def diplomado_modificar(request):

    idCurso = request.GET.get('idCurso')
    curso = Clase.objects.filter(id=idCurso)[0]
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
            curso = Clase.objects.filter(id=idCurso)[0]
            curso.delete()
            return redirect('cronograma_diplomado')
    else:
        form = EventosDiplomadoForm(instance=curso)

    return render(request, 'diplomado_modificar.html', {
        'form': form, 
    })

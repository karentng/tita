#encoding: utf-8
from django.shortcuts import render
from cronograma.forms import *
from campus.forms import ActividadForm, AsistenciaForm
from campus.models import Clases, AcompanamientoInSitus, Estudiante, Cursos
import json
from django.shortcuts import redirect, render, render_to_response
from datetime import datetime, date, timedelta
from math import ceil
import datetime 
from campus.views import user_group
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404

def cronograma(request):
    # if this is a POST request we need to process the form data
    grupo = user_group(request)

    if grupo == None:
        return redirect('home')

    if grupo == "Formador":
        username = request.user
        formador = Formador.objects.get(usuario=username.id)
        curso = Cursos.objects.get(formador=formador.id)
        
        eventos = AcompanamientoInSitus.objects.filter(curso=curso)

    if grupo == "Coordinador":
        eventos = AcompanamientoInSitus.objects.all()

    if request.method == 'POST':
        form = EventosAcompanamientoForm(request.POST)
                
        if form.is_valid():
            objeto = AcompanamientoInSitus()
            objeto = form.save(commit=False)
            

            postFormatoDict = request.POST.dict() #obtuvimos el post
            post = str(postFormatoDict)

            repetir_hasta = datetime.datetime.now()

            contador = 1                
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
                        global contador
                        contador = contador + 1
                        objetoi.nombre=str(objeto.nombre)+ " "+ str(contador)
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
                        global contador
                        contador = contador + 1
                        objetoi.nombre=str(objeto.nombre)+ " "+ str(contador)
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
                        global contador
                        contador = contador + 1
                        objetoi.nombre=str(objeto.nombre)+ " "+ str(contador)
                        objetoi.fecha_inicio=nueva_fecha
                        objetoi.duracion=objeto.duracion
                        objetoi.descripcion=objeto.descripcion
                        
                        objetoi.save()

            
            objeto.nombre=(objeto.nombre)+" 1"
            #objeto.tipo = "2"
            objeto.save()

            return redirect('cronograma_acompanamiento')
    else:

        form = EventosAcompanamientoForm(initial={'nombre': 'Visita'})


    

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

        cursovar = Cursos.objects.get(id=i.curso.id)
        cursos = str(cursovar.descripcion)

        events.append({
            'id': i.id,
            'nombre': i.nombre,
            'curso': i.curso.descripcion,
            #'institucion': i.institucion,
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

            
            objeto = form.save(commit=False)
           

            postFormatoDict = request.POST.dict() #obtuvimos el post
            post = str(postFormatoDict)

            repetir_hasta = datetime.datetime.now()

            contador = 1     
                
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
                        global contador
                        contador = contador + 1
                        objetoi.nombre=str(objeto.nombre)+ " "+ str(contador)
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

                        global contador
                        contador = contador + 1
                        objetoi.nombre=str(objeto.nombre)+ " "+ str(contador)
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
                        global contador
                        contador = contador + 1
                        objetoi.nombre=str(objeto.nombre)+ " "+ str(contador)
                        objetoi.fecha_inicio=nueva_fecha
                        objetoi.duracion=objeto.duracion
                        objetoi.descripcion=objeto.descripcion
                        #objetoi.tipo=objeto.tipo
                        objetoi.save()


            objeto.nombre = str(objeto.nombre) + " 1"
            #objeto.tipo = "1"
            objeto.save()
            return redirect('cronograma_diplomado')
    else:
        form = EventosDiplomadoForm(initial={'nombre': 'Sesion'}) 

    eventos = Clases.objects.all()
    #
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

        cursovar = Cursos.objects.get(id=i.curso.id)
        cursos = str(cursovar.descripcion)
        

        events.append({
            'id': i.id,
            'nombre': i.nombre,
            #'curso': i.curso,
            #'institucion': i.institucion,
            'descripcion': cursos,
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

            form = EventosDiplomadoMForm(request.POST, instance=curso)
            if form.is_valid():
                objeto = form.save()
                objeto.save()
                return redirect('cronograma_diplomado')

        if get == "1":
            form = EventosDiplomadoMForm(instance=curso)

        if get == "2":
            idCurso = request.GET.get('idCurso')
            curso = Clases.objects.filter(id=idCurso)[0]
            curso.delete()
            return redirect('cronograma_diplomado')
    else:
        form = EventosDiplomadoMForm(instance=curso)

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

            form = EventosAcompanamientoMForm(request.POST, instance=curso)
            if form.is_valid():
                objeto = form.save()
                objeto.save()
                return redirect('cronograma_acompanamiento')

        if get == "1":
            form = EventosAcompanamientoMForm(instance=curso)

        if get == "2":
            idCurso = request.GET.get('idCurso')
            curso = AcompanamientoInSitus.objects.filter(id=idCurso)[0]
            curso.delete()
            return redirect('cronograma_acompanamiento')
    else:
        form = EventosAcompanamientoMForm(instance=curso)

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
    curso = clase.curso

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
        'curso' : curso.id,
    })

def subirsoportesacompanamiento(request):

    grupo = user_group(request)
    if grupo == None:
        return redirect('home')

    identificador = request.GET['v']
    acompanamiento= AcompanamientoInSitus.objects.get(id=identificador)
    curso = acompanamiento.curso

    if request.method == 'POST':
       
        form = DocumentosSoporteAcompanamientoForm(request.POST, request.FILES)
        
        if form.is_valid():
            obj = form.save(commit=False)
            obj.acompanamiento = acompanamiento
            obj.save()
            
            return redirect('cronograma_acompanamiento')

    else:
        
        form = DocumentosSoporteAcompanamientoForm()

        
    return render(request, 'cronograma_soportes.html', {
        'form': form,
        'user_group': user_group(request),
        'opcion_menu': 4,
        'clase' : acompanamiento.id,
        'curso' : curso.id,
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
def lista_acompanamiento(request, id):
    grupo = user_group(request)
    if grupo == None:
        return redirect('home')

    clase = AcompanamientoInSitus.objects.get(id=id)
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
    #
    clase = get_object_or_404(Clases, id=id)
    curso = clase.curso
    estudiante_list = curso.estudiantes.all()

    grupo = user_group(request)
    if grupo == None:
        return redirect('home')

    if request.method == 'POST':
        
        form = ActividadForm(request.POST)
        
        if form.is_valid():
            obj = form.save(commit=False)
            obj.clase = clase
            obj.save()
            
            return redirect('actividades.html')

    else:        

        form = ActividadForm()

    return render(request, 'actividadesyasistencia.html', {
        'clase':clase.id,
        'curso': curso.id,
        'form': form,
        'user_group': user_group(request),
        'opcion_menu': 5,
        'estudiante_list':estudiante_list

        
    })

def actividadacompanamiento(request, id):
    #
    clase = get_object_or_404(AcompanamientoInSitus, id=id)
    curso = clase.curso
    estudiante_list = curso.estudiantes.all()

    grupo = user_group(request)
    if grupo == None:
        return redirect('home')

    if request.method == 'POST':
        
        form = ActividadForm(request.POST)
        
        if form.is_valid():
            obj = form.save(commit=False)
            obj.clase = clase
            obj.save()
            
            return redirect('actividades.html')

    else:        

        form = ActividadForm()

    return render(request, 'actividadesyasistencia.html', {
        'clase':clase.id,
        'curso': curso.id,
        'form': form,
        'user_group': user_group(request),
        'opcion_menu': 5,
        'estudiante_list':estudiante_list

        
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
        'user_group': user_group(request),
        'opcion_menu': 5,
        #'soportesFormset' : soportesFormset,
    })

def asistencia_acompanamiento(request, curso_id, clase_id):
    curso = get_object_or_404(Cursos, id=curso_id)
    clase = get_object_or_404(AcompanamientoInSitus, id=clase_id)

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

    return render(request, 'asistencia_acompanamiento.html', {
        'clase':clase,
        'curso': curso,
        'form': form,
        'user_group': user_group(request),
        'opcion_menu': 5,
        #'soportesFormset' : soportesFormset,
    })


# encoding: utf-8
from django.shortcuts import render, redirect
import csv
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core import urlresolvers
from django.contrib import messages
import datetime
from survey.models import *

#import settings

from models import Question, Survey, Category
from forms import ResponseForm, CodigoEncuestaForm

def codigo_encuesta_session(request):
    codigo = request.session.get('codigo_encuesta')
    if not codigo:
        return None
    return codigo

def codigo_encuesta(request):
    print(request)
    codigo = codigo_encuesta_session(request)
    if codigo:
        return redirect('encuesta_nuevo_estudiante')
    mensaje = ""
    if request.method == 'POST':
        form = CodigoEncuestaForm(request.POST)
        if form.is_valid():
            clave = form.cleaned_data['registro']
            if clave == '98765234567': # clave de acceso
                request.session['codigo_encuesta']=clave
                return redirect('encuesta_nuevo_estudiante')
            if clave == '98765234566': # clave de acceso
                request.session['codigo_encuesta']=clave
                return redirect('encuesta_nuevo_padre')
            if clave == '98765234565': # clave de acceso
                request.session['codigo_encuesta']=clave
                return redirect('encuesta_nuevo_maestro')
            else :
                mensaje = "Código inválido"
    else:
        form = CodigoEncuestaForm()

    return render(request, 'codigo_encuestas.html', {
        'mensaje':mensaje,
        'form' : form
    })

def encuesta_padre(request):
    codigo = codigo_encuesta_session(request)
    if not codigo:
        return codigo_encuesta(request)

    survey = Survey.objects.get(id=1)

    if request.method == 'POST':
        form = ResponseForm(request.POST, survey=survey)
        if form.is_valid():
            form.save()
            return redirect('encuesta_finalizada')
        else:
            print "error llenando", form.errors
    else :
        form = ResponseForm(survey=survey)

    # customizar form de acuerdo a la encuesta para padres
    #form.fields['jornada'].label = u"1. Jornada en la que estudia su hijo(a)"
    #form.fields['nombre'].label = u"3. Nombre(s) y apellidos del padre de familia o acudiente"
    #form.fields['institucion'].label = u"5. Nombre de la institución educativa en la que estudia su hijo(a)"

    camposMaterias = [form['question_13%02d'%x] for x in xrange(1,20) ]
    camposDispositivos = [form['question_%d'%x] for x in xrange(23,27) ]
    camposUsos = [form['question_29%02d'%x] for x in xrange(1,20)]
    camposHerramientas = [form['question_19%02d'%x] for x in xrange(1,15) ]

    return render(request, 'encuesta_padre.html', {
        'form': form,

        'camposMaterias1': camposMaterias[:10],
        'camposMaterias2': camposMaterias[10:],
        'camposDispositivos1': camposDispositivos[:2],
        'camposDispositivos2': camposDispositivos[2:],
        'camposHerramientas1' : camposHerramientas[:7],
        'camposHerramientas2' : camposHerramientas[7:],
        'camposUsos1' : camposUsos[:10],
        'camposUsos2' : camposUsos[10:]
    })


def encuesta_docente(request):
    codigo = codigo_encuesta_session(request)
    if not codigo:
        return codigo_encuesta(request)
    survey = Survey.objects.get(id=2)
    category_items = list(survey.category_set.all())

    if request.method == 'POST':
        form = ResponseForm(request.POST, survey=survey)
        if form.is_valid():
            form.save()
            return redirect('encuesta_finalizada')
        else:
            print "error llenando", form.errors
    else :
        form = ResponseForm(survey=survey)


    # customizar form de acuerdo a la encuesta para padres
    #form.fields['jornada'].label = u"1. Jornada en la que enseñas"
    #form.fields['institucion'].label = u"2. Nombre de tu institución educativa"
    #form.fields['nombre'].label = u"3. Nombre y apellidos"


    camposMaterias = [form['question_09%02d'%x] for x in xrange(1,20) ]
    camposHerramientas = [form['question_15%02d'%x] for x in xrange(1,30) ]
    camposDispositivos = [form['question_%02d'%x] for x in xrange(25,29) ]
    camposUsos = [form['question_31%02d'%x] for x in xrange(1,21) ]

    return render(request, 'encuesta_docente.html', {
        'form': form,
        'camposMaterias1': camposMaterias[:10],
        'camposMaterias2': camposMaterias[10:],
        'camposHerramientas1': camposHerramientas[:14],
        'camposHerramientas2': camposHerramientas[14:],
        'camposDispositivos1': camposDispositivos[:2],
        'camposDispositivos2': camposDispositivos[2:],
        'camposUsos1': camposUsos[:10],
        'camposUsos2': camposUsos[10:]
    })

def encuesta_estudiante(request):
    codigo = codigo_encuesta_session(request)
    if not codigo:
        return codigo_encuesta(request)
    survey = Survey.objects.get(id=3)
    category_items = list(survey.category_set.all())

    if request.method == 'POST':
        form = ResponseForm(request.POST, survey=survey)
        if form.is_valid():
            form.save()
            return redirect('encuesta_finalizada')
        else:
            print "error llenando", form.errors
    else :
        form = ResponseForm(survey=survey)

    # customizar form de acuerdo a la encuesta para padres

    camposMaterias = [form['question_13%02d'%x] for x in xrange(1,20) ]
    camposRecursos = [form['question_18%02d'%x] for x in xrange(1,8) ]
    camposDispositivos = [form['question_2%0d'%x] for x in xrange(2,6) ]
    camposInternet = [form['question_28%02d'%x] for x in xrange(1,19) ]

    return render(request, 'encuesta_estudiante.html', {
        'form': form,
        'camposMaterias1': camposMaterias[:10],
        'camposMaterias2': camposMaterias[10:],
        'camposRecursos1': camposRecursos[:4],
        'camposRecursos2': camposRecursos[4:],
        'camposDispositivos1': camposDispositivos[:2],
        'camposDispositivos2': camposDispositivos[2:],
        'camposInternet1': camposInternet[:9],
        'camposInternet2': camposInternet[9:]
    })

def encuesta_nuevo_estudiante(request):
    codigo = codigo_encuesta_session(request)
    if not codigo:
        return codigo_encuesta(request)
    survey = Survey.objects.get(id=4)
    category_items = list(survey.category_set.all())

    if request.method == 'POST':
        form = ResponseForm(request.POST, survey=survey)
        if form.is_valid():
            form.save()
            return redirect('encuesta_finalizada')
        else:
            print "error llenando", form.errors
    else :
        form = ResponseForm(survey=survey)


    camposMaterias = [form['question_13%02d'%x] for x in xrange(1,9) ]
    camposRecursos = [form['question_15%02d'%x] for x in xrange(1,8) ]

    return render(request, 'encuesta_nuevo_estudiante.html', {
        'form': form,
        'camposMaterias1': camposMaterias[:4],
        'camposMaterias2': camposMaterias[4:],
        'camposRecursos1': camposRecursos[:4],
        'camposRecursos2': camposRecursos[4:]
    })

def encuesta_nuevo_maestro(request):
    codigo = codigo_encuesta_session(request)
    if not codigo:
        return codigo_encuesta(request)
    survey = Survey.objects.get(id=5)
    category_items = list(survey.category_set.all())

    if request.method == 'POST':
        form = ResponseForm(request.POST, survey=survey)
        if form.is_valid():
            form.save()
            return redirect('encuesta_finalizada')
        else:
            print "error llenando", form.errors
    else :
        form = ResponseForm(survey=survey)


    camposHerramientas = [form['question_25%02d'%x] for x in xrange(1,18) ]
    #camposDispositivos = [form['question_38%02d'%x] for x in xrange(1,9) ]

    return render(request, 'encuesta_nuevo_maestro.html', {
        'form': form,
        'camposHerramientas1': camposHerramientas[:9],
        'camposHerramientas2': camposHerramientas[9:]
    })

def encuesta_nuevo_padre(request):
    codigo = codigo_encuesta_session(request)
    if not codigo:
        return codigo_encuesta(request)
    survey = Survey.objects.get(id=6)
    category_items = list(survey.category_set.all())

    if request.method == 'POST':
        form = ResponseForm(request.POST, survey=survey)
        if form.is_valid():
            form.save()
            return redirect('encuesta_finalizada')
        else:
            print "error llenando", form.errors
    else :
        form = ResponseForm(survey=survey)


    camposMaterias = [form['question_18%02d'%x] for x in xrange(1,9) ]
    camposHerramientas = [form['question_26%02d'%x] for x in xrange(1,15) ]

    return render(request, 'encuesta_nuevo_padre.html', {
        'form': form,
        'camposMaterias1': camposMaterias[:4],
        'camposMaterias2': camposMaterias[4:],
        'camposHerramientas1': camposHerramientas[:7],
        'camposHerramientas2': camposHerramientas[7:],
    })

def reporte_encuesta(request, survey_id):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="reporte_encuesta.csv"'
    writer = csv.writer(response, delimiter=";")
    print "encuesta numero "+survey_id
    if survey_id==4:
        print "entro"
        writer.writerow(['ID','Fecha de Encuesta','Jornada','Nombre de tu institución educativa','Sus nombre(s) y apellidos:','¿Qué materias enseña?','Grados en los que enseña:', 'Edad:','Fecha de Nacimiento','Lugar de nacimiento:','Nombre del barrio donde reside actualmente:','¿Cuál es su máximo nivel educativo? Marque con una X su respuesta.','Título obtenido:','¿A qué área de formación corresponde su carrera de pregrado? Marque con una X su respuesta.','Otra. ¿Cuál?','¿Cuántos años lleva ejerciendo la docencia? Marque con una X su respuesta.','1. Actualmente ¿con qué frecuencia utiliza el computador? Marque con una X sólo una respuesta.','2. Actualmente ¿con qué frecuencia se conecta a Internet? Marque con una X sólo una respuesta.','3. ¿Qué opina sobre que sus estudiantes hagan las tareas con ayuda de Internet? Marque con una X sólo una respuesta.','4. Califique de 1 a 3 las materias que usted enseña según qué tanto le serviría utilizar Internet en cada una de ellas. Si cree que le serviría mucho marque 3, si cree que le serviría un poco marque 2 y si cree que le serviría muy poquito o nada marque 1.','Calificación','Nombre materia 2','Calificación','Nombre materia 3','Calificación','Nombre materia 4','Calificación','Nombre materia 5','Calificación','5. Frente al uso del computador y la Internet en mi trabajo… Marque con una X sólo una respuesta.','6. El computador y la Internet dispersan la atención de los estudiantes.','7. El computador y la Internet limitan la capacidad de creación de los estudiantes.','8. La Internet está perjudicando las capacidades de lectura y escritura de los estudiantes.','9. Justifique su respuesta a la pregunta anterior (No. 8). En esta pregunta debe explicar las razones por las que escogió una de las tres opciones de la pregunta 8.','10. ¿Le genera dificultades el uso del computador y la Internet? Marque con una X su respuesta.','11. Mencione las dificultades que tiene cuando usa computador e Internet:','12. ¿Usted se ha certificado en algún curso de formación en TIC? Marque con una X su respuesta.','¿Cuáles?','Si usted no se ha certificado en algún curso de formación en TIC, pero actualmente está realizando un curso de este tipo, mencione ¿Cuál(es)?','Procesador de texto (Apache OpenOffice Writer, LibreOffice Writer).','Bases de datos (MySQL, ORACLE, Microsoft Access).','Correo electrónico.','Hoja de cálculo (Microsoft Excel, Apache Open Office Calc, Spreadsheet de Google Drive).','Programas para hacer presentaciones (Microsoft Power Point, Prezi).','Programas de dibujo (Corel Draw, Adobe Flash, Microsoft Paint). ','Programas para editar imágenes y fotografías (Adobe Photoshop, GIMP)','Internet para realizar consultas generales.','Medios audiovisuales.','Internet para hacer actividades pedagógicas.','Plataforma virtual de aprendizaje.','Blog personal para interactuar con sus alumnos.','Sitios especializados en temas que le interesan.','Software especializado.','Utiliza el computador y la Internet para el diseño de proyectos de aula.','Diseña y emplea ambientes constructivos, críticos, reflexivos y colaborativos, apoyándose en el computador y la Internet.','Otra herramienta. ¿Cuál?','14. ¿En qué sitios se conecta a Internet? Marque con una X sus respuestas. Puede marcar varias opciones. ','15. En el último mes de trabajo ¿ha utilizado el computador en sus clases? Marque con una X su respuesta. ','16. ¿Qué tareas o trabajos les pone a hacer a sus estudiantes en Internet? Marque con una X sus respuestas.Puede marcar varias opciones. ','Otra actividad. ¿Cuál?','17. Si usted pertenece a algún grupo o red virtual en la que se aborden temas sobre el uso del computador y la Internet en la enseñanza y el aprendizaje, mencione en cuál(es):','18. ¿Qué actividades relacionadas con el uso del computador y la Internet en la enseñanza y el aprendizaje hace con otros profesores? ','19. ¿De qué manera usted investiga en Internet sobre un tema que le interesa para sus clases? Marque con una X su respuesta. Puede marcar varias opciones. ','Otra forma. ¿Cuál?','Computador','Lo uso para otra cosa. Mencione ¿cuál?','Internet','Lo uso para otra cosa. Mencione ¿cuál?','Tablet','Lo uso para otra cosa. Mencione ¿cuál?','Celular','Lo uso para otra cosa. Mencione ¿cuál?','Videojuegos','Lo uso para otra cosa. Mencione ¿cuál?','Cámara fotográfica digital','Lo uso para otra cosa. Mencione ¿cuál?','Cámara de video','Lo uso para otra cosa. Mencione ¿cuál?','Grabadora digital','Lo uso para otra cosa. Mencione ¿cuál?','DVD/Blue-ray','Lo uso para otra cosa. Mencione ¿cuál?','Televisor','Lo uso para otra cosa. Mencione ¿cuál?','Radio','Lo uso para otra cosa. Mencione ¿cuál?','Otro ','21. ¿A qué redes sociales pertenece? Marque con una X sus respuestas. Puede marcar varias opciones. ','Otra. ¿Cuál?','22. ¿Con quién comparte la información que encuentra en Internet? Marque con una X sus respuestas. Puede marcar varias opciones. ','23. ¿Con quién aprende a usar el computador y la Internet? Marque con una X sus respuestas. Puede marcar varias opciones.''Haciendo cursos. ¿Cuáles?','24. Cuando usa Internet ¿con quién prefiere hacerlo? Marque con una X sólo una respuesta.','25. ¿Qué le gustaría hacer o aprender a hacer con Internet? Marque con una X sus respuestas. Puede marcar varias opciones','Otra cosa. ¿Cuál?','Primer dispositivo que lamentaría','Segundo dispositivo que lamentaría','Tercer dispositivo que lamentaría','27. Suponiendo que el escenario descrito al inicio es real', '¿qué cree que sucedería con el desempeño y el comportamiento de sus estudiantes en clase? Marque con una X sólo una respuesta.','28. Suponiendo que el escenario descrito al inicio es real, ¿qué cree que sucedería con las tareas y responsabilidades de los profesores con los nuevos equipos? Marque con una X sólo una respuesta.','29. Suponiendo que el escenario descrito al inicio es real, ¿qué cree que sucedería con la comunicación entre los padres de familia y la institución educativa? Marque con una X sólo una respuesta.','30. ¿Le gustó responder esta encuesta en computador? Marque con una X su respuesta.'])


    respuestas = Response.objects.filter(survey_id=survey_id)

    for respuesta in respuestas: 
        item = respuesta.id, respuesta.created,         

        respuestas_radio = AnswerRadio.objects.filter(response_id=respuesta.id).select_related('question')
        respuestas_select = AnswerSelect.objects.filter(response_id=respuesta.id).select_related('question')
        respuestas_select_multiple = AnswerSelectMultiple.objects.filter(response_id=respuesta.id).select_related('question')
        respuestas_text = AnswerText.objects.filter(response_id=respuesta.id).select_related('question')

        respuestas_todas = list(respuestas_radio)+list(respuestas_select)+list(respuestas_select_multiple)+list(respuestas_text)
        respuestas_todas.sort(key = lambda res : res.question.number)

        for respuesta_todas in respuestas_todas:            
            if isinstance(respuesta_todas, AnswerSelectMultiple):
                valor =  "|".join(eval(respuesta_todas.body))
            else :
                valor = respuesta_todas.body
            
            item += (valor.encode('iso-8859-1'),)

        writer.writerow(item)
    return response
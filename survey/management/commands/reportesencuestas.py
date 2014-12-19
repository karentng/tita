# encoding:utf-8
from django.core.management.base import BaseCommand, CommandError
import csv
from django.http import HttpResponse
from survey.models import *
from django.db import connection


class Command(BaseCommand):
    def handle(self, *args, **options):
        survey_id = args[0]

        respuestas = Response.objects.filter(survey_id=survey_id)                       
        archivo = open("reporte_encuesta.csv","w") 
        writer = csv.writer(archivo, delimiter=';')
        contador = 0
        #print "nro respuestas", len(respuestas)
        #print "nro queries antes de iniciar", len(connection.queries)
        for respuesta in respuestas: 
            item = [respuesta.id, respuesta.created]        
            #print "oso", len(connection.queries)
            respuestas_radio = AnswerRadio.objects.filter(response_id=respuesta.id).select_related('question')
            respuestas_select = AnswerSelect.objects.filter(response_id=respuesta.id).select_related('question')
            respuestas_select_multiple = AnswerSelectMultiple.objects.filter(response_id=respuesta.id).select_related('question')
            respuestas_text = AnswerText.objects.filter(response_id=respuesta.id).select_related('question')
            
             
            respuestas_todas = list(respuestas_radio)+list(respuestas_select)+list(respuestas_select_multiple)+list(respuestas_text)
            #print "pinteta", len(connection.queries)
            respuestas_todas.sort(key = lambda res : res.question.number)
            #print "emico", len(connection.queries)

            for respuesta_todas in respuestas_todas:            
                if isinstance(respuesta_todas, AnswerSelectMultiple):
                    valor =  "|".join(eval(respuesta_todas.body))
                else :
                    valor = respuesta_todas.body
                
                item.append(valor.encode('iso-8859-1'))
            #print "osopeteno", len(connection.queries)

            writer.writerow(item)

            #print len(connection.queries)
            #raw_input('enter para continuar')
            #if True or contador%100==0:
            #    print len(connection.queries)

        #unicode(book.author).encode('iso-8859-1')

        #book.author.encode(....) String

        #aqui escribir las filas....


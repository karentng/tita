# encoding:utf-8
from django.core.management.base import BaseCommand, CommandError
import csv
from django.http import HttpResponse
from survey.models import *


class Command(BaseCommand):
    def handle(self, *args, **options):
        survey_id = args[0]

        respuestas = Response.objects.filter(survey_id=survey_id)                       
        archivo = open("salida.csv","w") 
        writer = csv.writer(archivo)

        for respuesta in respuestas: 
            item = respuesta.id, respuesta.created, respuesta.updated,          

            respuestas_radio = AnswerRadio.objects.filter(response_id=respuesta.id)
            respuestas_select = AnswerSelect.objects.filter(response_id=respuesta.id)
            respuestas_select_multiple = AnswerSelectMultiple.objects.filter(response_id=respuesta.id)
            respuestas_text = AnswerText.objects.filter(response_id=respuesta.id)

            respuestas_todas = list(respuestas_radio)+list(respuestas_select)+list(respuestas_select_multiple)+list(respuestas_text)
            respuestas_todas.sort(key = lambda res : res.question.number)

            for respuesta_todas in respuestas_todas:            
                if isinstance(respuesta_todas, AnswerSelectMultiple):
                    valor =  "|".join(eval(respuesta_todas.body))
                else :
                    valor = respuesta_todas.body
                
                item += (valor.encode('iso-8859-1'),)

            writer.writerow(item)

        #unicode(book.author).encode('iso-8859-1')

        #book.author.encode(....) String

        #aqui escribir las filas....


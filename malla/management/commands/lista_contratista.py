# encoding:utf-8
from django.core.management.base import BaseCommand, CommandError
from django.template import Template, Context
import smtplib
from malla.models import Requerimiento, Contratista, ContratistaInfoContacto, Lista
import csv

class Command(BaseCommand):
    def handle(self, *args, **options):
        archivo = open("ReporteListaContratistas.csv","w") 
        writer = csv.writer(archivo, delimiter=';')      

        requerimientos = Requerimiento.objects.all()

        string = ""
        arreglo = []

        arreglo.append("Nombres")
        arreglo.append("Apellidos")
        arreglo.append("No. Documento")
        arreglo.append("Celular")
        arreglo.append("Direccion".encode('latin-1'))
        
        for i in requerimientos:

            arreglo.append(i.descripcion_req.encode('latin-1'))

        arreglo.append("Total Horas")
        # columnas
        writer.writerow(arreglo)
             

        contratistas = Contratista.objects.all()
        for contratista in contratistas:

            nombres = str(contratista.nombre1) +" "+ str(contratista.nombre2)
            apellidos = str(contratista.apellido1) +" "+ str(contratista.apellido2)
            numero_doc = contratista.numero_documento

            celular = ContratistaInfoContacto.objects.get(monitor = contratista).celularppal
            direccion = contratista.direccion

            arreglo = []
            arreglo.append(nombres.encode('latin-1'))
            arreglo.append(apellidos.encode('latin-1'))
            arreglo.append(numero_doc)
            arreglo.append(celular)
            arreglo.append(direccion.encode('latin-1'))


            global requerimientos
            x = len(requerimientos)
            
            for i in requerimientos:
                try:
                    lista = Lista.objects.get(contratista=contratista,  requerimiento= i).horas
                    arreglo.append(lista)
                except:
                    lista = 0
                    arreglo.append(lista)
                    continue
            total = 0
            for i in range(5, len(arreglo)):
                total = int(arreglo[i])+total

            arreglo.append(total)           

            writer.writerow(arreglo)
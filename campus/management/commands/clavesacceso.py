# encoding:utf-8
from django.core.management.base import BaseCommand, CommandError
from django.template import Template, Context
import smtplib
from campus.models import Estudiante, Municipio, Cursos
from estudiante.models import InfoLaboral, FormacionAcademicaME, CertificacionTIC
from bilinguismo.models import Bilinguismo
import csv

class Command(BaseCommand):
    def handle(self, *args, **options):
        archivo = open("ClavesAcceso.csv","w") 
        writer = csv.writer(archivo, delimiter=';')
        writer.writerow(["Nombre Completo", "Clave de Acceso", "Cohorte"])

        aspirantes = Estudiante.objects.all().order_by('cohorte')
        for aspirante in aspirantes:

            nombre = aspirante
            clave = aspirante.numero_inscripcion()
            cohorte = aspirante.cohorte
            
            arreglo = [nombre, clave, cohorte]
            writer.writerow(arreglo)
        '''
        bilinguismo = Bilinguismo.objects.all()
        for aspirante in bilinguismo:

            nombre = aspirante
            clave = aspirante.numero_inscripcion()
            cohorte = "Bilinguismo"
            
            arreglo = [nombre, clave, cohorte]
            writer.writerow(arreglo)
        '''
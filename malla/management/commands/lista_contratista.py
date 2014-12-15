# encoding:utf-8
from django.core.management.base import BaseCommand, CommandError
from django.template import Template, Context
import smtplib
from campus.models import Estudiante, Municipio, Cursos
from estudiante.models import InfoLaboral, FormacionAcademicaME, CertificacionTIC
import csv

class Command(BaseCommand):
    def handle(self, *args, **options):
        archivo = open("ReporteListaContratistas.csv","w") 
        writer = csv.writer(archivo, delimiter=';')
        # columnas
        writer.writerow(["Grupos", "Nombre Completo", u"Cédula".encode('latin-1'),
            u"Género".encode('latin-1'), u"Correo Personal".encode('latin-1'), "Correo Institucional", "Municipio",
            u"Teléfono Fijo".encode('latin-1'), "Celular", u"Dirección".encode('latin-1'), "Nivel Educativo",
            u"Secretaría de Educación".encode('latin-1'),"Sede", "Cargo", "Zona", "Jornada", "Asignaturas",
            "Grados", "Decreto Docente", "Nombramiento", "Tipo Etnoeducador",
            u"Formación Académica".encode('latin-1'), "Certificaciones TIC"])

        aspirantes = Estudiante.objects.all()
        for aspirante in aspirantes:
            
            arreglo = ['campo1', 'campo2']
            writer.writerow(arreglo)
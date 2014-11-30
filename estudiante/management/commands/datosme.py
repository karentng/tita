# encoding:utf-8
from django.core.management.base import BaseCommand, CommandError
from django.template import Template, Context
import smtplib
from campus.models import Estudiante, Municipio
from estudiante.models import InfoLaboral
import csv

class Command(BaseCommand):
    def handle(self, *args, **options):
        archivo = open("MaestrosEstudiante.csv","w") 
        writer = csv.writer(archivo, delimiter=';')
        writer.writerow(["Nombre Completo", u"Cédula".encode('iso-8859-1'),
            u"Género".encode('iso-8859-1'), u"Correo Personal".encode('iso-8859-1'), "Correo Institucional", "Municipio",
            u"Teléfono Fijo".encode('iso-8859-1'), "Celular", u"Dirección".encode('iso-8859-1'), "Nivel Educativo",
            "Sede", "Cargo", "Zona", "Jornada"])

        aspirantes = Estudiante.objects.all()
        for aspirante in aspirantes:
            try:
                infoLaboral = InfoLaboral.objects.get(estudiante=aspirante)
            except Exception:
                continue
            nombre = aspirante
            num_doc = aspirante.numero_documento
            municipio = Municipio.objects.get(id=aspirante.municipio_id)

            sede = infoLaboral.get_sede_display().encode('iso-8859-1')
            cargo = infoLaboral.get_cargo_display().encode('iso-8859-1')
            zona = infoLaboral.get_zona_display().encode('iso-8859-1')
            jornada = infoLaboral.get_jornada_display().encode('iso-8859-1')
            
            arreglo = [nombre, num_doc, aspirante.sexo, aspirante.email, aspirante.email_institucional,
            municipio.nombre.encode('iso-8859-1'), aspirante.telefono, aspirante.celular,
            aspirante.direccion.encode('iso-8859-1'), aspirante.get_nivel_educativo_display().encode('iso-8859-1'),
            sede, cargo, zona, jornada]
            writer.writerow(arreglo)
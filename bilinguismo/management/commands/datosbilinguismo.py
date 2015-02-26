# encoding:utf-8
from django.core.management.base import BaseCommand, CommandError
from django.template import Template, Context
import smtplib
from bilinguismo.models import *
import csv

class Command(BaseCommand):
    def handle(self, *args, **options):
        archivo = open("InscritosBilinguismo.csv","w") 
        writer = csv.writer(archivo, delimiter=';')
        writer.writerow(["Terminado", "Nombre Completo", u"Cédula".encode('latin-1'), u"Género".encode('latin-1'),
            u"Correo Personal".encode('latin-1'), "Correo Institucional", "Municipio",
            u"Teléfono Fijo".encode('latin-1'), "Celular", u"Dirección".encode('latin-1'), "Nivel Educativo",
            "Sede", "Cargo", "Zona", "Jornada", "Asignaturas",
            "Grados", "Decreto Docente", "Nombramiento", "Tipo Etnoeducador",
            u"Formación Académica".encode('latin-1'), "Certificaciones Bilinguismo"])

        personas = Bilinguismo.objects.all()
        for aspirante in personas:
            try:
                infoLaboral = InfoLaboralBilinguismo.objects.get(persona=aspirante)
                sede = infoLaboral.get_institucion_display().encode('latin-1')
                cargo = infoLaboral.get_cargo_display().encode('latin-1')
                zona = infoLaboral.get_zona_display().encode('latin-1')
                jornada = infoLaboral.get_jornada_display().encode('latin-1')

                asigs = infoLaboral.asignaturas.all()
                asignaturas = ""
                for i in asigs:
                    asignaturas+= i.nombre.encode('latin-1')+" - "

                grads = infoLaboral.grados.all()
                grados = ""
                for i in grads:
                    grados+= i.nombre.encode('latin-1')+" - "

                decreto_docente = infoLaboral.get_decreto_docente_display().encode('latin-1')
                if infoLaboral.decreto_docente < 15:
                    decreto_docente+= " - "+"D.L 2277 de 1979"
                else:
                    decreto_docente+= " - "+"D.L 1278 de 2002"
            except Exception as e:
                sede = "---"
                cargo = "---"
                zona = "---"
                jornada = "---"
                asignaturas = "---"
                grados = "---"
                decreto_docente = "---"

            formacion = FormacionAcademicaBilinguismo.objects.filter(persona=aspirante)
            formaciones = ""
            for i in formacion:
                formaciones+= "["+i.titulo.encode('latin-1')+" - "+i.get_nivel_display().encode('latin-1')+" - "+i.institucion.encode('latin-1')+"]"

            certificacion = CertificacionBilinguismo.objects.filter(persona=aspirante)
            certificaciones = ""
            for i in certificacion:
                certificaciones+= "["+i.nombre.encode('latin-1')+" - "+i.get_duracion_display().encode('latin-1')+" - "+i.entidad.encode('latin-1')+"]"

            nombre = aspirante
            num_doc = aspirante.numero_documento
            municipio = Municipio.objects.get(id=aspirante.municipio_id)

            if aspirante.finalizada == True:
                finalizado = "SI"
            else:
                finalizado = "NO"

            arreglo = [finalizado, nombre, num_doc, aspirante.sexo, aspirante.email, aspirante.email_institucional,
            municipio.nombre.encode('latin-1'), aspirante.telefono, aspirante.celular,
            aspirante.direccion.encode('latin-1'), aspirante.get_nivel_educativo_display().encode('latin-1'),
            sede, cargo, zona, jornada, asignaturas, grados, decreto_docente,
            infoLaboral.get_nombramiento_display().encode('latin-1'),
            infoLaboral.get_tipo_etnoeducador_display().encode('latin-1'), formaciones, certificaciones]
            writer.writerow(arreglo)
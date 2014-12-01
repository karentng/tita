# encoding:utf-8
from django.core.management.base import BaseCommand, CommandError
from django.template import Template, Context
import smtplib
from campus.models import Estudiante, Municipio
from estudiante.models import InfoLaboral, FormacionAcademicaME, CertificacionTIC
import csv

class Command(BaseCommand):
    def handle(self, *args, **options):
        archivo = open("MaestrosEstudiante.csv","w") 
        writer = csv.writer(archivo, delimiter=';')
        writer.writerow(["Nombre Completo", u"Cédula".encode('iso-8859-1'),
            u"Género".encode('iso-8859-1'), u"Correo Personal".encode('iso-8859-1'), "Correo Institucional", "Municipio",
            u"Teléfono Fijo".encode('iso-8859-1'), "Celular", u"Dirección".encode('iso-8859-1'), "Nivel Educativo",
            u"Secretaría de Educación".encode('iso-8859-1'),"Sede", "Cargo", "Zona", "Jornada", "Asignaturas",
            "Grados", "Decreto Docente", "Nombramiento", "Tipo Etnoeducador",
            u"Formación Académica".encode('iso-8859-1'), "Certificaciones TIC"])

        aspirantes = Estudiante.objects.all()
        for aspirante in aspirantes:
            try:
                infoLaboral = InfoLaboral.objects.get(estudiante=aspirante)
            except Exception:
                continue
            formacion = FormacionAcademicaME.objects.filter(estudiante=aspirante)
            certificacion = CertificacionTIC.objects.filter(estudiante=aspirante)

            nombre = aspirante
            num_doc = aspirante.numero_documento
            municipio = Municipio.objects.get(id=aspirante.municipio_id)

            sede = infoLaboral.get_sede_display().encode('iso-8859-1')
            cargo = infoLaboral.get_cargo_display().encode('iso-8859-1')
            zona = infoLaboral.get_zona_display().encode('iso-8859-1')
            jornada = infoLaboral.get_jornada_display().encode('iso-8859-1')

            asigs = infoLaboral.asignaturas.all()
            asignaturas = ""
            for i in asigs:
                asignaturas+= i.nombre.encode('iso-8859-1')+" - "

            grads = infoLaboral.grados.all()
            grados = ""
            for i in grads:
                grados+= i.nombre.encode('iso-8859-1')+" - "

            formaciones = ""
            for i in formacion:
                formaciones+= "["+i.titulo.encode('iso-8859-1')+" - "+i.get_nivel_display().encode('iso-8859-1')+" - "+i.institucion.encode('iso-8859-1')+"]"

            certificaciones = ""
            for i in certificacion:
                certificaciones+= "["+i.nombre.encode('iso-8859-1')+" - "+i.get_duracion_display().encode('iso-8859-1')+" - "+i.entidad.encode('iso-8859-1')+"]"

            decreto_docente = infoLaboral.get_decreto_docente_display().encode('iso-8859-1')
            if infoLaboral.decreto_docente < 15:
                decreto_docente+= " - "+"D.L 2277 de 1979"
            else:
                decreto_docente+= " - "+"D.L 1278 de 2002"
            
            arreglo = [nombre, num_doc, aspirante.sexo, aspirante.email, aspirante.email_institucional,
            municipio.nombre.encode('iso-8859-1'), aspirante.telefono, aspirante.celular,
            aspirante.direccion.encode('iso-8859-1'), aspirante.get_nivel_educativo_display().encode('iso-8859-1'),
            infoLaboral.secretaria_educacion.nombre,
            sede, cargo, zona, jornada, asignaturas, grados, decreto_docente,
            infoLaboral.get_nombramiento_display().encode('iso-8859-1'),
            infoLaboral.get_tipo_etnoeducador_display().encode('iso-8859-1'), formaciones, certificaciones]
            writer.writerow(arreglo)
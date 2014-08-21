# encoding:utf-8
from django.core.management.base import BaseCommand, CommandError
from django.template import Template, Context
import smtplib
from email.mime.text import MIMEText
from convocat.models import Aspirante

EMAIL_TEMPLATE= u"""
{{calificativo}} {{nombre}}

A partir de este momento en la aplicación  se encuentra habilitado el módulo de subir documentos soporte.

Dado que se han detectado errores en el diligenciamiento del formulario de inscripción, se han añadido campos en algunas secciones para precisar la información. Por ello se ha habilitado nuevamente la edición para que se complete la información. 

No olvide guardar el número del registro que aparece en la segunda pestaña de la inscripción para editar o subir los soportes.

Su número de registro es: {{numero_registro}}
Ingrese a http://www.titaedpt.com.co/inscripcion/iniciar-inscripcion y en el recuadro "Ya estoy inscrito" ingrese este número para actualizar sus datos.

Por favor tenga en cuenta las siguientes sugerencias para cada una de las secciones del formulario:

= DATOS PERSONALES
Antes de finalizar esta página por favor asegúrese de que están totalmente diligenciadas todas casillas. 
Asegúrese de registrar la institución, el municipio y la jornada  donde usted es docente.

= FORMACIÓN ACADÉMICA
Guarde el número de registro que le acaba de asignar el sistema, lo va a necesitar durante el proceso.
Al llenar la información, asegúrese  de ingresar el nivel más alto de escolaridad que tenga y de marcar en la casilla donde se indica el tipo de formación.  

= FORMACIÓN EN TIC
Al llenar la información, verifique antes de finalizar que ha ingresado el curso donde haya recibido el mayor número de horas. 

= CONOCIMIENTOS ESPECÍFICOS
Antes de terminar asegúrese que ha calificado cada uno de los ítems de esta sección.

= IDIOMAS
Puede agregar varios idiomas extranjeros. Asegúrese de agregar el idioma extranjero que mejor domina.  

EXPERIENCIA EN ENSEÑANZA EN TIC

Tenga en cuenta que puede ingresar varios ítems en cada una de las categorías (Enseñanza a estudiantes, a profesores y a formadores).

Al llenar la información, asegúrese de seleccionar el mayor numero de horas que posee como formador TIC a estudiantes.  

Asegúrese de seleccionar también el mayor numero de horas que posee como formador TIC a docentes.  Si la mayor experiencia en numero de horas que posee como formador a docentes es como formador TIT@ en ejercicio, no es necesario que cargue el soporte.

De la misma manera, asegúrese de seleccionar el mayor número de horas que posee como formador de formadores.   


Cordialmente,


--
Equipo de Desarrollo
Proyecto TIT@
"""

lista_negra = set([])

#print sorted(lista_negra)
#exit();
class Command(BaseCommand):
    def handle(self, *args, **options):
        template = Template(EMAIL_TEMPLATE)
        self.stdout.write("args es "+str(args))
        id_ini, id_fin = args
        aspirantes = Aspirante.objects.filter(id__gte=id_ini, id__lte=id_fin).order_by('id')

        self.abrir_email()

        for asp in aspirantes:
            if asp.id in lista_negra: continue
            self.stdout.write("Procesando %d"%(asp.id))
            if not asp.email:
                self.stdout.write("ASPIRANTE SIN EMAIL:  %d - %s"%(asp.id, unicode(asp), asp.email))
            else :
                context = Context({
                    'calificativo': 'Estimado' if asp.sexo=='M' else 'Estimada',
                    'nombre': unicode(asp),
                    'numero_registro': asp.numero_inscripcion()
                })

                texto = template.render(context)

                #self.stdout.write(texto)
                self.enviar_email(asp.email, texto)

        self.cerrar_email()

    def abrir_email(self):
        
        self.server = smtplib.SMTP('smtp.gmail.com',587)
        
        self.server.ehlo()
        self.server.starttls()
        self.server.ehlo()
        
        self.server.login('titaedpt@gmail.com', 'titaedpt@2014')

    def enviar_email(self, direccion, contenido):
        #direccion = "vector9x@gmail.com"
        msg = MIMEText(contenido.encode('iso-8859-1'))
        msg['From'] = 'titaedpt@gmail.com'
        msg['To'] = direccion
        msg['Subject'] = "Convocatoria TITA - Subir soportes"
        self.server.sendmail('titaedpt@gmail.com', [direccion], msg.as_string())

    def cerrar_email(self):
        self.server.quit()
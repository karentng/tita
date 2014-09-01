# -*- coding: utf-8 -*-
from django import forms
#from bootstrap3_datetime.widgets import DateTimePicker
from datetimewidget.widgets import DateWidget
from django.forms import ModelForm, Textarea, HiddenInput, TextInput, Select, CheckboxSelectMultiple, FileInput, ClearableFileInput
from django.forms.models import inlineformset_factory
from django_select2 import AutoModelSelect2Field, Select2MultipleWidget
from campus.models import Estudiante, DatosLaborales, CertificacionTIC, ProgramasTIC, Horario
from convocat.forms import MyDateWidget, MunicipioChoice

class EstudianteForm(forms.ModelForm):
    #cargos = AutoModelSelect2Field()
    #instituciones = AutoModelSelect2Field()
    #asignaturas = AutoModelSelect2Field()
    #grados = AutoModelSelect2Field()
    municipio = MunicipioChoice(label = u"Municipio de residencia")
    class Meta:
        model = Estudiante
        fields = ('numero_documento', 'nombre1', 'nombre2', 'apellido1', 'apellido2', 'sexo', 'email', 'email_institucional', 'municipio','telefono', 'celular', 'direccion', 'nivel_educativo' )
        #fields = ('numero_documento', 'nombre1', 'nombre2', 'apellido1', 'apellido2', 'sexo', 'nacionalidad', 'municipio_nacimiento', 'direccion', 'municipio', 'telefono', 'celular', 'email')
        widgets = {
            # 'fecha_nacimiento': DateTimePicker(options={'format':'YYYY-MM-DD',  'pickTime':False}),
            #'cargos' : AutoModelSelect2Field()
        }

class DatosLaboralesForm(forms.ModelForm):
    class Meta:
        model = DatosLaborales
        fields = ('secretaria_educacion', 'institucion_educativa', 'cargos', 'sector', 'zona', 'jornada', 'grados', 'asignaturas', 'decreto_docente', 'nombramiento', 'etnoeducador', 'tipo_etnoeducador', 'poblacion_etnica')
        #fields = ('numero_documento', 'nombre1', 'nombre2', 'apellido1', 'apellido2', 'sexo', 'nacionalidad', 'municipio_nacimiento', 'direccion', 'municipio', 'telefono', 'celular', 'email')
        widgets = {
            # 'fecha_nacimiento': DateTimePicker(options={'format':'YYYY-MM-DD',  'pickTime':False}),
            #'cargos' : AutoModelSelect2Field()
        }

class CertificacionTICForm(forms.ModelForm):
    class Meta:
        model = CertificacionTIC
        fields = ('nombre', 'entidad', 'fecha')
        widgets = {
            'fecha': MyDateWidget()
        }

class ProgramaTICForm(forms.ModelForm):
    class Meta:
        model = ProgramasTIC
        fields = ('nombre', 'fecha')
        widgets = {
            'fecha': MyDateWidget()
        }

class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = ('dia', 'inicio', 'fin', 'curso')
# -*- coding: utf-8 -*-
from django import forms
from convocat.models import *
from bootstrap3_datetime.widgets import DateTimePicker
from django.forms import ModelForm, Textarea, HiddenInput, TextInput, Select
from django.forms.models import inlineformset_factory
from django_select2 import AutoModelSelect2Field

class MunicipioChoice(AutoModelSelect2Field):
    queryset = Municipio.objects.select_related('departamento')
    search_fields = ['nombre__icontains']

    def label_from_instance(self, obj):
        return u"%s (%s)"%(obj.nombre, obj.departamento.nombre)

class DatosPersonalesForm(forms.ModelForm):
    municipio_nacimiento = MunicipioChoice(help_text=u'Deje en blanco si nació fuera de Colombia', required=False)
    municipio = MunicipioChoice(label = "Municipio de residencia")
    class Meta:
        model = Aspirante
        fields = ('numero_documento', 'nombre1', 'nombre2', 'apellido1', 'apellido2', 'nacionalidad', 'municipio_nacimiento', 'fecha_nacimiento', 'sexo', 'municipio', 'direccion', 'telefono', 'celular', 'email')
        #fields = ('numero_documento', 'nombre1', 'nombre2', 'apellido1', 'apellido2', 'sexo', 'nacionalidad', 'municipio_nacimiento', 'direccion', 'municipio', 'telefono', 'celular', 'email')
        widgets = {
            'fecha_nacimiento': DateTimePicker(options={'format':'YYYY-MM-DD',  'pickTime':False}),
        }

class FormacionAcademicaForm(forms.ModelForm):
    class Meta:
        model = FormacionAcademica
        fields = ('nivel', 'titulo',  'institucion', 'fecha_inicio', 'fecha_terminacion','relacionado_pedagogia', 'relacionado_tics')
        widgets = {
            'fecha_inicio': DateTimePicker(options={'format':'YYYY-MM-DD',  'pickTime':False}),
            'fecha_terminacion': DateTimePicker(options={'format':'YYYY-MM-DD',  'pickTime':False}),
        }

class FormacionTicsForm(forms.ModelForm):
    class Meta:
        model = FormacionTics
        fields = ('duracion', 'titulo', 'fecha_inicio', 'fecha_terminacion', 'institucion')
        widgets = {
            'fecha_inicio': DateTimePicker(options={'format':'YYYY-MM-DD',  'pickTime':False}),
            'fecha_terminacion': DateTimePicker(options={'format':'YYYY-MM-DD',  'pickTime':False}),
        }

"""
class ConocimientosEspecificosForm(forms.ModelForm):
    class Meta:
        model = ConocimientosEspecificos
        fields = ('conocimiento1', 'conocimiento2', 'conocimiento3', 'conocimiento4', 'conocimiento5', 'conocimiento6', 'conocimiento7', 'conocimiento8')
        widgets = {
            #'manejo': Select({'size':3})
        }

class IdiomasManejadosForm(forms.ModelForm):
    class Meta:
        model = IdiomasManejados
        fields = ('idioma','habla','lee','escribe',)
        widgets = {
            'idioma': Select({'size':4}),
        }

class ExperienciaFormadorTicsForm(forms.ModelForm):
    class Meta:
        model = ExperienciaFormadorTics
        fields = ('formador_est','formador_doc','formador_for',)
        widgets = {
            'formador_est': Select({'size':4}),
            'formador_doc': Select({'size':4}),
            'formador_for': Select({'size':2}),
        }


"""
# -*- coding: utf-8 -*-
from django import forms
#from bootstrap3_datetime.widgets import DateTimePicker
from datetimewidget.widgets import DateWidget
from django.forms import ModelForm, Textarea, HiddenInput, TextInput, Select, CheckboxSelectMultiple, FileInput, ClearableFileInput
from django.forms.models import inlineformset_factory
from django_select2 import AutoModelSelect2Field, Select2MultipleWidget
from campus.models import Estudiante

def MyDateWidget():
    return DateWidget(usel10n=False, bootstrap_version=3, options={'format': 'yyyy-mm-dd', 'startView':4, 'language':'es'})

class EstudianteForm(forms.ModelForm):
    #cargos = AutoModelSelect2Field()
    #instituciones = AutoModelSelect2Field()
    #asignaturas = AutoModelSelect2Field()
    #grados = AutoModelSelect2Field()
    class Meta:
        model = Estudiante
        fields = ('numero_documento', 'nombre1', 'nombre2', 'apellido1', 'apellido2', 'sexo', 'telefono', 'celular', 'email', 'instituciones', 'cargos', 'asignaturas', 'grados', 'jornada')
        #fields = ('numero_documento', 'nombre1', 'nombre2', 'apellido1', 'apellido2', 'sexo', 'nacionalidad', 'municipio_nacimiento', 'direccion', 'municipio', 'telefono', 'celular', 'email')
        widgets = {
            # 'fecha_nacimiento': DateTimePicker(options={'format':'YYYY-MM-DD',  'pickTime':False}),
            #'cargos' : AutoModelSelect2Field()
        }
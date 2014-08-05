from django import forms
from convocat.models import *
from bootstrap3_datetime.widgets import DateTimePicker
from django.forms import ModelForm, Textarea, HiddenInput, TextInput, Select

class DatosPersonalesForm(forms.ModelForm):
    class Meta:
        model = Aspirante
        fields = ('tipo_documento', 'numero_documento', 'nombre1', 'nombre2', 'apellido1', 'apellido2', 'genero', 'nacionalidad', 'fecha_nacimiento', 'municipio_nacimiento', 'direccion', 'municipio', 'telefono', 'celular', 'email')
        widgets = {
            'fecha_nacimiento': DateTimePicker(options={'format':'YYYY-MM-DD',  'pickTime':False}),
        }

class FormacionAcademicaForm(forms.ModelForm):
    class Meta:
        model = FormacionAcademica
        fields = ('modalidad', 'numero_semestres', 'titulo', 'fecha_terminacion', 'tarjeta_profesional')
        widgets = {
            'fecha_terminacion': DateTimePicker(options={'format':'YYYY-MM-DD',  'pickTime':False}),
        }

class FormacionTicsForm(forms.ModelForm):
    class Meta:
        model = FormacionTics
        fields = ('curso',)
        widgets = {
            'curso': Select({'size': 5})
        }
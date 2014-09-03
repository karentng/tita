# -*- coding: utf-8 -*-
from django import forms
#from bootstrap3_datetime.widgets import DateTimePicker
from datetimewidget.widgets import DateWidget
from django.forms import ModelForm, Textarea, HiddenInput, TextInput, Select, CheckboxSelectMultiple, FileInput, ClearableFileInput
from django.forms.models import inlineformset_factory
from django_select2 import AutoModelSelect2Field, Select2MultipleWidget, Select2Widget
from campus.models import Estudiante
from estudiante.models import InfoLaboral,  CertificacionTIC, ProgramaTIC
from convocat.forms import MyDateWidget, MunicipioChoice

class EstudianteForm(forms.ModelForm):
    municipio = MunicipioChoice(label = u"Municipio de residencia")
    class Meta:
        model = Estudiante
        fields = ('numero_documento', 'nombre1', 'nombre2', 'apellido1', 'apellido2', 'sexo', 'email', 'email_institucional', 'municipio','telefono', 'celular', 'direccion', 'nivel_educativo' )

class InfoLaboralForm(forms.ModelForm):
    class Meta:
        model = InfoLaboral
        fields = ('secretaria_educacion', 'institucion_educativa', 'cargo', 'sector', 'zona', 'jornada', 'grados', 'asignaturas', 'decreto_docente', 'nombramiento', 'tipo_etnoeducador', 'poblacion_etnica')
        widgets = {
            'secretaria_educacion': Select2Widget(),
            'institucion_educativa': Select2Widget(),
            'grados': Select2MultipleWidget(),
            'asignaturas': Select2MultipleWidget(),
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
        model = ProgramaTIC
        fields = ('nombre', 'fecha')
        widgets = {
            'fecha': MyDateWidget()
        }

#class HorarioForm(forms.ModelForm):
#    class Meta:
#        model = Horario
#        fields = ('dia', 'inicio', 'fin', 'curso')
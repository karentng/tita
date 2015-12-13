# -*- coding: utf-8 -*-
from django import forms
#from bootstrap3_datetime.widgets import DateTimePicker
from datetimewidget.widgets import DateWidget
from django.forms import ModelForm, Textarea, HiddenInput, TextInput, Select, CheckboxSelectMultiple, FileInput, ClearableFileInput
from django.forms.models import inlineformset_factory
from django_select2 import AutoModelSelect2Field, Select2MultipleWidget, Select2Widget
from campus.models import Estudiante
from estudiante.models import InfoLaboral,  CertificacionTIC, FormacionAcademicaME, SEDES
from convocat.forms import MyDateWidget, MunicipioChoice
from convocat.forms import MyFileInput

class EstudianteForm(forms.ModelForm):
    municipio = MunicipioChoice(label = u"Municipio de residencia")
    #municipio_documento = MunicipioChoice(label = u"Municipio de expedición")
    class Meta:
        model = Estudiante
        fields = ('numero_documento', 'nombre1', 'nombre2', 'apellido1', 'apellido2', 'sexo', 'email', 'email_institucional', 'municipio','telefono', 'celular', 'direccion', 'nivel_educativo' )

class EstudianteCertificacionForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ('tipo_certificado', 'observacion_certificado',)

def obtenerSEDES():
    return SEDES

class InfoLaboralForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(InfoLaboralForm, self).__init__(*args, **kwargs)
        sedes = obtenerSEDES()
        cohorte2 = ()
        final = False
        for sede in sedes:
            if final == True:
                cohorte2 += ((sede),)
            else:
                if sede[0] == 46:
                    final = True
        
        self.fields['sede'].choices = cohorte2

    class Meta:
        model = InfoLaboral
        fields = ('secretaria_educacion', 'sede', 'cargo', 'zona', 'jornada', 'grados', 'asignaturas', 'decreto_docente', 'nombramiento', 'tipo_etnoeducador', 'poblacion_etnica')
        widgets = {
            'secretaria_educacion': Select2Widget(),
            #'institucion_educativa': Select2Widget(),
            'grados': Select2MultipleWidget(),
            'asignaturas': Select2MultipleWidget(),
        }

class FormacionAcademicaMEForm(forms.ModelForm):
    class Meta:
        model = FormacionAcademicaME
        fields = ('nivel', 'titulo', 'institucion', 'relacionado_pedagogia', 'relacionado_tic')

class CertificacionTICForm(forms.ModelForm):
    class Meta:
        model = CertificacionTIC
        fields = ('nombre', 'duracion', 'entidad')

class ContinuarRegistroFormDE(forms.Form):
    registro = forms.CharField(label='',max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Escriba su numero registro'}))

#class HorarioForm(forms.ModelForm):
#    class Meta:
#        model = Horario
#        fields = ('dia', 'inicio', 'fin', 'curso')
from django import forms
from bilinguismo.models import *
from convocat.forms import MyDateWidget, MunicipioChoice
from django_select2 import AutoModelSelect2Field, Select2MultipleWidget, Select2Widget

class BilinguismoForm(forms.ModelForm):

    municipio = MunicipioChoice(label = u"Municipio de residencia")
    class Meta:
        model = Bilinguismo
        exclude = ('inscripcion_finalizada', 'finalizada', 'cohorte')

class InfoLaboralBilinguismoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(InfoLaboralBilinguismoForm, self).__init__(*args, **kwargs)
        self.fields['institucion'].choices = self.fields['institucion'].choices[6:]
    class Meta:
        model = InfoLaboralBilinguismo
        exclude = ('persona',)
        widgets = {
            'grados': Select2MultipleWidget(),
            'asignaturas': Select2MultipleWidget(),
        }

class FormacionAcademicaBilinguismoForm(forms.ModelForm):
    class Meta:
        model = FormacionAcademicaBilinguismo
        exclude = ('persona',)

class CertificacionBilinguismoForm(forms.ModelForm):
    class Meta:
        model = CertificacionBilinguismo
        exclude = ('persona',)
#encoding: utf-8
from django import forms
from .models import *
from datetimewidget.widgets import DateWidget
from convocat.forms import MunicipioChoice, MyDateWidget

class EncuestaPadreForm(forms.ModelForm):
    municipio_nacimiento = MunicipioChoice(required=False, label = u"Municipio de nacimiento")

    class Meta:
        model = EncuestaPadreFamilia
        widgets = {
            'fecha_nacimiento' : MyDateWidget()
        }
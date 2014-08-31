#encoding: utf-8
from django import forms
from .models import *
from datetimewidget.widgets import DateWidget
from convocat.forms import MunicipioChoice, MyDateWidget

class MultiSelectFormField(forms.MultipleChoiceField):
    widget = forms.CheckboxSelectMultiple
 
    def __init__(self, *args, **kwargs):
        self.max_choices = kwargs.pop('max_choices', 0)
        super(MultiSelectFormField, self).__init__(*args, **kwargs)
 
    def clean(self, value):
        if not value and self.required:
            raise forms.ValidationError(self.error_messages['required'])
        # if value and self.max_choices and len(value) > self.max_choices:
        #     raise forms.ValidationError('You must select a maximum of %s choice%s.'
        #             % (apnumber(self.max_choices), pluralize(self.max_choices)))
        return value

class EncuestaPadreForm(forms.ModelForm):
    municipio_nacimiento = MunicipioChoice(required=False, label = u"Municipio de nacimiento")
    class Meta:
        model = EncuestaPadreFamilia
        widgets = {
            'fecha_nacimiento' : MyDateWidget(),
            'nivel_educativo' : forms.RadioSelect(),
            'ocupacion' : forms.RadioSelect(),
            'frecuencia_uso_computador' : forms.RadioSelect(),
            'frecuencia_uso_internet' : forms.RadioSelect(),
            
        }
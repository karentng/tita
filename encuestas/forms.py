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


class DatosBasicosPadreForm(forms.ModelForm):
    municipio_nacimiento = MunicipioChoice(required=False, label = u"Municipio de nacimiento")
    class Meta:
        model = EncuestaPadreFamilia
        fields = ('jornada','nombre','parentesco','municipio_nacimiento', 'fecha_nacimiento', 'barrio', 'institucion', 'grado', 'nivel_educativo', 'titulo', 'ocupacion')
        widgets = {
            'fecha_nacimiento' : MyDateWidget(),
            'nivel_educativo' : forms.RadioSelect(),
            'ocupacion' : forms.RadioSelect(),
        }


class FrecuenciaUsoPadreForm(forms.ModelForm):
    class Meta:
        model = EncuestaPadreFamilia
        fields = ('frecuencia_uso_computador', 'frecuencia_uso_internet')
        widgets = {
            'frecuencia_uso_computador' : forms.RadioSelect(),
            'frecuencia_uso_internet' : forms.RadioSelect(),
        }

class MejoraMateriaPadreForm(forms.ModelForm):
    class Meta:
        model = MejoraMateriaPadre
        fields = ('materia','puntos')
        widgets = {
            'materia' : forms.HiddenInput() ,
            'puntos' : forms.RadioSelect()
        }

def MejorasMateriaFormset(subform, data):
    materias = list(Materia.objects.order_by('id'))
    klass = forms.formsets.formset_factory(subform, extra=len(materias), can_delete=False, can_order=False)
    formset = klass(data)
    for mat,form in zip(materias,formset):
        form.initial = {'materia':mat, 'puntos':-1}
        form.fields['puntos'].label = mat.nombre


    return formset


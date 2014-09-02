#encoding: utf-8
from django import forms
from .models import *
from datetimewidget.widgets import DateWidget
from convocat.forms import MunicipioChoice, MyDateWidget



class EncuestaPadreForm(forms.ModelForm):
    municipio_nacimiento = MunicipioChoice(required=False, label = u"Municipio de nacimiento")
    class Meta:
        model = EncuestaPadreFamilia
        fields = ('jornada','nombre','parentesco','municipio_nacimiento', 'fecha_nacimiento', 'barrio', 'institucion', 'grado', 'nivel_educativo', 'titulo', 'ocupacion')
        widgets = {
            'fecha_nacimiento' : MyDateWidget(),
            'nivel_educativo' : forms.RadioSelect(),
            'ocupacion' : forms.RadioSelect(),
            'frecuencia_uso_computador' : forms.RadioSelect(),
            'frecuencia_uso_internet' : forms.RadioSelect(),
            'ayuda_internet' : forms.RadioSelect(),
            'angustia_evolucion' : forms.RadioSelect(),
            'dispersan_atencion' : forms.RadioSelect(),
            'bajo_puntaje_pisa' : forms.RadioSelect(),
        }



class MejoraMateriaPadreForm(forms.ModelForm):
    class Meta:
        model = MejoraMateriaPadre
        fields = ('materia','puntos')
        widgets = {
            'materia' : forms.HiddenInput() ,
            #'puntos' : forms.RadioSelect()
        }

def MejorasMateriaFormset(subform, data):
    materias = list(Materia.objects.order_by('id'))
    klass = forms.formsets.formset_factory(subform, extra=len(materias), can_delete=False, can_order=False)
    formset = klass(data)
    for mat,form in zip(materias,formset):
        form.initial = {'materia':mat, 'puntos':-1}
        form.fields['puntos'].label = mat.nombre
    return formset


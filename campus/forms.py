# -*- coding: utf-8 -*-
from django import forms
from django.forms.models import inlineformset_factory
from campus.models import *
import os.path
from django.db.models import Q

class NoModificableFileInput(forms.widgets.ClearableFileInput):
    template_with_initial = '%(initial)s'

class AsistenciaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AsistenciaForm, self).__init__(*args, **kwargs)
        #asistentes = forms.ModelMultipleChoiceField(initial=True, widget=forms.CheckboxSelectMultiple())
        laclase = self.instance
        self.fields['asistentes'].queryset = laclase.curso.estudiantes.all()    

    class Meta:
        model = Clases
        fields = ('asistentes','observacion')
        #ModelMultipleChoiceField(Numbers.objects.all(), required=True, widget=forms.CheckboxSelectMultiple(), label='Select No')
        widgets = {'asistentes': forms.CheckboxSelectMultiple(attrs={"checked":""}),
                   'observacion': forms.Textarea(attrs={'rows': 4})}

    

#AsistenciaFormset = modelformset_factory(Asistencia)

class SoporteClaseForm(forms.ModelForm):
    class Meta:
        model = SoporteClase
        fields = ('archivo',)
        widgets = {'archivo': NoModificableFileInput()}


SoportesFormset = inlineformset_factory(Clase, SoporteClase, form=SoporteClaseForm)# ,  can_delete=False)


class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        exclude = ('clase','estudiante',)
        '''widgets = {'actividad1': forms.CheckboxSelectMultiple(),
                   'actividad2': forms.CheckboxSelectMultiple()}'''

        

    '''def __init__(self, *args, **kwargs):
        super(ActividadForm, self).__init__(*args, **kwargs)
        actividad = self.instance
        self.fields['estudiantes'].queryset = actividad.clase.curso.estudiantes.all()

        '''
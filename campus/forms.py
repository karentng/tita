# -*- coding: utf-8 -*-
from django import forms
from django.forms.models import inlineformset_factory
from campus.models import *
import os.path
from django.db.models import Q

class NoModificableFileInput(forms.widgets.ClearableFileInput):
    template_with_initial = '%(initial)s'

class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Clases
        fields = ('asistentes',)
        widgets = {'asistentes': forms.CheckboxSelectMultiple()}

    def __init__(self, *args, **kwargs):
        super(AsistenciaForm, self).__init__(*args, **kwargs)
        laclase = self.instance
        self.fields['asistentes'].queryset = laclase.curso.estudiantes.all()

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
        '''fields = ('actividad1','actividad2',)
        widgets = {'actividad1': forms.CheckboxSelectMultiple(),
                   'actividad2': forms.CheckboxSelectMultiple()}

        

    def __init__(self, *args, **kwargs):
        super(ActividadForm, self).__init__(*args, **kwargs)
        actividad = self.instance
        self.fields['estudiantes'].queryset = actividad.clase.curso.estudiantes.all()

        '''
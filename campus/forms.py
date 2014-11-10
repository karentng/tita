# -*- coding: utf-8 -*-
from django import forms
from django.forms.models import inlineformset_factory
from campus.models import *

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
        #fields = ('asistencia', 'actividad1', 'actividad2', 'actividad3', 'actividad4')
        '''widgets = {'asistencia': forms.CheckboxSelectMultiple()}

    def __init__(self, *args, **kwargs):
        super(ActividadForm, self).__init__(*args, **kwargs)
        laclase = self.actividad.clase
        self.fields['asistencia'].queryset = laclase.cursos.estudiantes.all()'''
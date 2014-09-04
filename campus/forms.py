# -*- coding: utf-8 -*-
from django import forms
from campus.models import *

class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Clase
        fields = ('asistentes',)
        widgets = {'asistentes': forms.CheckboxSelectMultiple()}

class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = ('descripcion',)

# -*- coding: utf-8 -*-
from django import forms
from campus.models import *

class AsistenciaForm(forms.ModelForm):
    fields = ('asistentes',)
    class Meta:
        model = Clase


# -*- coding: utf-8 -*-
from django import forms
from cronograma.models import Evento
from convocat.forms import MyDateWidget
from datetimewidget.widgets import DateWidget

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento 

        fields = ('nombre', 'fecha_inicio', 'hora_inicio', 'fecha_finalizacion', 'hora_finalizacion', 'descripcion')
        widgets = {
            'fecha_inicio': MyDateWidget(),
            'fecha_finalizacion': MyDateWidget(),
         	'hora_inicio' : forms.TimeInput(format='%H:%M'),
            'descripcion': forms.Textarea(attrs={'rows': 3})
        }
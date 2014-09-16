# -*- coding: utf-8 -*-
from django import forms
from cronograma.models import EventosDiplomado, EventosAcompanamiento
from convocat.forms import MyDateWidget
from datetimewidget.widgets import DateWidget

class EventosDiplomadoForm(forms.ModelForm):
    class Meta:
        model = EventosDiplomado 

        fields = ('nombre', 'fecha_inicio', 'hora_inicio', 'fecha_finalizacion', 'hora_finalizacion', 'descripcion')
        widgets = {
            'fecha_inicio': MyDateWidget(),
            'fecha_finalizacion': MyDateWidget(),
         	'hora_inicio' : forms.TimeInput(format='%H:%M'),
            'descripcion': forms.Textarea(attrs={'rows': 3})
        }

class EventosAcompanamientoForm(forms.ModelForm):
    class Meta:
        model = EventosAcompanamiento

        fields = ('nombre', 'fecha_inicio', 'hora_inicio', 'fecha_finalizacion', 'hora_finalizacion', 'descripcion')
        widgets = {
            'fecha_inicio': MyDateWidget(),
            'fecha_finalizacion': MyDateWidget(),
         	'hora_inicio' : forms.TimeInput(format='%H:%M'),
            'descripcion': forms.Textarea(attrs={'rows': 3})
        }
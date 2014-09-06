# -*- coding: utf-8 -*-
from django import forms
from cronograma.models import Evento
from datetimewidget.widgets import DateWidget

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ('nombre', 'fecha_inicio', 'fecha_finalizacion','descripcion')
        widgets = {
            #'fecha_inicio': DateTimePicker(options={'format':'YYYY-MM-DD',  'pickTime':False}),
            #'fecha_terminacion': DateTimePicker(options={'format':'YYYY-MM-DD',  'pickTime':False}),
            'fecha_inicio': MyDateWidget(), 'fecha_finalizacion': MyDateWidget()
        }
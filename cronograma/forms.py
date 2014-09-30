# -*- coding: utf-8 -*-
from django import forms
from campus.models import Clase
from datetimewidget.widgets import DateTimeWidget



class EventosDiplomadoForm(forms.ModelForm):
    class Meta:
        model = Clase

        fields = ('nombre', 'fecha_inicio', 'duracion', 'descripcion')

        widgets = {
            'fecha_inicio': DateTimeWidget(options={'format': 'dd/mm/yyyy hh:ii','autoclose': 'true','startView':'4','minuteStep':'30',},usel10n=False, bootstrap_version=3),
            #'fecha_finalizacion': DateTimeWidget(options={'format': 'dd/mm/yyyy hh:ii','autoclose': 'true','startView':'4','minuteStep':'30',},usel10n=False, bootstrap_version=3),
         	'descripcion': forms.Textarea(attrs={'rows': 4})
        }

class EventosAcompanamientoForm(forms.ModelForm):
    class Meta:
        model = Clase

        fields = ('institucion', 'nombre', 'fecha_inicio','duracion', 'descripcion')
        widgets = {
            'fecha_inicio': DateTimeWidget(options={'format': 'dd/mm/yyyy hh:ii','autoclose': 'true','startView':'4','minuteStep':'30',},usel10n=False, bootstrap_version=3),
            #'fecha_finalizacion': DateTimeWidget(options={'format': 'dd/mm/yyyy hh:ii','autoclose': 'true','startView':'4','minuteStep':'30',},usel10n=False, bootstrap_version=3),
            'descripcion': forms.Textarea(attrs={'rows': 4})
        }
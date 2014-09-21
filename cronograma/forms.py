# -*- coding: utf-8 -*-
from django import forms
from campus.models import Clase
from convocat.forms import MyDateWidget
from datetimewidget.widgets import DateTimeWidget



class EventosDiplomadoForm(forms.ModelForm):
    class Meta:
        model = Clase

        fields = ('nombre', 'fecha_inicio', 'fecha_finalizacion', 'descripcion')

        widgets = {
            'fecha_inicio': MyDateWidget(),
            'fecha_finalizacion': MyDateWidget(),
         	#'hora_inicio' : forms.TimeInput(format='%H:%M'),
            'hora_inicio': DateTimeWidget(options={'format': 'hh:ii','viewSelect':'hour','autoclose': 'true', 'showMeridian' : 'false', 'startView':'1', 'minview':'0','maxView':'1','minuteStep':'30','keyboardNavigation':'false',},usel10n=False, bootstrap_version=3),
            'hora_finalizacion': DateTimeWidget(options={'format': 'hh:ii','viewSelect':'hour','autoclose': 'true', 'showMeridian' : 'false', 'startView':'1', 'minview':'0','maxView':'1','minuteStep':'30','keyboardNavigation':'false',},usel10n=False, bootstrap_version=3),
            'descripcion': forms.Textarea(attrs={'rows': 3})
        }

class EventosAcompanamientoForm(forms.ModelForm):
    class Meta:
        model = Clase

        fields = ('institucion', 'nombre', 'fecha_inicio','fecha_finalizacion', 'descripcion')
        widgets = {
            'fecha_inicio': MyDateWidget(),
            'fecha_finalizacion': MyDateWidget(),
         	#'hora_inicio' : forms.TimeInput(format='%H:%M'),
            #'hora_inicio' : DateWidget(usel10n=False, bootstrap_version=3, options={'format': 'hh:mm'}),
            'hora_inicio': DateTimeWidget(options={'format':'hh:ii','viewSelect':'hour','autoclose': 'true', 'showMeridian' : 'false', 'startView':'1', 'minview':'0','maxView':'1','minuteStep':'30','keyboardNavigation':'false',},usel10n=False, bootstrap_version=3),
            'hora_finalizacion': DateTimeWidget(options={'format':'hh:ii','viewSelect':'hour','autoclose': 'true', 'showMeridian' : 'false', 'startView':'1', 'minview':'0','maxView':'1','minuteStep':'30','keyboardNavigation':'false',},usel10n=False, bootstrap_version=3),
            'descripcion': forms.Textarea(attrs={'rows': 3})
        }
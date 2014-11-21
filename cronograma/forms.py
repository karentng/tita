# -*- coding: utf-8 -*-
from django import forms
from campus.models import Clases, AcompanamientoInSitus, SoporteClases, SoporteAcompanamiento, Cursos, Formador, Estudiante
from datetimewidget.widgets import DateTimeWidget
from datetimewidget.widgets import DateWidget
from django.forms import ModelForm, Textarea, HiddenInput, TextInput, Select, CheckboxSelectMultiple, FileInput, ClearableFileInput
from django.db.models import Q
from django.contrib.auth.models import User
from estudiante.models import JORNADAS, SEDES, InfoLaboral



class EventosDiplomadoForm(forms.ModelForm):
    class Meta:
        model = Clases

        fields = ('nombre', 'curso', 'fecha_inicio', 'duracion', 'descripcion')



        widgets = {

            'fecha_inicio': DateTimeWidget(options={'format': 'dd/mm/yyyy hh:ii','autoclose': 'true','startView':'4','minuteStep':'30',},usel10n=False, bootstrap_version=3),
            #'fecha_finalizacion': DateTimeWidget(options={'format': 'dd/mm/yyyy hh:ii','autoclose': 'true','startView':'4','minuteStep':'30',},usel10n=False, bootstrap_version=3),
         	'descripcion': forms.Textarea(attrs={'rows': 4}),
            'nombre': forms.TextInput(attrs={'readonly':'readonly'})
        }

class EventosDiplomadoMForm(forms.ModelForm):
    class Meta:
        model = Clases

        fields = ('nombre', 'curso', 'fecha_inicio', 'duracion', 'descripcion')



        widgets = {

            'fecha_inicio': DateTimeWidget(options={'format': 'dd/mm/yyyy hh:ii','autoclose': 'true','startView':'4','minuteStep':'30',},usel10n=False, bootstrap_version=3),
            #'fecha_finalizacion': DateTimeWidget(options={'format': 'dd/mm/yyyy hh:ii','autoclose': 'true','startView':'4','minuteStep':'30',},usel10n=False, bootstrap_version=3),
            'descripcion': forms.Textarea(attrs={'rows': 4}),
            #'nombre': forms.TextInput(attrs={'readonly':'readonly'})
        }

class EventosAcompanamientoForm(forms.ModelForm):
    class Meta:
        model = AcompanamientoInSitus

        fields = ('nombre', 'curso', 'fecha_inicio','duracion', 'descripcion')
        widgets = {
            'fecha_inicio': DateTimeWidget(options={'format': 'dd/mm/yyyy hh:ii','startView':'4','minuteStep':'30',},usel10n=False, bootstrap_version=3),
            #'fecha_inicio': DateWidget(usel10n=False, bootstrap_version=3, options={'format': 'yyyy-mm-dd', 'startView':4, 'language':'es'}),
            #'fecha_finalizacion': DateTimeWidget(options={'format': 'dd/mm/yyyy hh:ii','autoclose': 'true','startView':'4','minuteStep':'30',},usel10n=False, bootstrap_version=3),
            'descripcion': forms.Textarea(attrs={'rows': 4}),
            'nombre': forms.TextInput(attrs={'readonly':'readonly'})
        }

class EventosAcompanamientoMForm(forms.ModelForm):
    class Meta:
        model = AcompanamientoInSitus

        fields = ('nombre', 'curso', 'fecha_inicio','duracion', 'descripcion')
        widgets = {
            'fecha_inicio': DateTimeWidget(options={'format': 'dd/mm/yyyy hh:ii','startView':'4','minuteStep':'30',},usel10n=False, bootstrap_version=3),
            #'fecha_inicio': DateWidget(usel10n=False, bootstrap_version=3, options={'format': 'yyyy-mm-dd', 'startView':4, 'language':'es'}),
            #'fecha_finalizacion': DateTimeWidget(options={'format': 'dd/mm/yyyy hh:ii','autoclose': 'true','startView':'4','minuteStep':'30',},usel10n=False, bootstrap_version=3),
            'descripcion': forms.Textarea(attrs={'rows': 4})
        }

from django.utils.translation import ugettext_lazy
from django.utils.encoding import force_text, python_2_unicode_compatible
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape, format_html
from django.forms import CheckboxInput
import os.path
class MyFileInput(ClearableFileInput):
    
    clear_checkbox_label = '' #ugettext_lazy('Clear')
    template_with_clear = '%(clear)s <label class="text-danger" style="cursor:pointer" for="%(clear_checkbox_id)s">%(clear_checkbox_label)s</label>'
    url_markup_template = '<a target="_blank" href="{0}">{1}</a>'

    def render(self, name, value, attrs=None):
        
        substitutions = {
            'initial_text': self.initial_text,
            'input_text': self.input_text,
            'clear_template': '',
            'clear_checkbox_label': self.clear_checkbox_label,
        }

        template = '%(input)s'
        substitutions['input'] = super(ClearableFileInput, self).render(name, value, attrs)

        if value and hasattr(value, "url"):
            template = self.template_with_initial
            substitutions['initial'] = format_html(self.url_markup_template,
                                                   value.url,
                                                   os.path.basename(value.name))
            if  self.is_required:
                checkbox_name = self.clear_checkbox_name(name)
                checkbox_id = self.clear_checkbox_id(checkbox_name)
                substitutions['clear_checkbox_name'] = conditional_escape(checkbox_name)
                substitutions['clear_checkbox_id'] = conditional_escape(checkbox_id)
                substitutions['clear'] = CheckboxInput(attrs={'onclick':'if(confirm("Seguro que desea quitar este archivo?")){  $("form").submit().submit() } else return false;' } ).render(checkbox_name, False, attrs={'id': checkbox_id, 'style':'display:none'})
                substitutions['clear_template'] = self.template_with_clear % substitutions

        return mark_safe(template % substitutions)


class DocumentosSoporteForm(forms.ModelForm):
    class Meta:
        model = SoporteClases
        exclude = ('clase',)
        widgets = {
            'archivo' : MyFileInput(),

        }

class DocumentosSoporteAcompanamientoForm(forms.ModelForm):
    class Meta:
        model = SoporteAcompanamiento
        exclude = ('acompanamiento',)
        widgets = {
            'archivo' : MyFileInput(),

        }

class CursoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        jornada = kwargs.pop('jornada', None)
        sede = kwargs.pop('sede', None)
        super(CursoForm, self).__init__(*args, **kwargs)
        self.fields['formador1'].queryset = self.fields['formador1'].queryset.exclude( Q(formador1 = Cursos.objects.all()) | Q( formador2 =  Cursos.objects.all()))
        self.fields['formador2'].queryset = self.fields['formador2'].queryset.exclude( Q(formador1 = Cursos.objects.all()) | Q( formador2 =  Cursos.objects.all()))
        if sede and jornada :
            estudiantes = InfoLaboral.objects.filter(sede=sede, jornada=jornada).values('estudiante')
            ids = []
            for est in estudiantes:
                ids.append(est['estudiante'])
            self.fields['estudiantes'].queryset = Estudiante.objects.filter(id__in=ids)#self.fields['estudiantes'].queryset.exclude( Q(formador1 = Cursos.objects.all()) | Q( formador2 =  Cursos.objects.all()))
    class Meta:
        model = Cursos
        fields = ('descripcion','institucion','formador1','formador2', 'estudiantes',)
        widgets = {'estudiantes': forms.CheckboxSelectMultiple()}

class CursoMForm(forms.ModelForm):
    
    class Meta:
        model = Cursos
        fields = ('descripcion','institucion','formador1','formador2', 'estudiantes',)
        widgets = {'estudiantes': forms.CheckboxSelectMultiple()}

                

class FormadorForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(FormadorForm, self).__init__(*args, **kwargs)
        #self.fields['usuario'].queryset = self.fields['usuario'].queryset.exclude(formador = Formador.objects.all())
        self.fields['usuario'].queryset = self.fields['usuario'].queryset.filter(id__in = User.objects.filter(groups__id=2)).exclude(formador = Formador.objects.all())
    class Meta:
        model = Formador
        fields = ('nombre1','apellido1','jornada','tutor','usuario',)

class EstudiantesCurso(forms.Form):
    sedes = forms.ChoiceField(widget=forms.Select(), choices=SEDES)
    jornadas = forms.ChoiceField(widget=forms.Select(), choices=JORNADAS)
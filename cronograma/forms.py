# -*- coding: utf-8 -*-
from django import forms
from campus.models import Clases, AcompanamientoInSitus, SoporteClase, SoporteAcompanamiento, Cursos, Formador, Estudiante
from datetimewidget.widgets import DateTimeWidget
from datetimewidget.widgets import DateWidget
from django.forms import ModelForm, Textarea, HiddenInput, TextInput, Select, CheckboxSelectMultiple, FileInput, ClearableFileInput



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
            'fecha_inicio': DateTimeWidget(options={'format': 'dd/mm/yyyy hh:ii','autoclose': 'true','startView':'4','minuteStep':'30',},usel10n=False, bootstrap_version=3),
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
            'fecha_inicio': DateTimeWidget(options={'format': 'dd/mm/yyyy hh:ii','autoclose': 'true','startView':'4','minuteStep':'30',},usel10n=False, bootstrap_version=3),
            #'fecha_inicio': DateWidget(usel10n=False, bootstrap_version=3, options={'format': 'yyyy-mm-dd', 'startView':4, 'language':'es'}),
            #'fecha_finalizacion': DateTimeWidget(options={'format': 'dd/mm/yyyy hh:ii','autoclose': 'true','startView':'4','minuteStep':'30',},usel10n=False, bootstrap_version=3),
            'descripcion': forms.Textarea(attrs={'rows': 4})
        }

from django.utils.translation import ugettext_lazy
from django.utils.encoding import force_text, python_2_unicode_compatible
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape, format_html
from django.forms import CheckboxInput

class MyFileInput(ClearableFileInput):
    #initial_text = ugettext_lazy('Currently')
    #input_text = ugettext_lazy('Change')
    clear_checkbox_label = 'Quitar' #ugettext_lazy('Clear')

    #template_with_initial = '%(initial_text)s: %(initial)s %(clear_template)s<br />%(input_text)s: %(input)s'

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
            if not self.is_required:
                checkbox_name = self.clear_checkbox_name(name)
                checkbox_id = self.clear_checkbox_id(checkbox_name)
                substitutions['clear_checkbox_name'] = conditional_escape(checkbox_name)
                substitutions['clear_checkbox_id'] = conditional_escape(checkbox_id)
                substitutions['clear'] = CheckboxInput(attrs={'onclick':'if(confirm("Seguro que desea quitar este archivo?")){  $("form").submit() } else return false;' } ).render(checkbox_name, False, attrs={'id': checkbox_id, 'style':'display:none'})
                substitutions['clear_template'] = self.template_with_clear % substitutions

        return mark_safe(template % substitutions)


class DocumentosSoporteForm(forms.ModelForm):
    class Meta:
        model = SoporteClase
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
    class Meta:
        model = Cursos
        fields = ('descripcion','institucion','formador','estudiantes',)
        widgets = {'estudiantes': forms.CheckboxSelectMultiple()}

        



        

class FormadorForm(forms.ModelForm):
    class Meta:
        model = Formador

        
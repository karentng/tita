# -*- coding: utf-8 -*-
from django import forms
from malla.models import *
from datetimewidget.widgets import DateWidget
from django.forms import ModelForm, Textarea, HiddenInput, TextInput, Select, CheckboxSelectMultiple, FileInput, ClearableFileInput
from django.forms.models import inlineformset_factory
from django_select2 import AutoModelSelect2Field, Select2MultipleWidget

def MyDateWidget():
    return DateWidget(usel10n=False, bootstrap_version=3, options={'format': 'yyyy-mm-dd', 'startView':4, 'language':'es'})

class InformacionBasicaForm(forms.ModelForm):
    class Meta:
        model = Contratista
        fields = ('numero_documento', 'nombre1', 'nombre2', 'apellido1', 'apellido2','sexo', 'fecha_nacimiento', 'direccion', 'universidad','programa_academico')#, 'estrato',)# 'sector', 'sectordesplazamiento',)
        widgets = {
            'fecha_nacimiento' : MyDateWidget()
        }

class InformacionContactoForm(forms.ModelForm):
    class Meta:
        model = ContratistaInfoContacto
        fields = ('celularppal', 'celularsec', 'telfijoppal', 'telfijosec', 'email', 'twitter', 'facebook', 'personacontacto', 'numerocontacto',)

class AreasConocimientoForm(forms.ModelForm):
    class Meta:
        model = ContratistaAreasConocimiento
        fields = ('cienciasnaturales', 'fisica', 'quimica', 'biologia', 'matematica', 'trigonometria', 'algebra', 'logica', 'geometria', 'electronica', 'espanol', 'ingles', 'cienciassociales', 'filosofia', 'artistica', 'etica', 'cienciaseconomicas', 'educacionfisica', 'tecnologia', 'pedagogia', 'dibujotecnico',)

class RequerimientoForm(forms.ModelForm):
    class Meta:
        model = Requerimiento
        fields = ('estado_req', 'fecha_rec', 'fecha_eje', 'fisico_fir',  'descripcion_req', 'no_contratistas', 'lugar_req', 'responsable', 'email_responsable', 'celular_responsable')
        widgets = {
            'fecha_rec' : MyDateWidget(),
            'fecha_eje' : MyDateWidget(),
            'descripcion_req' : Textarea(attrs={'rows': 3}),
            #'justificacion_req' : Textarea(attrs={'rows': 3}),
        }

class ReclamacionForm(forms.ModelForm):
    class Meta:
        model = Reclamacion
        fields = ('colegio', 'jornada', 'fecha', 'supervisor', 'descripcion')
        widgets = {
            'fecha' : MyDateWidget(),
            'descripcion' : Textarea(attrs={'rows': 3}),
            
        }

class ReclamacionModificarForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReclamacionModificarForm, self).__init__(*args, **kwargs)
        #instance = getattr(self, 'instance', None)
        self.fields['colegio'].widget.attrs['disabled'] = True
    class Meta:
        model = Reclamacion
        fields = ('colegio', 'jornada', 'fecha', 'supervisor', 'descripcion', 'estado', 'observaciones')
        widgets = {
            'fecha' : MyDateWidget(),
            'descripcion' : Textarea(attrs={'rows': 3, 'readonly':'readonly'}),
            #'colegio' : TextInput(attrs={'readonly':'readonly'}),
            'jornada' : TextInput(attrs={'readonly':'readonly'}),
            'supervisor' : TextInput(attrs={'readonly':'readonly'}),
            'observaciones' : Textarea(attrs={'rows': 3,}),
            
        }


class ListaForm(forms.ModelForm):
    horas = forms.IntegerField(initial=5)
    class Meta:
        model = Lista
        fields = ('asignacion', 'requerimiento', 'fecha', 'colegio', 'profesor', 'contratista', 'espacio', 'condicion', 'tipo', 'horas', 'observaciones')
        widgets = {
            'fecha' : MyDateWidget(),
            'observaciones' : Textarea(attrs={'rows': 3}),
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
        model = ContratistaDocumentosSoporte
        exclude = ('monitor',)
        widgets = {
            'eps_sisben' : MyFileInput(),
            'matricula' : MyFileInput(),
            'rut' : MyFileInput(),
            'hv' : MyFileInput(),
        }

class MonitorForm(forms.ModelForm):
    class Meta:
        model = Monitor
        widgets = {
            'fecha_nacimiento' : MyDateWidget(),
            'soportes' : MyFileInput(),
            'd10' : MyFileInput(),
            'tabulado' : MyFileInput(),
            'recibo' : MyFileInput(),
            'cedula' : MyFileInput(),
            'rut' : MyFileInput(),
        }
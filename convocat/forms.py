# -*- coding: utf-8 -*-
from django import forms
from convocat.models import *
#from bootstrap3_datetime.widgets import DateTimePicker
from datetimewidget.widgets import DateWidget
from django.forms import ModelForm, Textarea, HiddenInput, TextInput, Select, CheckboxSelectMultiple, FileInput, ClearableFileInput
from django.forms.models import inlineformset_factory
from django_select2 import AutoModelSelect2Field, Select2MultipleWidget

def MyDateWidget():
    return DateWidget(usel10n=False, bootstrap_version=3, options={'format': 'yyyy-mm-dd', 'startView':4, 'language':'es'})

class MunicipioChoice(AutoModelSelect2Field):
    queryset = Municipio.objects.select_related('departamento')
    search_fields = ['nombre__icontains']

    def label_from_instance(self, obj):
        return u"%s (%s)"%(obj.nombre, obj.departamento.nombre)

class DatosPersonalesForm(forms.ModelForm):
    municipio_nacimiento = MunicipioChoice(help_text=u'Deje en blanco si nació fuera de Colombia', required=False)
    municipio = MunicipioChoice(label = u"Municipio de residencia")
    municipio_institucion = MunicipioChoice(label=u'Municipio de la institución donde labora')
    class Meta:
        model = Aspirante
        fields = ('numero_documento', 'nombre1', 'nombre2', 'apellido1', 'apellido2', 'nacionalidad', 'municipio_nacimiento', 'fecha_nacimiento', 'sexo', 'municipio', 'direccion', 'telefono', 'celular', 'email', 'institucion_actual', 'municipio_institucion', 'jornada')
        #fields = ('numero_documento', 'nombre1', 'nombre2', 'apellido1', 'apellido2', 'sexo', 'nacionalidad', 'municipio_nacimiento', 'direccion', 'municipio', 'telefono', 'celular', 'email')
        widgets = {
            # 'fecha_nacimiento': DateTimePicker(options={'format':'YYYY-MM-DD',  'pickTime':False}),
            'fecha_nacimiento' : MyDateWidget()
        }

class FormacionAcademicaForm(forms.ModelForm):
    class Meta:
        model = FormacionAcademica
        fields = ('nivel', 'titulo',  'institucion', 'fecha_inicio', 'fecha_terminacion','relacionado_pedagogia', 'relacionado_tics')
        widgets = {
            #'fecha_inicio': DateTimePicker(options={'format':'YYYY-MM-DD',  'pickTime':False}),
            #'fecha_terminacion': DateTimePicker(options={'format':'YYYY-MM-DD',  'pickTime':False}),
            'fecha_inicio': MyDateWidget(), 'fecha_terminacion': MyDateWidget()
        }

class FormacionTicsForm(forms.ModelForm):
    class Meta:
        model = FormacionTics
        fields = ('duracion', 'titulo', 'fecha_inicio', 'fecha_terminacion', 'institucion')
        widgets = {
            #'fecha_inicio': DateTimePicker(options={'format':'YYYY-MM-DD',  'pickTime':False}),
            #'fecha_terminacion': DateTimePicker(options={'format':'YYYY-MM-DD',  'pickTime':False}),
            'fecha_inicio': MyDateWidget(), 'fecha_terminacion': MyDateWidget()
        }


class ConocimientosEspecificosForm(forms.ModelForm):
    class Meta:
        model = ConocimientosEspecificos
        fields = ('conocimiento1', 'conocimiento2', 'conocimiento3', 'conocimiento4', 'conocimiento5', 'conocimiento6', 'conocimiento7', 'conocimiento8')
        widgets = {
            #'manejo': Select({'size':3})
        }


class IdiomasManejadosForm(forms.ModelForm):
    class Meta:
        model = Idioma
        fields = ('idioma','habla','lee','escribe',)



class ExperienciaFormadorForm(forms.ModelForm):
    class Meta:
        model = ExperienciaFormador
        exclude = ('aspirante',)
        widgets = {
            'fecha_inicio': MyDateWidget(), 'fecha_fin': MyDateWidget(),
        }
"""
class ExperienciaEnsenanzaForm(forms.ModelForm):
    class Meta:
        model = ExperienciaEnsenanza
        fields = ('institucion', 'tipo_institucion', 'jornada', 'nivel', 'areas', 'fecha_inicio', 'fecha_fin', 'telefono', 'email')
        widgets = {
            #'fecha_inicio': DateTimePicker(options={'format':'YYYY-MM-DD',  'pickTime':False}),
            #'fecha_fin': DateTimePicker(options={'format':'YYYY-MM-DD',  'pickTime':False}),
            'fecha_inicio': MyDateWidget(), 'fecha_fin': MyDateWidget(),
            'areas' : Select2MultipleWidget()
        }



class ExperienciaOtraForm(forms.ModelForm):
    class Meta:
        model = ExperienciaOtra
        fields = ('entidad', 'tipo_entidad', 'telefono', 'email', 'fecha_inicio', 'fecha_fin', 'cargo')
        widgets = {
            #'fecha_inicio': DateTimePicker(options={'format':'YYYY-MM-DD',  'pickTime':False}),
            #'fecha_fin': DateTimePicker(options={'format':'YYYY-MM-DD',  'pickTime':False}),
            'fecha_inicio': MyDateWidget(), 'fecha_fin': MyDateWidget(),
        }
"""

class ContinuarRegistroForm(forms.Form):
    registro = forms.CharField(label='',max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Escriba su numero registro'}))

"""
class AdjuntoForm(forms.ModelForm):
    class Meta:
        model = Adjunto
        fields = ('tipo', 'descripcion', 'archivo')
"""



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
        model = DocumentosSoporte
        exclude = ('aspirante',)
        widgets = {
            'formacion_academica' : MyFileInput(),
            'formacion_tics' : MyFileInput(),
            'idiomas' : MyFileInput(),
            'ensenanza_tic_estudiantes' : MyFileInput(),
            'ensenanza_tic_profesores' : MyFileInput(),
            'ensenanza_tic_formadores' : MyFileInput(),
        }

class ArchivoForm(forms.ModelForm):
    class Meta:
        model = Archivo
        exclude = ('activo','usuario')

class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        exclude = ('concepto_por_actividad', 'activo', 'usuario')

class EstadoDeAvanceForm(forms.ModelForm):
    #fecha = forms.DateField(label='', widget=forms.TextInput(attrs={'size':14}))
    fecha = forms.DateField(label='', widget=DateWidget(usel10n=False, bootstrap_version=3, attrs={'size':10, 'style':'width:110px'}, options={'format': 'yyyy-mm-dd', 'startView':2, 'language':'es'}))
    meta = forms.FloatField(label='', widget=forms.NumberInput(attrs={'style':'width:90px'}))
    avance_actual = forms.FloatField(label='', widget=forms.NumberInput(attrs={'style':'width:90px'}))
    presupuesto_actividad = forms.FloatField(label='', widget=forms.NumberInput(attrs={'style':'width:180px'}))
    presupuesto_ejecutado = forms.FloatField(label='', widget=forms.NumberInput(attrs={'style':'width:140px'}))
    ejecucion_financiera = forms.FloatField(label='', widget=forms.NumberInput(attrs={'style':'width:130px'}))
    observacion = forms.CharField(label='', widget=forms.TextInput(attrs={'style':'width:140px'}))

    class Meta:
        model = EstadoDeAvance
        exclude = ('actividad','usuario')

class VariablePorSedeForm(forms.ModelForm):
    class Meta:
        model = VariablePorSede
        exclude = ('fecha','usuario')

class VariablePorAulaForm(forms.ModelForm):
    class Meta:
        model = VariablePorAula
        exclude = ('fecha','usuario')

class ResumenProyectoForm(forms.ModelForm):
    fecha = forms.DateField(label='', widget=DateWidget(usel10n=False, bootstrap_version=3, attrs={'size':5, 'style':'width:210px'}, options={'format': 'yyyy-mm-dd', 'startView':2, 'language':'es'}))

    class Meta:
        model = ResumenProyecto
        exclude = ('usuario',)

class ActaDeSeguimientoForm(forms.ModelForm):
    class Meta:
        model = ActaDeSeguimiento
        exclude = ('fecha','usuario','activo')

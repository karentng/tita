#encoding: utf-8
from django import forms
from .models import *
from datetimewidget.widgets import DateWidget
from django_select2 import AutoModelSelect2Field, Select2MultipleWidget

class EncuestaPadreForm(forms.ModelForm)
    class Meta:
        model = EncuestaPadreFamilia
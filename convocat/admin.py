#encoding:utf-8
from collections import OrderedDict
from django.contrib import admin
from convocat.models import *
# Register your models here.


def readonly(self, request, obj=None):
    if request.user.is_superuser:
        return self.readonly_fields

    if self.declared_fieldsets:
        return flatten_fieldsets(self.declared_fieldsets)
    else:
        return list(
            [field.name for field in self.opts.local_fields] +
            [field.name for field in self.opts.local_many_to_many]
        )




class AcademicaInline(admin.TabularInline):
    model = FormacionAcademica
    get_readonly_fields = readonly

class FormacionTicsAdmin(admin.TabularInline):
    model = FormacionTics
    get_readonly_fields = readonly

class ExperienciaEnsenanzaInline(admin.TabularInline):
    model = ExperienciaFormador
    get_readonly_fields = readonly

class IdiomaInline(admin.TabularInline):
    model = Idioma
    get_readonly_fields = readonly

"""
class ExperienciaOtraAdmin(admin.TabularInline):
    model = ExperienciaOtra
    get_readonly_fields = readonly
"""

class ConocimientoInline(admin.StackedInline):
    model = ConocimientosEspecificos
    get_readonly_fields = readonly

class DocumentosSoporteInline(admin.StackedInline):
    model = DocumentosSoporte
    #get_readonly_fields = readonly


class PuntajeFilter(admin.SimpleListFilter):
    title = "Puntaje"
    parameter_name='punt'

    def lookups(self, request, model_admin):
        return (
            ('39', 'Menos de 40'),
            ('40', 'Entre 40 y 49'),
            ('50', '50 o más'),
        )

    def queryset(self, request, queryset):
        if self.value()=='39':
            return queryset.filter(puntuacion_hv__lte=39)
        elif self.value()=='40':
            return queryset.filter(puntuacion_hv__range=(40,49))
        elif self.value()=='50':
            return queryset.filter(puntuacion_hv__gte=50)
        return queryset

class AspiranteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_completo', 'puntuacion_hv', 'tiene_soportes','numero_inscripcion', 'modificado')
    inlines = [AcademicaInline, FormacionTicsAdmin, ConocimientoInline, IdiomaInline, ExperienciaEnsenanzaInline, DocumentosSoporteInline]
    actions = ['recalcular_puntaje']
    get_readonly_fields = readonly
    search_fields = ('nombre1','apellido1')
    list_filter = (PuntajeFilter,)

    def nombre_completo(self, obj):
        return unicode(obj)

    def tiene_soportes(self, obj):
        return u"✓" if obj.documentossoporte.tiene_soportes() else ''

    def recalcular_puntaje(self, request, queryset):
        for aspirante in queryset:
            if aspirante.puntuacion_hv is not None:
                aspirante.puntuacion_hv = aspirante.calcular_puntaje()
                aspirante.save()


    


#admin.site.register(AreaEnsenanza)
admin.site.register(Aspirante, AspiranteAdmin)
#admin.site.register(Adjunto)

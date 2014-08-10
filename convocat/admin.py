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
    model = ExperienciaEnsenanza
    get_readonly_fields = readonly

class IdiomaInline(admin.TabularInline):
    model = Idioma
    get_readonly_fields = readonly


class ExperienciaOtraAdmin(admin.TabularInline):
    model = ExperienciaOtra
    get_readonly_fields = readonly

class ConocimientoInline(admin.StackedInline):
    model = ConocimientosEspecificos
    get_readonly_fields = readonly

class AspiranteAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'puntuacion_hv')
    inlines = [AcademicaInline, FormacionTicsAdmin, ConocimientoInline, IdiomaInline, ExperienciaEnsenanzaInline, ExperienciaOtraAdmin]

    get_readonly_fields = readonly

    def nombre_completo(self, obj):
        return unicode(obj)



admin.site.register(AreaEnsenanza)
admin.site.register(Aspirante, AspiranteAdmin)


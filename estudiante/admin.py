from django.contrib import admin
from cronograma.models import EventosDiplomado

class EventoAdmin(admin.ModelAdmin):
	model = EventosDiplomado
	list_display = ('nombre', 'fecha_inicio')

admin.site.register(EventosDiplomado, EventoAdmin)

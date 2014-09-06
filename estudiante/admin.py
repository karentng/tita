from django.contrib import admin
from cronograma.models import Evento

class EventoAdmin(admin.ModelAdmin):
	model = Evento
	list_display = ('nombre', 'fecha_inicio')

admin.site.register(Evento, EventoAdmin)

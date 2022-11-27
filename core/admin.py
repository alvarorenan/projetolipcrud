from django.contrib import admin
from .models import Evento

# Register your models here.

class EventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'data', 'created_at', 'descricao', 'usuario')
    list_filter = ('usuario', 'data')

admin.site.register(Evento, EventoAdmin)


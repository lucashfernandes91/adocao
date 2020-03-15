from django.contrib import admin
from apps.ongs.models import Ong

class OngAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade', 'responsavel', 'telefone')

admin.site.register(Ong, OngAdmin)
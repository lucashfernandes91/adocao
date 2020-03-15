from django.contrib import admin
from apps.adocoes_temporarias.models import Adocao_temporaria


class Adocao_temporariaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'cidade')


admin.site.register(Adocao_temporaria, Adocao_temporariaAdmin)
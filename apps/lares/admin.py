from django.contrib import admin
from apps.lares.models import Lar


class LarAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'cidade', 'porte_desejado')


admin.site.register(Lar, LarAdmin)
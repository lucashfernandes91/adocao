from django.contrib import admin
from apps.pets.models import Pet

class PetAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'ong')

admin.site.register(Pet, PetAdmin)

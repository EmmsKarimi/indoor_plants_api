from django.contrib import admin
from .models import Plant

@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'owner', 'date_added')
    search_fields = ('name', 'species')
    list_filter = ('date_added', 'owner')

from django.contrib import admin
from .models import Plant

@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner')  # Removed 'species' and 'date_added'
    search_fields = ('name', 'species')  # 'species' might also be removed
    list_filter = ('owner',)  # Removed 'date_added'

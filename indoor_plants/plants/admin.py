from django.contrib import admin
from .models import Plant

@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'created_at')  # Removed 'species'
    search_fields = ('name',)
    list_filter = ('created_at', 'owner')  # Corrected filter field

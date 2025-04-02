from django.contrib import admin
from .models import Maintenance

@admin.register(Maintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ('plant', 'task_description', 'scheduled_date', 'status')
    search_fields = ('task_description', 'plant__name')
    list_filter = ('status', 'scheduled_date')

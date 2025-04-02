from django.contrib import admin
from .models import Maintenance

@admin.register(Maintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'plant', 'task', 'scheduled_date', 'completed')
    list_filter = ('scheduled_date', 'completed')
    search_fields = ('plant__name', 'task')

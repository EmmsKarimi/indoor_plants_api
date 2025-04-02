from django.contrib import admin
from .models import Maintenance

@admin.register(Maintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'plant', 'task_description', 'scheduled_date', 'status')  # Use correct fields
    list_filter = ('scheduled_date', 'status')  # Use 'status' instead of 'completed'
    search_fields = ('plant__name', 'task_description')  # Correct search fields

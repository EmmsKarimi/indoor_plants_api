from rest_framework import serializers
from .models import Maintenance

class MaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance
        # Fields to be included in the serialized output
        fields = ['id', 'plant', 'task_description', 'scheduled_date', 'status', 'created_at']
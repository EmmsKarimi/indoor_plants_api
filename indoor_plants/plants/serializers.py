from rest_framework import serializers
from .models import Plant

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ['id', 'name', 'description', 'stock_quantity', 'created_at', 'owner']
        read_only_fields = ['owner', 'created_at']  # Owner and created_at are set automatically

    def validate_name(self, value):
        """Ensure plant name is not empty."""
        if not value.strip():
            raise serializers.ValidationError("Plant name cannot be empty.")
        return value

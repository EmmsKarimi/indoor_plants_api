from rest_framework import serializers
from .models import Plant

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ['id', 'name', 'description', 'stock_quantity', 'created_at', 'owner']
        read_only_fields = ['owner', 'created_at']

    def validate_name(self, value):
        """Ensure plant name is not empty."""
        if not value.strip():  # Check if the name is empty or consists only of whitespace
            raise serializers.ValidationError("Plant name cannot be empty.")  # Raise a validation error if empty
        return value  # Return the validated name
    
    def validate_stock_quantity(self, value):
        """Ensure stock_quantity is a positive integer."""
        if value < 0:
            raise serializers.ValidationError("Stock quantity cannot be negative.")
        return value  # Return the validated stock quantity

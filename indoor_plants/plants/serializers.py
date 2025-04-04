from rest_framework import serializers
from .models import Plant

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant  # Specify the model to serialize
        fields = ['id', 'name', 'description', 'stock_quantity', 'created_at', 'owner']  # Fields to include in serialization
        read_only_fields = ['owner', 'created_at']  # These fields are set automatically and should not be modified by the user

    def validate_name(self, value):
        """Ensure plant name is not empty."""
        if not value.strip():  # Check if the name is empty or consists only of whitespace
            raise serializers.ValidationError("Plant name cannot be empty.")  # Raise a validation error if empty
        return value  # Return the validated name
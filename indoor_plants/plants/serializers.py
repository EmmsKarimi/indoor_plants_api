from rest_framework import serializers
from .models import Plant

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ['id', 'name', 'species', 'description', 'date_added', 'owner']
        read_only_fields = ['owner', 'date_added']  # Owner and date_added are set automatically

    def validate_name(self, value):
        """Ensure plant name is not empty."""
        if not value.strip():
            raise serializers.ValidationError("Plant name cannot be empty.")
        return value

    def validate_species(self, value):
        """Ensure species name is not empty."""
        if not value.strip():
            raise serializers.ValidationError("Species cannot be empty.")
        return value

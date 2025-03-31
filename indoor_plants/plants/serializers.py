from rest_framework import serializers
from .models import Plant

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ['id', 'name', 'species', 'description', 'date_added', 'owner']
        read_only_fields = ['owner', 'date_added']  # Owner and date_added are set automatically

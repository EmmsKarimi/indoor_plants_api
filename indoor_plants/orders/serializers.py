from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    # Add a read-only field for plant_name (calculated property from the model)
    plant_name = serializers.ReadOnlyField()  # Remove the source argument

    class Meta:
        model = Order  # Specify the model to serialize
        fields = ['id', 'user', 'plant', 'plant_name', 'quantity', 'status', 'created_at', 'updated_at']  # Fields to include in serialization
        read_only_fields = ['user', 'created_at', 'updated_at']  # These fields are set automatically and should not be modified by the user
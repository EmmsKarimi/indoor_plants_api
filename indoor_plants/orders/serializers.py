from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    # Add a read-only field for plant_name (calculated property from the model)
    plant_name = serializers.ReadOnlyField(source='plant_name')

    class Meta:
        model = Order
        fields = ['id', 'user', 'plant', 'plant_name', 'quantity', 'status', 'created_at', 'updated_at']
        read_only_fields = ['user', 'created_at', 'updated_at']  # user is read-only (set to current user automatically), created_at and updated_at are set automatically

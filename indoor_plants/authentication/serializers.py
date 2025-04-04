from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation

User  = get_user_model()  # Get the custom User model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'password']  # Fields to be serialized
        extra_kwargs = {'password': {'write_only': True}}  # Password should not be read

    def validate_password(self, value):
        try:
            # Validate the password using Django's built-in validators
            password_validation.validate_password(value)
        except ValidationError as e:
            raise serializers.ValidationError({"password": e.messages})  # Raise validation error if invalid
        return value

    def create(self, validated_data):
        # Check for existing username
        if User.objects.filter(username=validated_data['username']).exists():
            raise serializers.ValidationError({"username": "This username is already taken."})
        
        # Check for existing email
        if User.objects.filter(email=validated_data['email']).exists():
            raise serializers.ValidationError({"email": "This email is already registered."})
        
        # Create a new user with the validated data
        user = User.objects.create_user(**validated_data)  # Use create_user to hash the password
        return user
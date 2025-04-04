from django.contrib.auth import authenticate
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token  # Import Token model for token authentication
from rest_framework.permissions import AllowAny

User  = get_user_model()  # Get the custom User model

# Register Serializer for user registration
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Password should not be read

    class Meta:
        model = User
        fields = ['username', 'email', 'password']  # Fields for registration

    def create(self, validated_data):
        # Create a new user with the validated data
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

# Register View for handling user registration
class RegisterView(APIView):
    permission_classes = [AllowAny]  # Allow any user to access this view
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)  # Initialize serializer with request data
        if serializer.is_valid():
            serializer.save()  # Save the new user
            return Response({"message": "User  created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return errors if invalid

# Login View for handling user login and returning a token
class LoginView(APIView):
    permission_classes = [AllowAny]  # Allow any user to access this view
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

# Profile View for retrieving user profile (requires authentication)
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure user is authenticated

    def get(self, request):
        user = request.user  # Get the authenticated user
        return Response({
            "username": user.username,
            "email": user.email,
            "phone_number": getattr(user, "phone_number", None),  # Get phone number if it exists
        })

# Profile Update View for updating user profile (requires authentication)
class ProfileUpdateView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure user is authenticated

    def put(self, request):
        user = request.user  # Get the authenticated user
        username = request.data.get('username')
        email = request.data.get('email')
        phone_number = request.data.get('phone_number')

        # Update fields if provided
        if username:
            user.username = username
        if email:
            user.email = email
        if phone_number:
            user.phone_number = phone_number

        user.save()  # Save changes to the user
        return Response({"message": "Profile updated successfully"})

# Logout View for logging out the user (requires authentication)
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure user is authenticated

    def post(self, request):
        request.user.auth_token.delete()  # Delete the user's token
        return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)
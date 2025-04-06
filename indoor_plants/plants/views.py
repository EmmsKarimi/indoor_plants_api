from rest_framework import generics, permissions
from .models import Plant
from .serializers import PlantSerializer
from rest_framework.permissions import IsAuthenticated
class PlantListCreateView(generics.ListCreateAPIView):
    """Handles listing and creating plants owned by the authenticated user."""
    serializer_class = PlantSerializer  # Specify the serializer to use
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this view

    def get_queryset(self):
        """Return only plants owned by the authenticated user, optimizing queries."""
        return Plant.objects.filter(owner=self.request.user).select_related('owner')  # Filter plants by the logged-in user

    def perform_create(self, serializer):
        """Assign the logged-in user as the owner when creating a plant."""
        serializer.save(owner=self.request.user)  # Save the plant with the current user as the owner

class PlantDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Handles retrieving, updating, and deleting a plant."""
    serializer_class = PlantSerializer  # Specify the serializer to use
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this view

    def get_queryset(self):
        """Ensure users can only access their own plants."""
        return Plant.objects.filter(owner=self.request.user).select_related('owner')  # Filter plants by the logged-in user

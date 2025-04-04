from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer

class OrderListCreateView(generics.ListCreateAPIView):
    """Handles listing and creating orders for the authenticated user."""
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can access this view
    serializer_class = OrderSerializer  # Specify the serializer to use

    def get_queryset(self):
        """Return only orders owned by the authenticated user."""
        return Order.objects.filter(user=self.request.user)  # Filter orders by the logged-in user

    def perform_create(self, serializer):
        """Assign the logged-in user as the user when creating an order."""
        serializer.save(user=self.request.user)  # Save the order with the current user as the owner


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Handles retrieving, updating, and deleting an order."""
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can access this view
    serializer_class = OrderSerializer  # Specify the serializer to use
    queryset = Order.objects.all()  # Get all orders

    def get_queryset(self):
        """Ensure users can only access their own orders."""
        return Order.objects.filter(user=self.request.user)  # Filter orders by the logged-in user
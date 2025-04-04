from django.urls import path
from .views import PlantListCreateView, PlantDetailView  # Import only necessary views

urlpatterns = [
    path('plants/', PlantListCreateView.as_view(), name='plant-list-create'),  # Endpoint for listing and creating plants
    path('plants/<int:pk>/', PlantDetailView.as_view(), name='plant-detail'),  # Endpoint for retrieving, updating, and deleting a specific plant
]
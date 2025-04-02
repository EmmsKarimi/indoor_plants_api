from django.urls import path
from .views import PlantListCreateView, PlantDetailView  # Import only necessary views

urlpatterns = [
    path('plants/', PlantListCreateView.as_view(), name='plant-list-create'),  # List & create plants
    path('plants/<int:pk>/', PlantDetailView.as_view(), name='plant-detail'),  # Retrieve, update, delete a plant
]

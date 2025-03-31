from django.urls import path
from . import views

urlpatterns = [
    path('plants/', views.PlantListCreateView.as_view(), name='plant-list-create'),  # List and create plants
    path('plants/<int:pk>/', views.PlantDetailView.as_view(), name='plant-detail'),  # View, update, delete a specific plant
]

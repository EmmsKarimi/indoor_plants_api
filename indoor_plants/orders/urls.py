from django.urls import path
from . import views

urlpatterns = [
    path('', views.OrderListCreateView.as_view(), name='order-list-create'),  # Endpoint for listing and creating orders
    path('<int:pk>/', views.OrderDetailView.as_view(), name='order-detail'),  # Endpoint for retrieving, updating, and deleting a specific order
]
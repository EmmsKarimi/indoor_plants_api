from django.urls import path
from . import views

urlpatterns = [
    path('', views.OrderListCreateView.as_view(), name='order-list-create'),  # List and create orders
    path('<int:pk>/', views.OrderDetailView.as_view(), name='order-detail'),  # Retrieve, update, or delete specific order
]

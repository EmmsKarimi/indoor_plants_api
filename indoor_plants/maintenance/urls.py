from django.urls import path
from . import views

urlpatterns = [
    path('', views.MaintenanceListView.as_view(), name='maintenance-list'),  # GET and POST
    path('<int:pk>/', views.MaintenanceDetailView.as_view(), name='maintenance-detail'),  # GET, PUT, DELETE
]

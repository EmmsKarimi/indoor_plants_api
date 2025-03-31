from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),  # Registration
    path('login/', views.LoginView.as_view(), name='login'),  # Login
    path('profile/', views.ProfileView.as_view(), name='profile'),  # Profile
    path('profile/update/', views.ProfileUpdateView.as_view(), name='profile-update'),  # Update Profile
]

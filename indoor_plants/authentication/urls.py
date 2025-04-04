from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),  # Endpoint for user registration
    path('login/', views.LoginView.as_view(), name='login'),  # Endpoint for user login
    path('profile/', views.ProfileView.as_view(), name='profile'),  # Endpoint for retrieving user profile
    path('profile/update/', views.ProfileUpdateView.as_view(), name='profile-update'),  # Endpoint for updating user profile
    path('logout/', views.LogoutView.as_view(), name='logout'),  # Endpoint for logging out the user
]
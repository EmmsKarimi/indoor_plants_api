from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User  = get_user_model()  # Get the custom User model

class AuthenticationTests(APITestCase):

    def setUp(self):
        # Create a user for testing
        self.user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword123'
        }
        self.user = User.objects.create_user(**self.user_data)  # Ensure this uses create_user
        self.token = Token.objects.create(user=self.user)  # Create a token for the user
        self.assertIsNotNone(self.user)  # Ensure user is created
        self.assertIsNotNone(self.token)  # Ensure token is created  # Ensure user is created
        
    def test_user_registration(self):
        """Test user registration"""
        url = reverse('register')
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpassword123'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)  # Check if a new user is created

    def test_user_login(self):
        """Test user login"""
        url = reverse('login')  # Ensure this matches your URL configuration
        data = {
            'username': self.user_data['username'],  # This should match the created user's username
            'password': self.user_data['password']   # This should match the created user's password
        }
        response = self.client.post(url, data)
        print(response.data)  # Log the response data for debugging
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)  # Check if token is returned

    def test_profile_retrieval(self):
        """Test retrieving user profile"""
        url = reverse('profile')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)  # Set the token in the header
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.user_data['username'])  # Check username

    def test_profile_update(self):
        """Test updating user profile"""
        url = reverse('profile-update')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)  # Set the token in the header
        data = {
            'username': 'updateduser',
            'email': 'updateduser@example.com',
            'phone_number': '1234567890'
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()  # Refresh the user instance from the database
        self.assertEqual(self.user.username, 'updateduser')  # Check if username is updated
        self.assertEqual(self.user.email, 'updateduser@example.com')  # Check if email is updated

    def test_user_logout(self):
        """Test user logout"""
        url = reverse('logout')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)  # Set the token in the header
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "Logged out successfully")  # Check logout message
        # Check if the token is deleted
        with self.assertRaises(Token.DoesNotExist):
            Token.objects.get(user=self.user)

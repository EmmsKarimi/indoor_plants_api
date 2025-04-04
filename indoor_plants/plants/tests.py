from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Plant
from django.contrib.auth import get_user_model

User  = get_user_model()

class PlantTests(APITestCase):
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        # Create a plant instance for testing
        self.plant = Plant.objects.create(
            name='Test Plant',
            description='A plant for testing',
            stock_quantity=10,
            owner=self.user  # Associate the plant with the user
        )

    def test_list_plants(self):
        """Test retrieving the list of plants owned by the authenticated user."""
        url = reverse('plant-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # We expect one plant

    def test_create_plant(self):
        """Test creating a new plant."""
        url = reverse('plant-list-create')
        data = {
            'name': 'New Plant',
            'description': 'A new plant for testing',
            'stock_quantity': 5
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Plant.objects.count(), 2)  # We should have two plants now
        self.assertEqual(Plant.objects.get(id=response.data['id']).name, 'New Plant')  # Check the name of the created plant

    def test_retrieve_plant(self):
        """Test retrieving a specific plant."""
        url = reverse('plant-detail', args=[self.plant.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.plant.name)  # Check the name of the retrieved plant

    def test_update_plant(self):
        """Test updating an existing plant."""
        url = reverse('plant-detail', args=[self.plant.id])
        data = {
            'name': 'Updated Plant',
            'description': 'An updated plant description',
            'stock_quantity': 15
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.plant.refresh_from_db()  # Refresh the instance from the database
        self.assertEqual(self.plant.name, 'Updated Plant')  # Check the updated name

    def test_delete_plant(self):
        """Test deleting a plant."""
        url = reverse('plant-detail', args=[self.plant.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Plant.objects.count(), 0)  # The plant should be deleted

    def test_unauthenticated_access(self):
        """Test that unauthenticated users cannot access the plant endpoints."""
        self.client.logout()  # Log out the user
        url = reverse('plant-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)  # Should be unauthorized

    def test_access_other_users_plants(self):
        """Test that users cannot access other users' plants."""
        # Create another user and a plant for that user
        other_user = User.objects.create_user(username='otheruser', email='otheruser@example.com', password='otherpassword')
        other_plant = Plant.objects.create(
            name='Other User Plant',
            description='A plant owned by another user',
            stock_quantity=5,
            owner=other_user
        )

        # Attempt to retrieve the other user's plant
        url = reverse('plant-detail', args=[other_plant.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)  # Should not be found
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Maintenance
from plants.models import Plant
from django.contrib.auth import get_user_model

User  = get_user_model()

class MaintenanceTests(APITestCase):
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        # Create a plant instance for testing, associating it with the user
        self.plant = Plant.objects.create(
            name='Test Plant',
            description='A plant for testing',
            stock_quantity=10,
            owner=self.user  # Associate the plant with the user
        )

        # Create a maintenance task instance
        self.maintenance_task = Maintenance.objects.create(
            plant=self.plant,
            task_description='Water the plant',
            scheduled_date='2023-12-01T10:00:00Z',
            status='healthy'
        )

    def test_list_maintenance_tasks(self):
        """Test retrieving the list of maintenance tasks."""
        url = reverse('maintenance-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # We expect one maintenance task

    def test_create_maintenance_task(self):
        """Test creating a new maintenance task."""
        url = reverse('maintenance-list')
        data = {
            'plant': self.plant.id,
            'task_description': 'Fertilize the plant',
            'scheduled_date': '2023-12-02T10:00:00Z',
            'status': 'healthy'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Maintenance.objects.count(), 2)  # We should have two maintenance tasks now

    def test_retrieve_maintenance_task(self):
        """Test retrieving a specific maintenance task."""
        url = reverse('maintenance-detail', args=[self.maintenance_task.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['task_description'], self.maintenance_task.task_description)

    def test_update_maintenance_task(self):
        """Test updating an existing maintenance task."""
        url = reverse('maintenance-detail', args=[self.maintenance_task.id])
        data = {
            'task_description': 'Water the plant thoroughly',
            'status': 'needs_attention'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.maintenance_task.refresh_from_db()  # Refresh the instance from the database
        self.assertEqual(self.maintenance_task.task_description, 'Water the plant thoroughly')
        self.assertEqual(self.maintenance_task.status, 'needs_attention')

    def test_delete_maintenance_task(self):
        """Test deleting a maintenance task."""
        url = reverse('maintenance-detail', args=[self.maintenance_task.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Maintenance.objects.count(), 0)  # The maintenance task should be deleted

    def test_unauthenticated_access(self):
        """Test that unauthenticated users cannot access the maintenance endpoints."""
        self.client.logout()  # Log out the user
        url = reverse('maintenance-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)  # Change to 401
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from plants.models import Plant
from .models import Order

User  = get_user_model()

class OrderTests(APITestCase):
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', email='testuser@example.com', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        # Create a plant instance for testing with the owner set
        self.plant = Plant.objects.create(
            name='Test Plant',
            description='A plant for testing',
            stock_quantity=10,
            owner=self.user  # Set the owner of the plant
        )

        # Create an order instance for testing
        self.order = Order.objects.create(
            user=self.user,
            plant=self.plant,
            quantity=2
        )

    def test_list_orders(self):
        """Test retrieving the list of orders owned by the authenticated user."""
        url = reverse('order-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # We expect one order

    def test_create_order(self):
        """Test creating a new order."""
        url = reverse('order-list-create')
        data = {
            'plant': self.plant.id,
            'quantity': 3
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 2)  # We should have two orders now
        self.assertEqual(Order.objects.get(id=response.data['id']).quantity, 3)  # Check the quantity of the created order

    def test_retrieve_order(self):
        """Test retrieving a specific order."""
        url = reverse('order-detail', args=[self.order.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['quantity'], self.order.quantity)  # Check the quantity of the retrieved order

    def test_update_order(self):
        """Test updating an existing order."""
        url = reverse('order-detail', args=[self.order.id])
        data = {
            'plant': self.plant.id,
            'quantity': 5
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.order.refresh_from_db()  # Refresh the instance from the database
        self.assertEqual(self.order.quantity, 5)  # Check the updated quantity

    def test_delete_order(self):
        """Test deleting an order."""
        url = reverse('order-detail', args=[self.order.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Order.objects.count(), 0)  # The order should be deleted

    def test_unauthenticated_access(self):
        """Test that unauthenticated users cannot access the order endpoints."""
        self.client.logout()  # Log out the user
        url = reverse('order-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)  # Should be unauthorized

    def test_access_other_users_orders(self):
        """Test that users cannot access other users' orders."""
        # Create another user and an order for that user
        other_user = User.objects.create_user(username='otheruser', email='otheruser@example.com', password='otherpassword')
        other_order = Order.objects.create(
            user=other_user,
            plant=self.plant,
            quantity=1
        )

        # Attempt to retrieve the other user's order
        url = reverse('order-detail', args=[other_order.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)  # Should not be found
from django.db import models
from django.contrib.auth import get_user_model
from plants.models import Plant
from django.core.exceptions import ValidationError  # Import for validation

User  = get_user_model()  # Get the user model

class Order(models.Model):
    # Define order statuses
    PENDING = 'Pending'
    COMPLETED = 'Completed'
    CANCELLED = 'Cancelled'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (COMPLETED, 'Completed'),
        (CANCELLED, 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who placed the order
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)  # Plant being ordered
    quantity = models.IntegerField()  # Quantity of the plant ordered
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)  # Order status
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the order was created
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)  # Timestamp when the order was last updated

    def __str__(self):
        return f"Order {self.id} - {self.user.username}"  # String representation of the order

    def set_status(self, status):
        """Set the status of the order."""
        if status not in dict(self.STATUS_CHOICES).keys():
            raise ValueError("Invalid status value")  # Raise error if status is invalid
        self.status = status  # Update the status
        self.save()  # Save the order

    def clean(self):
        """Validate the order before saving."""
        if self.quantity <= 0:
            raise ValidationError("Quantity must be greater than zero.")  # Raise error if quantity is invalid

    @property
    def plant_name(self):
        """Return the name of the plant associated with the order."""
        return self.plant.name  # Access the plant's name
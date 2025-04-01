from django.db import models
from django.contrib.auth import get_user_model
from plants.models import Plant
from django.core.exceptions import ValidationError  # <-- Add this import

User = get_user_model()

class Order(models.Model):
    PENDING = 'Pending'
    COMPLETED = 'Completed'
    CANCELLED = 'Cancelled'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (COMPLETED, 'Completed'),
        (CANCELLED, 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"Order {self.id} - {self.user.username}"

    def set_status(self, status):
        if status not in dict(self.STATUS_CHOICES).keys():
            raise ValueError("Invalid status value")
        self.status = status
        self.save()

    def clean(self):
        if self.quantity <= 0:
            raise ValidationError("Quantity must be greater than zero.")

    @property
    def plant_name(self):
        return self.plant.name

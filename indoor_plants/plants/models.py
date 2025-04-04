from django.db import models
from django.conf import settings

class Plant(models.Model):
    # Model representing a plant
    name = models.CharField(max_length=255)  # Name of the plant
    description = models.TextField()  # Description of the plant
    stock_quantity = models.IntegerField(default=0)  # Quantity of the plant in stock
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the plant was created
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Owner of the plant

    def __str__(self):
        return self.name  # String representation of the plant (its name)
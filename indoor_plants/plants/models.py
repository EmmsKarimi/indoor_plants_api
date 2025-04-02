from django.db import models
from django.conf import settings

class Plant(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    stock_quantity = models.IntegerField(default=0)  # Add stock_quantity as per your schema
    created_at = models.DateTimeField(auto_now_add=True)  # Renamed from date_added
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

from django.db import models
from plants.models import Plant  # Import Plant model

class Maintenance(models.Model):
    STATUS_CHOICES = [
        ('healthy', 'Healthy'),
        ('needs_attention', 'Needs Attention'),
    ]
    
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    task_description = models.TextField()
    scheduled_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='healthy')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Maintenance for {self.plant.name} scheduled on {self.scheduled_date}"

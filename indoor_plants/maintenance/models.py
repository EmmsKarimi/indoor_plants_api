from django.db import models
from plants.models import Plant  # Import Plant model

class Maintenance(models.Model):
    # Choices for the status of the maintenance task
    STATUS_CHOICES = [
        ('healthy', 'Healthy'),
        ('needs_attention', 'Needs Attention'),
    ]
    
    # Foreign key relationship to the Plant model
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    # Description of the maintenance task
    task_description = models.TextField()
    # Date and time when the maintenance is scheduled
    scheduled_date = models.DateTimeField()
    # Current status of the maintenance task
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='healthy')
    # Timestamp for when the maintenance task was created
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # String representation of the maintenance task
        return f"Maintenance for {self.plant.name} scheduled on {self.scheduled_date}"
from django.contrib.auth.models import AbstractUser 
from django.db import models

# Custom User model that extends Django's AbstractUser 
class User(AbstractUser ):
    email = models.EmailField(unique=True)  # Ensure email is unique
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Optional phone number field

    def __str__(self):
        return self.username  # Return the username when the object is printed
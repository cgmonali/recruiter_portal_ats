from django.db import models
from django.core.exceptions import ValidationError
import re

class Candidate(models.Model):
    # Choices for gender field
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)

    def clean(self):
        # Validate age is between 18 and 100
        if not (18 <= self.age <= 100):
            raise ValidationError({'age': 'Age must be between 18 and 100.'})

        # Validate phone number format (digits, +, -, and spaces allowed)
        if not re.match(r'^[\d\+\-\s]+$', self.phone_number):
            raise ValidationError({'phone_number': 'Invalid phone number format.'})

    def __str__(self):
        return self.name

    class Meta:
        # Default ordering by name
        ordering = ['name']
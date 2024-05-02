from django.db import models
from django.contrib.auth.models import User


class Advertisement(models.Model):
    """
    Model for advertisements. One user can have many advertisements.
    availability and ad_image come with a default value.
    """

    availability_choices = [
        ('available', 'Available'),
        ('not_available', 'Not Available'),
        ('reserved', 'Reserved')
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    plant_type = models.CharField(max_length=30)
    availability = models.CharField(
        max_length=32, choices=availability_choices, default='available'
    )
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    contact = models.CharField(max_length=40)
    content = models.TextField(blank=True, max_length=280)
    ad_image = models.ImageField(
        upload_to='images/', default='../placeholder_ad_fj7ldv', blank=True
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.id} {self.title}'

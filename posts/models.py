from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    image_filter_choices = [
        ('_1977', '1977'), 
        ('brannan', 'Brannan'),
        ('earlybird', 'Earlybird'), 
        ('hudson', 'Hudson'),
        ('inkwell', 'Inkwell'), 
        ('lofi', 'Lo-Fi'),
        ('kelvin', 'Kelvin'), 
        ('normal', 'Normal'),
        ('nashville', 'Nashville'), 
        ('rise', 'Rise'),
        ('toaster', 'Toaster'), 
        ('valencia', 'Valencia'),
        ('walden', 'Walden'), 
        ('xpro2', 'X-pro II')
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    post_image = models.ImageField(
        upload_to='images/', default='../placeholder_post_en6vln', blank=True
    )
    image_filter = models.CharField(
        max_length=32, choices=image_filter_choices, default='normal'
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.id} {self.title}'
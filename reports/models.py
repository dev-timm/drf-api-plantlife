from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Report(models.Model):
    report_reason_choices = [
        ('offensive_content', 'Offensive Content'),
        ('foul_language', 'Foul Language'),
        ('other', 'Other')
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='reports', on_delete=models.CASCADE)
    report_reason = models.CharField(
        max_length=32, choices=report_reason_choices, default='Offensive Content'
    )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.report_reason
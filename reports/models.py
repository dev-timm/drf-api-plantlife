from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Report(models.Model):  
    """
    Model for reporting a post. One post can have many reports.
    report_reason comes with a default value.
    """

    report_reason_choices = [
        ('offensive_content', 'Offensive Content'),
        ('foul_language', 'Foul Language'),
        ('other', 'Other')
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='reports', on_delete=models.CASCADE)
    report_reason = models.CharField(
        max_length=32, choices=report_reason_choices, default='offensive_content'
    )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        unique_together = ['owner', 'post']

    def __str__(self):
        return self.report_reason

# Generated by Django 4.2.11 on 2024-05-01 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmark',
            name='content',
        ),
    ]

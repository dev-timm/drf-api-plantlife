# Generated by Django 4.2.11 on 2024-04-19 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisement',
            name='is_available',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='is_for_free',
        ),
        migrations.AddField(
            model_name='advertisement',
            name='availability',
            field=models.CharField(choices=[('available', 'Available'), ('not_available', 'Not Available'), ('reserved', 'Reserved')], default='available', max_length=32),
        ),
    ]

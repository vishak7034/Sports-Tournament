# Generated by Django 4.1.5 on 2024-02-13 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sports_app', '0002_location_sports'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sports',
            old_name='Lname',
            new_name='sportsname',
        ),
    ]

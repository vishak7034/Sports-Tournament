# Generated by Django 4.1.5 on 2024-03-09 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sports_app', '0007_user_reg_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_reg',
            name='count',
        ),
        migrations.AddField(
            model_name='manager_reg',
            name='count',
            field=models.IntegerField(max_length=50, null=True),
        ),
    ]
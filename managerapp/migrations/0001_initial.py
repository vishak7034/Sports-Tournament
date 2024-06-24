# Generated by Django 4.1.5 on 2024-03-09 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sports_app', '0006_organizer_reg_manager_reg'),
    ]

    operations = [
        migrations.CreateModel(
            name='My_Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sports_app.manager_reg')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sports_app.user_reg')),
            ],
        ),
    ]
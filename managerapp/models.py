from django.db import models

from sports_app.models import Manager_Reg, user_reg


# Create your models here.
class My_Team(models.Model):
    manager = models.ForeignKey(Manager_Reg, on_delete=models.CASCADE)
    user = models.ForeignKey(user_reg, on_delete=models.CASCADE)
from django.db import models

from sports_app.models import Manager_Reg, Organizer_Reg, user_reg, Sports
from django.contrib.auth.models import User


class CreateTournament(models.Model):
    organizer = models.ForeignKey(Organizer_Reg,on_delete=models.CASCADE,null=True)
    sports = models.ForeignKey(Sports,on_delete=models.CASCADE,null=True,default='gr')

    location = models.CharField(max_length=50)
    Eventname=models.CharField(max_length=50)
    date=models.DateField(max_length=100,null=True)
    time=models.TimeField(max_length=100,null=True)
    image=models.ImageField()
    description=models.CharField(max_length=1000,null=True)
    fee=models.CharField(max_length=1000,null=True)
    payment=models.CharField(max_length=1000,null=True)

    
class join_tournament(models.Model):
    Tournament = models.ForeignKey(CreateTournament,on_delete=models.CASCADE)
    manager = models.ForeignKey(Manager_Reg,on_delete=models.CASCADE,null=True)
    status=models.CharField(max_length=50)
    payment=models.CharField(max_length=1000,null=True)
    organizer = models.ForeignKey(Organizer_Reg,on_delete=models.CASCADE,null=True)

    
class send_request(models.Model):
    user = models.ForeignKey(user_reg,on_delete=models.CASCADE)
    manager = models.ForeignKey(Manager_Reg,on_delete=models.CASCADE)
    status=models.CharField(max_length=50,null=True)

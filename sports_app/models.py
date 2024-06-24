from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class user_reg(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100,null=True)
    phone_number = models.CharField(max_length=50, null=True)

class UserType(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    
class Manager_Reg(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100,null=True)
    phone_number = models.CharField(max_length=50, null=True) 
    count = models.IntegerField(null=True)

class Organizer_Reg(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100,null=True)
    phone_number = models.CharField(max_length=50, null=True)    
# class Tournament(models.Model):
#     Tname = models.CharField(max_length=100,null=True)
#     date = models.CharField(max_length=50, null=True)
#     Time = models.CharField(max_length=50, null=True)


class location(models.Model):
    Lname=models.CharField(max_length=50)
    def __str__(self):
        return self.Lname
    
    

class Sports(models.Model):
    sportsname=models.CharField(max_length=50)
    def __str__(self):
        return self.sportsname
    
    
    
class Tournament(models.Model):
    sports = models.ForeignKey(Sports,on_delete=models.CASCADE,default='gr')
    location = models.ForeignKey(location,on_delete=models.CASCADE,default='gr')
    tname=models.CharField(max_length=50)
    date=models.DateField(max_length=100,null=True)
    time=models.TimeField(max_length=100,null=True)
    image=models.ImageField()
    description=models.CharField(max_length=1000,null=True)
    







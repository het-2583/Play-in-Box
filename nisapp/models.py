from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class UserModel(AbstractUser):
    userProfile=models.ImageField(upload_to="user")
    type = models.CharField(max_length=20)


    

class addGround(models.Model):
    owner_id = models.ForeignKey(UserModel,on_delete=models.CASCADE)
    box_name = models.CharField(max_length=100)
    location = models.TextField()
    timings  = models.TextField()
    image    = models.ImageField(upload_to='user')
    price    = models.CharField(max_length=5, default="1000")




class Team(models.Model):
    team_name = models.CharField(max_length=100)
    city_town = models.CharField(max_length=100)
    captain_phone = models.CharField(max_length=15, blank=True, null=True)
    captain_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.team_name



class booking(models.Model):
    user_id    = models.ForeignKey(UserModel,on_delete=models.CASCADE,default=1)
    ground_id  = models.ForeignKey(addGround,on_delete=models.CASCADE,default=1)
    sports     = models.CharField(max_length=30,default="cricket")
    day        = models.DateField()
    time       = models.CharField(max_length=10, default="3 PM")
    hours      = models.CharField(max_length=2, default="1")
    

class tournament(models.Model):
    user_id    = models.ForeignKey(UserModel,on_delete=models.CASCADE,default=1)
    logo = models.ImageField(upload_to="user")
    tournament_name = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date = models.DateField()
    category = models.CharField(max_length=30)
    ball_type = models.CharField(max_length=20)
    pitch_type = models.CharField(max_length=30)
    


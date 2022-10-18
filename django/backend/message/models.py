
from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Room(models.Model):
    room_name = models.CharField(max_length=100)
    # online = models.ManyToManyField(to=User, blank=True)
    
class Message(models.Model):
    content = models.TextField()
    room = models.ForeignKey(to=Room, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    



class Offers(models.Model):
    user  = models.ManyToManyField(User)
    offers = models.IntegerField()
   
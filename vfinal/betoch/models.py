 
from django.utils import timezone
from django.db.models import F 
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from datetime import date, datetime, timedelta

# Create your models here.
#:TODO PROPERTY create,filter with price, number of rooms and bed , and property type 
# TODO: filter with cites,area,bathroom
from .property_type import PROPERTY_STATUS,PROPERTY_TYPE


class Rating(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    rate = models.IntegerField(default=0)



   

class Location (models.Model):
    place = models.CharField(max_length=10)




class RequestTour(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    date1 = models.DateField()
    date2 = models.DateField()
    date3 = models.DateField()
    date4 = models.DateField()
    date5 = models.DateField()
    date6 = models.DateField()
    date7  = models.DateField()


class House_Feat(models.Model):

    wifi = models.BooleanField(default=False)
    smoking_allowed = models.BooleanField(default=False)
    gym= models.BooleanField(default=False)
    suna = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    swiming_pool =models.BooleanField(default=False)
    working_space = models.BooleanField(default=False)
    washer = models.BooleanField(default=False)
    balcony = models.BooleanField(default=False)
    elevator = models.BooleanField(default=False)
    security = models.BooleanField(default=False)
    generator = models.BooleanField(default=False)
    water_pump = models.BooleanField(default=False)
    furnished = models.BooleanField(default=False)

    


class PropertyListing(models.Model):

    property_status = models.CharField(choices=PROPERTY_STATUS,max_length=100)            
    location = models.ForeignKey(Location,on_delete=models.CASCADE,related_name='property_location')
    features  = models.ForeignKey(House_Feat,on_delete=models.CASCADE,related_name='property_feat')
    bed_rooms = models.IntegerField()
    rooms = models.IntegerField()
    salon = models.IntegerField()
    kitchen = models.IntegerField()
    bathroom = models.IntegerField()
    property_type = models.CharField(choices=PROPERTY_TYPE,max_length=200,default=None)
    desc  = models.TextField(default='description')
    area = models.FloatField()
    # # tour = models.ForeignKey(RequestTour,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=30,decimal_places=4)
    

class PropertyDetails(models.Model):
    image = models.ImageField(upload_to='home/')
    listings = models.ForeignKey(PropertyListing,on_delete=models.CASCADE,related_name='details')

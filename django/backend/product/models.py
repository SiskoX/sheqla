from email.policy import default
from secrets import choice
from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils.text import slugify 
# Create your models here.
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse
from .gear import  BOOK_CONDITION,BUSINESS_INDUSTRIAL,CLOTH_SHOES_WATCHES_CONDITION,ELECTORINCS,FOOD_BEVERAGES_CONDTION,HEALTH_BEAUTY_CONDTION,MOTORS_CONDTIOND,MOVIES_TV_MUSIC_VIDEO_GAMES_CONDTION,SPARE_PARTS,TOY_CONDITION


class Category(MPTTModel):
  
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    slug = models.SlugField(max_length=255, unique=True,blank=True,null=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
      return reverse('category_detail', args=[str(self.slug)])
    def __str__(self):
        return self.name
        
class Location(models.Model):
    country  = models.CharField(max_length=50, blank=True, null=True)
    city  = models.CharField(max_length=50, blank=True, null=True) 

class CommonInfo(models.Model):
    title = models.CharField(max_length=20)
    item_desc = models.TextField()
    price  = models.FloatField()
    created_time = models.DateTimeField(auto_now_add=True)
    item_location = models.CharField(max_length=50, blank=True, null=True)
    fee = models.FloatField()
    category = TreeForeignKey('Category',null=True,blank=True,on_delete=models.DO_NOTHING)
    item_location =  models.ForeignKey('Location', on_delete=models.CASCADE,blank=True,null=True)
    class Meta:
        abstract =True
        ordering = ['created_time']



class Product(CommonInfo):
    pass
  
class Shoe_Addtional(models.Model):
    baseball = models.BooleanField(default=False)
    cycling = models.BooleanField(default=False)
    boxing = models.BooleanField(default=False)
    beach = models.BooleanField(default=False)
    basketball = models.BooleanField(default=False)
    bodybuliding = models.BooleanField(default=False)
    football = models.BooleanField(default=False)

# class Cloth(models.Model):
#     handmade =models.BooleanField(default=False)
#     color = models.CharField(max_length = 30)
#     brand = models.CharField(max_length=40)

class Shoe(CommonInfo):
     
    condition = models.CharField(choices=CLOTH_SHOES_WATCHES_CONDITION, default='None',max_length=20)
    # gender = models.CharField(choice = '')

    # color = models.CharField(choice = '')
    # brand = models.CharField(choice=BRAND,max_length=20, null=True , blank=True)
    release_year = models.DateField()
    # type = models.CharField(choice='')
    shoe_size = models.FloatField()
    
    customized = models.BooleanField(default=False)
    shilhouette  = models.CharField(max_length=50, blank=True, null=True)
    country_manufacture = models.CharField(max_length=20)

class Football(CommonInfo):
 
    team = models.CharField(max_length=20)
    player_name = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
     

    

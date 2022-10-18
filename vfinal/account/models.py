
from datetime import datetime
from pickle import TRUE

from django.db import models
from .account_type import ACCOUNT_TYPE, BANK_ACC
from .subscrption_gear import PLAN,Status
# Create your models here.
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from datetime import datetime, timedelta
from django.utils import timezone

now = timezone.now()
  


# class Subscription(models.Model):
#     active  = models.BooleanField(default=False)
#     create_time = models.DateField()
#     description = models.TextField()
#     plan_name = models.CharField(choices=PLAN, max_length=10)
#     status =models.CharField(choices = Status,max_length=14)
#     tax = models.FloatField()
#     price = models.FloatField()
    
#     subscriber = models.ForeignKey(User, on_delete=models.CASCADE)
    
#     def expried(self):
#         if (self.create_time - now) < datetime.timedelta(days=30):
#             return self.active(False)
#         return None

  
     

class Account(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    fist_name = models.CharField(max_length=100)
    last_name =  models.CharField(max_length=100)
    account_type =  models.CharField(max_length=150, choices=ACCOUNT_TYPE)
    # accnt_type_fliter = AccountManager()
    phone_number = models.IntegerField()
    email = models.EmailField()
    bank_account = models.CharField(max_length=20,choices=BANK_ACC)
    # subscrption = models.ForeignKey(Subscription,on_delete=models.CASCADE)


    

# @receiver(post_save, sender=User)
# def post_save_userprofile_create(sender, instance, created, **kwargs):
#     if created:
        
#        Account.objects.create(user=instance)
       
#     instance.profile.save()

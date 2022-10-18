
from datetime import datetime
from distutils.command.upload import upload
 
 
import uuid
from django.db import models
from .account_type import ACCOUNT_TYPE, BANK_ACC
from .subscription_gear import PLAN,Status
# Create your models here.
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from datetime import datetime, timedelta
from django.utils import timezone
from .gear import PAYMENT_STATUS
from .gear_plan import SUB_PLAN

from .banks import BANKS
 
class Subscription(models.Model):
    active  = models.BooleanField(default=False)
    create_time = models.DateField()
    description = models.TextField()
    plan_name = models.CharField(choices=PLAN, max_length=10)
    status =models.CharField(choices = Status,max_length=14)
    tax = models.FloatField()
    price = models.FloatField()
    
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # def expried(self):
    #     if (self.create_time - now) < datetime.timedelta(days=30):
    #         return self.active(False)
    #     return None

  
 
class BankInfo (models.Model):
    bank_name = models.CharField(max_length=20,choices=BANKS,null=True)

class Billing(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    date = models.DateField(

    )
    amount = models.DecimalField(
        decimal_places=2,max_digits=10
    )
    
    plan = models.CharField(max_length=60,choices=SUB_PLAN , default='free')
    payment_status = models.CharField(max_length=80,choices=PAYMENT_STATUS,default='none')

class Recepit (models.Model):
    image_recipt = models.ImageField()

class Order(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    orderID =models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at  = models.DateTimeField()

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None,related_name='profile')
    account_type = models.CharField(max_length=150,choices=ACCOUNT_TYPE,default='user')
    profile_pic = models.ImageField(upload_to='profile/',blank=True)
    # subscription = models.ForeignKey(Subscription,models.DO_NOTHING,null=True)
 
    amount =models.FloatField(null=True,blank=True)
    credit_balance = models.FloatField(
        default=0,
        
 
    )
  
        # credit= self.credit_balance > 5
    


#    credit_balance class Account(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
#     account_type =  models.CharField(max_length=150, choices=ACCOUNT_TYPE)
#     # accnt_type_fliter = AccountManager()
#     profile_pic = models.ImageField(upload_to='profile/')
#     phone_number = models.IntegerField()
#     # email = models.EmailField()
#     can_post = models.BooleanField()
#     # bank_account = models.CharField(max_length=20,choices=BANK_ACC)
#     # subscrption = models.ForeignKey(Subscription,on_delete=models.CASCADE)

#     #TODO: ADD subsctipprrion expire
#     # 
 

# @receiver(post_save, sender=User)
# def post_save_userprofile_create(sender, instance, created, **kwargs):
#     if created:
        
#        Account.objects.create(user=instance)
       
#     instance.profile.save()

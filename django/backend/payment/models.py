
from django.db import models
from .bank_name import BANK_NAME
from django.contrib.auth.models import User
# Create your models here.

class BankTransfer(models.Model):
    account_no = models.IntegerField()
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    phone_no = models.IntegerField()
    bank = models.CharField( choices=BANK_NAME, max_length=30)
    receipt = models.ImageField(upload_to='recept/%Y/%m/%d',blank=True,null=True)

class Payment(models.Model):
    cash = models.BooleanField(default=False)
    # online_payment = models.ForeignKey(Online_payment)
    bank_transfer = models.ForeignKey(BankTransfer,on_delete=models.CASCADE)


class Order(models.Model):
    pass
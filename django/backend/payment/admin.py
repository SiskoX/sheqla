from django.contrib import admin

# Register your models here.
from .models import BankTransfer

admin.site.register(BankTransfer)
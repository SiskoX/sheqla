from django.contrib import admin

# Register your models here.
from .models import Subscription,Profile


admin.site.register(Subscription)
admin.site.register(Profile)
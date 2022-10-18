from django.contrib import admin

# Register your models here.
from .models import  House_Feat ,Location,Rating,PropertyListing,PropertyDetails

admin.site.register(PropertyListing)
admin.site.register(House_Feat)
admin.site.register(Location)
admin.site.register(PropertyDetails)
admin.site.register(Rating)


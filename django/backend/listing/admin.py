from django.contrib import admin

# Register your models here.
from .models import  House_Feat,Favourite ,Location,Rating,PropertyListing,PropertyDetails,Leads,ReqTour
 
admin.site.register(PropertyListing)
admin.site.register(House_Feat)
admin.site.register(Location)
admin.site.register(PropertyDetails)
admin.site.register(Rating)
admin.site.register(ReqTour)
admin.site.register(Leads)
admin.site.register(Favourite)

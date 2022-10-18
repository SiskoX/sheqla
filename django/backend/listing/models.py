  
from django.utils import timezone
from django.db.models import F 
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from datetime import date, datetime, timedelta
from django.urls import reverse
# Create your models here.
#:TODO PROPERTY create,filter with price, number of rooms and bed , and property type 
# TODO: filter with cites,area,bathroom
from .property_type import PROPERTY_OPTION, PROPERTY_STATUS,PROPERTY_TYPE
from io import BytesIO
from PIL import Image
from django.template.defaultfilters import slugify  #
from django.core.files import File
import uuid
#image compression method
def compress(image):
    im = Image.open(image)
    im_io = BytesIO() 
    if not im.mode == 'RGB':
        im = im.convert('RGB') 
    im.save(im_io, 'JPEG', quality=60) 
    new_image = File(im_io, name=image.name)
    return new_image
class Rating(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    rate = models.IntegerField(default=0)



class ReqTour(models.Model):

    start = models.DateField()
    end = models.DateField()

class Location (models.Model):
    place = models.CharField(max_length=10)
  
    city = models.CharField(max_length=120,blank=True)



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
    # agent =models.ForeignKey(User,on_delete=models.CASCADE)
   
    # user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    # agent = models.ForeignKey(User,on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name='property_listing')
    created_at = models.DateTimeField(auto_now_add=True)
    property_option = models.CharField(choices=PROPERTY_OPTION,max_length=100)            
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
    tours  = models.ForeignKey(ReqTour,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=30,decimal_places=1)
    property_title = models.CharField(max_length=120)
    listing_status = models.CharField(choices=PROPERTY_STATUS,max_length=10,default='active')
    # leads = models.ForeignKey(Leads,on_delete=models.CASCADE,null=True)
    imageF = models.ImageField(upload_to = 'home/',blank=True)
    slug = models.SlugField(null=True,editable=False,unique=True)
    # property_url = models.URLField(unique=True)

    def get_absolute_url(self):
        return reverse("property-list", kwargs={"slug": self.slug})
    #TODO: ADD count the lisinggs 

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            slugged = self.property_title , self.id
            print(slugged)
            self.slug = slugify(self.property_title + str(self.id))
        return super().save(*args, **kwargs)
class Leads (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    request = models.BooleanField(default=False)
    listings = models.ForeignKey(PropertyListing,on_delete=models.CASCADE,related_name='leads')

class Favourite (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    listing= models.ForeignKey(PropertyListing,on_delete=models.CASCADE,blank=True)
class PropertyDetails(models.Model):
    image = models.ImageField(upload_to='home/',blank=True) 
    listings = models.ForeignKey(PropertyListing,on_delete=models.CASCADE,related_name='details')
   
     
    def save(self, *args, **kwargs):
                new_image = compress(self.image)
                self.image = new_image
                super().save(*args, **kwargs)


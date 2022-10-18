
from email.mime import image
from pyexpat import features
from rest_framework import serializers
from .models import Location,House_Feat,Rating,PropertyListing ,PropertyDetails
import json
from .property_type import PROPERTY_TYPE
from django.contrib.auth.models import User
from django.utils import timezone


class PropertyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyDetails
        fields = ['image']

class UserSerilizers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
                    'username',
                    'first_name',
                    'last_name',
                    'email'
        ]

# class ImageUploadSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Uploads
#         fields = "__all__"


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Location
        fields  = "__all__"

class Home_FeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = House_Feat
        fields = "__all__" 
      


class AllPropertyListing(serializers.ModelSerializer):
    details = PropertyDetailSerializer(many=True)
    class Meta:
        model = PropertyListing
        fields =[
                    'pk',
                    'details',
                    'bed_rooms',
                    'rooms',
                    'property_status',
                    'location',
                    'features',
                    'salon',
                    'kitchen',
                    'desc',
                    'bathroom',
                    'property_type',
                    'area',
                    'price'                    
                    ]

    def create(self,validated_data):
        property_details_data  = validated_data.pop('details')
        
        location_data = validated_data.pop('location')
         
        feature_data = validated_data.pop('features')
        location_ = Location.objects.create(**location_data)
        features_  = House_Feat.objects.create(**feature_data)
       
        listing = PropertyListing.objects.create(**validated_data,location=location_,features=features_)
        for images in property_details_data:
            PropertyDetails.objects.create(**images , listings=listing)
        

       
        return listing

     
 
# class AllPropertyListing(serializers.ModelSerializer):
#     # image  = ImageUploadSerializers()
#     # location = LocationSerializer()
#     # features = Home_FeaturesSerializer()
   
#     class Meta:
#         model = PropertyListing
#         fields = [
#            'pk',
#             'bed_rooms',
#             'rooms',
#             'salon',
#             'kitchen',
#             'bathroom',
#             'property_type',
#             'desc',
#             'area',
#             'price',
#             # 'features',
#             # 'location',
#             'photo', 
             
                    
#         ]
#         depth = 1
#     def create(self,validated_data):
      
#         image_data = validated_data.pop('photo')
        
        
#         t = []
#         for i in image_data:
#             t.append(i)
#         print('listing',i)
#         # location_data = validated_data.pop('location')
#         # features_data = validated_data.pop('features')
#         # location_ = Location.objects.create(**location_data)
#         # features_ = House_Feat.objects.create(**features_data)
        
#         # for img_data in image_data:
#         #     ImageUploads.objects.create(**img_data)
#         # photo_ = ImageUpload.objects.create(**photo_data)
        
#         for file in image_data:
#             listing = PropertyListing.objects.create(photo=file,**validated_data)
     
       
#         return listing 

 
       


class RatingSerializers(serializers.ModelSerializer):
    class Meta :
        model = Rating
        fields = "__all__"



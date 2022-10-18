
from rest_framework import serializers
from .models import Location,House_Feat,Rating,PropertyListing ,PropertyDetails,Leads,ReqTour,Favourite
import json
from .property_type import PROPERTY_TYPE
from django.contrib.auth.models import User





class RequestTourSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReqTour
        fields = '__all__'

        


class UserSerilizers(serializers.ModelSerializer):
   
   
    class Meta:
        model = User
        # fields='__all__'
        fields = [
                    'username',
                    # 'first_name',
                    # 'last_name',
                    # 'email'
        ]

class LeadSerializer(serializers.ModelSerializer):
    user = UserSerilizers()
    class Meta:
        model = Leads
        fields = [
            'user',
            'request'
        ]
class PropertyDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = PropertyDetails
        fields = ['image']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Location
        fields  = "__all__"

class Home_FeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = House_Feat
        fields = "__all__" 
      
class EditListingSerializers(serializers.ModelSerializer):
    class Meta:
        model = PropertyListing
        fields = [ 'listing_status']
    
 

    def update(self, instance, validated_data):
    
        instance.listing_status = validated_data.get('listing_status',instance.listing_status)
        instance.save()
        return instance

class AllPropertyListingSerializers(serializers.ModelSerializer):
  
    leads  = LeadSerializer(many=True)
    tours = RequestTourSerializer()
    details = PropertyDetailsSerializers(many=True)
    location = LocationSerializer()
    features = Home_FeaturesSerializer()
    owner = serializers.HiddenField(
    default=serializers.CurrentUserDefault()
)
    class Meta:
        model = PropertyListing
        fields = [
                    'pk',
                    'owner',
                    'bed_rooms',
                    'rooms',
                    'property_option',
                    'listing_status',
                    'location',
                    'features',
                    'salon',
                    'kitchen',
                    'desc',
                    'bathroom',
                    'property_type',
                    'area',
                    'price',
                    'details' ,
                    'tours',
                    'imageF',
                    'leads',
                    'property_title',
                    'slug',
                    'created_at']
        depth=1
   
class AFavSerializer(serializers.ModelSerializer):
    
    user = serializers.HiddenField(
    default=serializers.CurrentUserDefault()
)
    listing = AllPropertyListingSerializers()
    class Meta:
        model = Favourite
        fields = [
                'user',
                'listing']
    depth  =1
 
class FavSerializer(serializers.ModelSerializer):
    
    user = serializers.HiddenField(
    default=serializers.CurrentUserDefault()
)
    listing = serializers.PrimaryKeyRelatedField( read_only=False,queryset=PropertyListing.objects.all() )

    class Meta:
        model = Favourite
        fields = [
                'user',
                'listing']

    def create(self,validated_data):
        owner = validated_data.pop('user')
        listing_= validated_data.pop('listing')
        fav  = Favourite.objects.create(listing=listing_,user=owner)
        print(fav)
        return fav


class PropertySerializerUrl(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PropertyListing
        fields = [
                    'pk',
                    'owner',
                    'bed_rooms',
                    'rooms',
                    'property_option',
                    'listing_status',
                    'location',
                    'features',
                    'salon',
                    'kitchen',
                    'desc',
                    'bathroom',
                    'property_type',
                    'area',
                    'price',
                    'details' ,
                    'tours',
                    'imageF',
                    'leads',
                    'property_title',
                    'slug',
                    'created_at']

      
        # extra_kwargs = {'lookup_field': 'slug'}
        

class PropertyListingSerializer(serializers.ModelSerializer):
    tours = RequestTourSerializer()
    details = PropertyDetailsSerializers(many=True)
    location = LocationSerializer()
    features = Home_FeaturesSerializer()
    owner = serializers.HiddenField(
    default=serializers.CurrentUserDefault()
)
    # leads = LeadSerializer(many=True)
  
    class Meta:
        model = PropertyListing
        fields =[
                    'pk',
                   
                    'bed_rooms',
                    'rooms',
                    'property_option',
                    'property_title',
                    'location',
                    'features',
                    'salon',
                    'kitchen',
                    'desc',
                    'bathroom',
                    'property_type',
                    'area',
                    'price',
                    'details' ,
                    'imageF',
                    # 'leads',
                    'tours'  ,
                    'owner'
                      
                    ]
        
        
        depth=1

    def create(self,validated_data):
        # leads_data = validated_data.pop('leads')

        tour_data = validated_data.pop('tours')
        image_data = validated_data.pop('details')
       
 
        tour_= ReqTour.objects.create(**tour_data)
        location_data = validated_data.pop('location')
        feature_data = validated_data.pop('features')
        location_ = Location.objects.create(**location_data)
        features_  = House_Feat.objects.create(**feature_data)
        
       
        usser = validated_data.pop('owner')
   
        listing = PropertyListing.objects.create(**validated_data,location=location_,features=features_,tours=tour_  ,owner=usser)
         
        # lead = Leads.objects.create(**leads_data,listings=listing)
 
        for img in image_data:
         
            PropertyDetails.objects.create(**img,listings=listing)
 
        return listing
    
    # def update(self, instance, validated_data):
    
    #     instance.bed_rooms = validated_data.get('bed_rooms',instance.bed_rooms)
    #     instance.rooms = validated_data.get('rooms',instance.rooms)
    #     instance.property_option= validated_data.get('property_option',instance.property_option)
    #     instance.property_title = validated_data.get('property_title',instance.property_title)
    #     instance.kitchen = validated_data.get('kitchen',instance.kitchen)
    #     instance.salon = validated_data.get('salon',instance.salon)
    #     instance.bathroom = validated_data.get('bathroom',instance.bathroom)
    #     instance.property_type = validated_data.get('property_type',instance.property_type)
    #     instance.area = validated_data.get('area',instance.area)
    #     instance.price = validated_data.get('price',instance.price)
    #     instance.imageF = validated_data.get('imageF',instance.imageF)  
    #     # instance.user =request.user     
    #     # instance.tour  = validated_data.get('tour',instance.tour)
    #     # instance.location = validated_data.get('location',instance.location)
    #     # instance.features = validated_data.get('features',instance.features)
    #     instance.save()
    #     image_data = validated_data.pop('details')
    #     # location_data = validated_data.pop('location') 
    #     # loc = json.loads(json.dumps(location_data))
        
    
    #     # features_data  = validated_data.pop('features')
    #     # print('ft_data',location_data)
    #     # # ft_id = features_data.get(,None)
    
    #     # # features_ = House_Feat.objects.get(id=ft_id)
    #     # features_.save()
   
 

    #     # location_  = Location.objects.update_or_create(**loc)
    #     # print(location_)
    #     # location_.save()
        
     
    #     for img in image_data:
    #         item_id = img.get('id', None)
    #         print(item_id,'itemID')
    #         img_=PropertyDetails.objects.get(id=item_id,listings=instance)
    #         img_.image = img.get('image',img_.image)
    #         img_.image.save
    #     return instance
     

       


class RatingSerializers(serializers.ModelSerializer):
    class Meta :
        model = Rating
        fields = "__all__"



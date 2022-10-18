from email.mime import image
from rest_framework import status, viewsets
# Create your views here.
from .models import PropertyListing 
from rest_framework.views import APIView
from .serializers import AllPropertyListing
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import generics
import json
from django_filters.rest_framework import DjangoFilterBackend

from .helper import modify_helper


#TODO: ADD MONTYLY OCCURINNG BILL FOR RENTAL PROPERTY

class PropertyListingsView(APIView):

    permission_classes = [AllowAny]
    parser_classes = [MultiPartParser,FormParser]
    # parser_classes = [FileUploadParser]

    def get(self,request):
        rent_ = PropertyListing.objects.all()
        serializer = AllPropertyListing(rent_,many=True)
       
       
        return Response(serializer.data)

    def post(self,request,format=None):
        data = request.data 
        
        # print ('the original data',data)
        features= data["features"]
        bathroom= data["bathroom"]
        property_type= data["property_type"]
        price = data["price"]
        bedroom = data["bed_rooms"]
        rooms = data["rooms"]
        kitchen= data["kitchen"]
        salon = data["salon"]
        area = data["area"]
        location = data["location"]
        images = dict((request.data).lists())['image']

        modify_data = modify_helper(features,bathroom,property_type,price,bedroom,
                                            rooms,kitchen,salon,area,location,images)
        
    
        print('iam modify',modify_data)
       
         
      
        
        serializers = AllPropertyListing(data=modify_data)
         
        serializers.is_valid(raise_exception = True)
      
        serializers.save()
        
        return Response(serializers.data)
 
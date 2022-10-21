
from asgiref.sync import async_to_sync
 
import time
from acc.serializers import UserSerilizers,ProfileSerializers
from rest_framework import status, viewsets
# Create your views here.
import calendar
from django.views import View
from .models import PropertyDetails, PropertyListing , Favourite
from rest_framework.views import APIView
from .serializers import  PropertySerializerUrl,AllPropertyListingSerializers,AFavSerializer, EditListingSerializers,PropertyListingSerializer,FavSerializer
from rest_framework.permissions import IsAuthenticated ,AllowAny,IsAdminUser,SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import generics
import json
from django_filters.rest_framework import DjangoFilterBackend
from django.http import Http404
from .helper import modify_helper,edit_modifer
from rest_framework import status
from rest_framework.pagination import  LimitOffsetPagination,PageNumberPagination
import datetime
from django.core.serializers.json import DjangoJSONEncoder
from django.http import StreamingHttpResponse
from channels.layers import get_channel_layer
#TODO: ADD MONTYLY OCCURINNG BILL FOR RENTAL PROPERTY
 
from acc.models import Profile
class FavList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    # queryset =Favourite.objects.all()
    serializer_class = AFavSerializer
    def get_queryset(self):
        user = self.request.user
   
        return Favourite.objects.filter(user=user)

class FavApi(APIView):
    permission_classes = [IsAuthenticated]
    # def get(self,request):
    
    #     fav = Favourite.objects.filter(user=self.request.user)
    #     serializer = AFavSerializer(fav,many=True)
    #     return Response(serializer.data) 
    def get_object(self, pk  ):
        try:
            usr = self.request.user
           
            return Favourite.objects.get(pk=pk,user=usr)
        except Favourite.DoesNotExist:
            raise Http404
    def post(self,request,format=None):
        data = request.data 
       
        listing_ = request.data["listing"]
      
        # data_ = json.loads(listing_)
  
        serializers  =FavSerializer(data={
            'listing': str(listing_)
        },context={'request': request} )
        serializers.is_valid(raise_exception = True)
       
        serializers.save()
        
            
        return Response(serializers.data)
    
    def delete(self, request, pk, format=None):
        fav = self.get_object(pk)
        fav.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 1000

 

class PropertyListingLLL(generics.ListAPIView):

    permission_classes = [AllowAny]
    parserclasses = [MultiPartParser,FormParser]
    queryset = PropertyListing.objects.all()
    serializer_class = AllPropertyListingSerializers



class PropertyListingPagView(generics.ListAPIView):
    
  
    # queryset = PropertyListing.objects.filter(owner=request.user)
    serializer_class = AllPropertyListingSerializers
    pagination_class = StandardResultsSetPagination
    permission_classes = [AllowAny] 
 
 
    def get_queryset(self):
       
 
        return PropertyListing.objects.all().order_by('-created_at')

 

class AllPropertyListingPagView(APIView):
    

 

    
    # permission_classes = [IsAuthenticated] 
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticated] 
    def get(self,request):
        user = self.request.user
        listings = PropertyListing.objects.filter(owner=user) 

        serializer=AllPropertyListingSerializers(listings,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)
   

# class SearchListings(List)
 

class ListingDetail(generics.RetrieveAPIView):
    permission_classes = [AllowAny] 
    serializer_class =  AllPropertyListingSerializers
    lookup_field = 'slug' 
    def get_queryset(self):
        slug = self.request.query_params.get('slug', None)
        print(slug,'jjuju')
        return PropertyListing.objects.filter(slug=slug)


class PropertyListingsDetailView(APIView,LimitOffsetPagination):
    
    parserclasses = [MultiPartParser,FormParser]
    permission_classes = [AllowAny] 
    
    def get_object(self, pk  ):
        try:
            usr = self.request.user
           
            return PropertyListing.objects.get(pk=pk)
        except PropertyListing.DoesNotExist:
            raise Http404
 
    def get(self, request, pk, format=None):
        listing = self.get_object(pk)
        serializer = AllPropertyListingSerializers(listing)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        data=request.data
      
        listing = self.get_object(pk)
       
        
        listing_status = data["listing_status"]
   
        
        modified_data = edit_modifer(listing_status)
       
        serializer = EditListingSerializers(listing,modified_data )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        listing = self.get_object(pk)
        listing.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

 

class TotalListingsView(APIView):
    permission_classes = [IsAuthenticated] 
    def get(self,request):
        user = self.request.user
        listings = PropertyListing.objects.filter(owner=user).count()

        data= []
        data.append({'total':listings})

        return Response(data,status=status.HTTP_200_OK)

class SoldThisMonthView(APIView):
    permission_classes = [IsAuthenticated] 
    def get(self,request):
        user = request.user
        print(user)
       
        # e = user_acc.filter(credit_balance_gte=9)
        # cre= user_acc.prefetch_related('credit_balance')
        # sere = ProfileSerializers(user_acc,many=True)
        # print (sere.data)
        listings  = PropertyListing.objects.filter(owner=user,listing_status='sold') 
    
        months =[]
        for listing in listings:
            months.append(listing.created_at.date().month)
        
        months = list(set(months))
        months.sort()
     
        data = []
        for month in months:
            data.append({
                'month':calendar.month_name[month],
                'count':PropertyListing.objects.filter(owner=user.id,listing_status='sold').count()

            })
        
        return Response(data,status=status.HTTP_200_OK)

class PropertyListingsView(APIView, LimitOffsetPagination):
    permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    parser_classes = [MultiPartParser,FormParser]
    # parser_classes = [FileUploadParser]

    def get(self,request):
        property_ = PropertyListing.objects.all()
        serializer = AllPropertyListingSerializers(property_,many=True)
        return Response(serializer.data)

    

    def post(self,request,format=None):
       
        data = request.data 
       
        user = request.user
        profile_balance = Profile.objects.filter(credit_balance__lt=5)
        # if (Profile.objects.get(user=user)):pass
        features= data["features"]
        bathroom= data["bathroom"]
        property_type= data["property_type"]
        price = data["price"]
        bedroom = data["bed_rooms"]
        rooms = data["rooms"]
        kitchen= data["kitchen"]
        salon = data["salon"]
        property_title = data["property_title"]
        area = data["area"]
        location = data["location"]
        property_option = data["property_option"]
        tour = data["tour"]
        imageF = data["imageF"]
        #put many images to list
        images = dict((request.data).lists())['image']
        #append to list so that it can loop and put it in nested serializer
        tour_list=[tour]
        tour_listt=[]
        for tours in tour_list:
            tour_listt.append(tours)
      
        # tour_date = datetime.date(tour)
        img_list=[]
        for img in images:
            imgg = dict(image=img)
            img_list.append(imgg)
     
        modified_data = modify_helper(  tour,property_option,features,bathroom,property_type,price,bedroom,
                                            rooms,kitchen,salon,area,location,img_list,property_title,imageF)
          
 
        serializers = PropertyListingSerializer(data=modified_data,context={'request': request} )
   
 
   
        serializers.is_valid(raise_exception = True)
       
        serializers.save()
        user_acc,__ = Profile.objects.get_or_create(user=user) 
        user_acc.credit_balance -= 5
        user_acc.save()
        # channel_layer = get_channel_layer()
        # channel_layer.group_send(
        #      'notification',
        #     {"type": "listings", "text": 'you have posted new listingss'},
        #      )
            
        return Response(serializers.data)
 
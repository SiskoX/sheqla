from unicodedata import category
from django.shortcuts import render

# Create your views here.
from .models import Category, Product,Shoe,Art
from .serializers import CategorySerializer,ProductSerializer, ShoeSerializer,ArtSerializer
from rest_framework.permissions import IsAuthenticated ,AllowAny,IsAdminUser,SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions
from rest_framework.views import APIView
from rest_framework import generics,viewsets
from rest_framework.response import Response
from django.http import Http404

class CategoryDetail(viewsets.ModelViewSet):
    # queryset = Category.objects.all()
    # serializer_class = CategorySerializer
    lookup_field = 'slug'

    def list(self, request,slug):
        queryset = Category.objects.get(slug=slug)
        serializer = CategorySerializer(queryset)
        return Response(serializer.data)

 

 
class CategoryList(generics.ListAPIView):

    permission_classes = [AllowAny]
 
    queryset = Category.objects.filter(level=0)
    serializer_class =CategorySerializer


class ProductView(APIView):

   
    def get(self,request):
        
        listings = Product.objects.all() 

        serializer=ProductSerializer(listings,many=True)

        return Response(serializer.data)
    def post(self,request):
        data = request.data   
        serializers  = ProductSerializer(data=data)
        serializers.is_valid(raise_exception = True)
       
        serializers.save()
        
            
        return Response(serializers.data)

class ShoeView(APIView):

    def get(self,request):
        shoe_ = Shoe.objects.all()
        serializers = ShoeSerializer(shoe_,many=True)
        return Response(serializers.data)

    def post (self,request):
        data = request.data 
        serializer  = ShoeSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class ArtView(APIView):

    def get(self,request):
        art_ = Art.objects.all()
        serializer = ArtSerializer(art_,many=True)
        return Response (serializer.data)
    def post (self,request):
        data = request.data 
        serializer  =  ArtSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
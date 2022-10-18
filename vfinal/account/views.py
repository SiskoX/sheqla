from urllib import request
from django.shortcuts import render


from .permissions import IsSeller,IsAdmin
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework import generics
from .serializers import AccountSerializers, RegisterSerializers,LoginSerializer,UserSerilizers
# Create your views here.
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView 
from .models import Account

from rest_framework.authtoken.models import Token
from rest_framework.response import Response
import json

#TODO;add phone number on regester view

# class SubscriptionView(APIView):
#     permission_classes = [AllowAny]
#     def post (self,request):
#         data = request.data
        
    

class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        data = request.data
        serializer = LoginSerializer(data=data,context={'request':self.request})
        serializer.is_valid(raise_exception=True) 
        
        user = serializer.validated_data['user']
        token,created = Token.objects.get_or_create(user=user)
       
       
        return Response({'token ': token.key}, status = 202)



class RegistrationView(APIView):
    # queryset = User.objects.all()
    
    permission_classes = [AllowAny]
    
    # serializer_class = RegisterSerializers
    def post(self,request):
        
        data = request.data 
        serializer = RegisterSerializers(data=data,context={'request':self.request})
        serializer.is_valid(raise_exception=True)
        account = serializer.save()
        
        token,created = Token.objects.get_or_create(user=account)
        return Response({'token ': token.key}, status = 202)
    
   

class PasswordForgotView():
    pass 

class AccountView(APIView):
    permission_classes = [AllowAny] 
    def get (self,request):
        account = User.objects.all()
        serializer = UserSerilizers(account,many=True)
        return Response(serializer.data)
    



class ChangePassword:
    pass


class SellerView(APIView):
    permission_class = [IsAuthenticated,IsAdmin]
    def get(self, request, format=None):
        content = {
            'status': 'request '
        }
        return Response(content)


from django.shortcuts import render



# Create your views here.
from .models import Room
from .serializers import RoomSerializers
from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework.permissions import IsAuthenticated,AllowAny

class RoomView(APIView):
    permission_classes = [AllowAny]

    def get(self,request):
        room = Room.objects.all()
        serialzers = RoomSerializers(room, many=True)
        return Response(serialzers.data)

    def post (self,request):
        data = request.data 
        serializers = RoomSerializers(data=data)

        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data)



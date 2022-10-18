from .models import Room,Message
from rest_framework import serializers


class RoomSerializers(serializers.ModelSerializer):

    class Meta:
        model = Room 
        fields = "__all__"

class MessageSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Message
        fields = "__all__"

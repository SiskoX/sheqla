from channels.exceptions import StopConsumer
from channels.generic.websocket import JsonWebsocketConsumer
from channels.generic.websocket import WebsocketConsumer
from .models import Room,Message

import json

from asgiref.sync import async_to_sync
class MessageConsumer(WebsocketConsumer):
    # groups = ["broadcast"]
  
    
    print('websocket is connect ----')
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        # connection has to be accepted
        # join the rom group
        Room.objects.create( room_name=self.room_name)
        self.user = self.scope["user"]
        print(self.user)
        async_to_sync(self.channel_layer.group_add)(
            self.room_name,
            self.channel_name,
        )
  
        self.accept()

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # send chat message event to the room
        
        async_to_sync(self.channel_layer.group_send)(
            self.room_name,
            {
                'type': 'message',
                'message': message,
            }
        )
        
    
    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_name,
            self.channel_name,
        )
        

    def message(self, event):
        self.send(text_data=json.dumps(event))
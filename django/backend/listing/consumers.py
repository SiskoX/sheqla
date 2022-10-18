from sqlite3 import connect
from channels.exceptions import StopConsumer
from channels.generic.websocket import JsonWebsocketConsumer
from channels.generic.websocket import WebsocketConsumer
 

import json

from asgiref.sync import async_to_sync



class ListingsConsumer(WebsocketConsumer):
    # groups = ["broadcast"]
  
    
 
    def connect(self):
        # self.room_name = self.scope['url_route']['kwargs']['room_name']
        # connection has to be accepted
        # join the rom group
 
        # self.user = self.scope["user"]
        # print(self.user)
        async_to_sync(self.channel_layer.group_add)("notification", self.channel_name)
  
        self.accept()

    def receive(self, text_data):
        p = dict(x=text_data)
        p['x']
        # p['type']
        print(p)
        async_to_sync(self.channel_layer.group_send)(
            "notification",
            {
                "type": "message",
                "text": text_data,
    
            },
              
        )
        print('====')
        

    def chat_message_echo(self, event):
        print(event)
        self.send_json(event)
    
    def disconnect(self, close_code):
      
        async_to_sync(self.channel_layer.group_discard)(
            'notification',
            self.channel_name,
        )
        

    def message(self, event):
        self.send(text_data=event["text"])
  
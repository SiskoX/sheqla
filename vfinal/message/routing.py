from django.urls import path

from .consumer import MessageConsumer

websocket_urlpatterns = [
    path('ws/message/<room_name>/', MessageConsumer.as_asgi()),
]
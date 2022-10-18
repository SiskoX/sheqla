from django.urls import re_path

from .consumer import MessageConsumer

# websocket_urlpatterns = [
#     re_path('ws/message/<room_name>/', MessageConsumer.as_asgi()),
#     ('r'ws/chat/(?P<room_name>\w+)/$')
# ]

websocket_urlpatterns = [
    re_path(r'ws/message/(?P<room_name>\w+)/$', MessageConsumer.as_asgi()),
]
from django.urls import re_path

from .consumers import ListingsConsumer

# websocket_urlpatterns = [
#     re_path('ws/message/<room_name>/', MessageConsumer.as_asgi()),
#     ('r'ws/chat/(?P<room_name>\w+)/$')
# ]

websocket_urlpatterns = [
    re_path(r"^listings/", ListingsConsumer.as_asgi()),
]
from django.urls import path
from message import views

urlpatterns = [
    path('room/',views.RoomView.as_view(),name="rooom")
]
from django.urls import path
from .views import RegistrationView,LoginView,SellerView,ProfileView
urlpatterns = [
    path('seller/',SellerView.as_view(),name='seller'),
    path('login/',LoginView.as_view(),name='account_login'),
    path('register/',RegistrationView.as_view(),name='account_register'),
    path('profile/',ProfileView.as_view())
]
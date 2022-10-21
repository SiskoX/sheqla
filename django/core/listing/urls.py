from .views import AllPropertyListingPagView,PropertyListingsDetailView,PropertyListingLLL, FavApi ,FavList , PropertyListingsView,PropertyListingsDetailView,SoldThisMonthView,TotalListingsView,PropertyListingPagView
from django.urls import path ,include

 
urlpatterns = [
    path('propertylisting/',PropertyListingPagView.as_view()),
    path('everypropertylisting/',PropertyListingLLL.as_view(),name='propertyall'),
    path('listing/',PropertyListingsView.as_view()),
    path('sold-listing-this-month/',SoldThisMonthView.as_view()),
    path('propertylisting/<str:pk>/',PropertyListingsDetailView.as_view(),name='property-list' ),
    path('total-listings/',TotalListingsView.as_view()),
    path('favourite/',FavList.as_view()),
    path('createfavourite/<int:pk>/',FavApi.as_view()),
 
    path('allpropertylisting/',AllPropertyListingPagView.as_view())

]
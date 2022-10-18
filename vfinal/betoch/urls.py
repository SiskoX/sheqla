from .views import PropertyListingsView
from django.urls import path ,include

# activ_bid_list = ActiveBid.as_view({
#     'get': 'list'
    
# })
urlpatterns = [
    path('propertylisting/',PropertyListingsView.as_view(),name='property-list'),
  

]
from django.db.models.signals import post_save
from channels.layers import get_channel_layer
from .models import PropertyListing
from django.dispatch import receiver
from backend.acc.models import Profile

@receiver(post_save,sender=PropertyListing)
def listingsSignal(self,instance,created):
    posting_fee = 5
    if created:pass
     

        # channel_layer = get_channel_layer()
        # channel_layer.group_send(
        #      'notification',
        #     {"type": "listings", "text": 'you have posted new listingss'},
        #      )
            
        
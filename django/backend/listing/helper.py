
import json
from django.contrib.auth.models import User

def modify_helper ( tour,property_status,features,bathroom,property_type,price,bedroom,
                                            rooms,kitchen,salon,area,location,images,property_title,imageF):

 
    
    ft =json.loads(features)
    tours = json.loads(tour)
    loc =json.loads(location)
#     usr = {'username':str(user)}
#     x = usr.get('username')
#     print (x)
#     usser = User.objects.get(username =x )
#     usrr = {'username':str(usser)}
    dictt ={
        #     'owner':usr,
            'property_title':property_title,    
            'features': ft,
            'bathroom':bathroom,
            'property_type':property_type,
            'price':price,
            'bed_rooms':bedroom,
            'rooms':rooms,
            'kitchen':kitchen,
            'salon':salon,
        #     'tour':tours,
            'location':loc,
            'property_option':property_status,
            'area':area,
            'imageF':imageF,
            'details':images,
            'tours':tours,
    }
    
 
     
 
    
    return dictt
 



def edit_modifer(listing_status):
        dict={
                'listing_status':listing_status
        }
        return dict
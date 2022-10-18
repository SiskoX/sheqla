def modify_helper(features,bathroom,property_type,price,bedroom,
                                            rooms,kitchen,salon,area,location,images):
    dict ={
       
        'features': features,
        
        'bathroom':bathroom,
        'property_type':property_type,
        'price':price,
        'bed_rooms':bedroom,
        'rooms':rooms,
        'kitchen':kitchen,
        'salon':salon,
        
        'location':location,
       
        'area':area,
        'details':[{'image':images}],
    } 
    
    
    return dict
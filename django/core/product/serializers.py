from .models import Art, Product,Category,Shoe
from rest_framework import serializers
from django.db.models import Count
from rest_framework_recursive.fields import RecursiveField
class CategorySerializer(serializers.ModelSerializer):
    # children = serializers.SerializerMethodField(source='get_children')
    children = RecursiveField(many=True)
    class Meta:
        model= Category
        fields =  ['pk','slug','name', 'children']
   
        depth=1
 
   
## make
# class Categorys(serializers.ModelSerializer):
#     name = serializers.CharField(max_length=20)
#     children = RecursiveField(many=True)
#     parent = 
 


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title','description','category','price']


class ShoeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shoe
        fields = '__all__'

class ArtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Art
        fields = '__all__'

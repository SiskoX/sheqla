
from dataclasses import fields
from rest_framework import serializers
from .models import  Billing,Profile
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate, get_user_model

from rest_framework.authtoken.models import Token
from rest_framework.response import Response



# class SubscriptionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Subscription
#         fields =  "__all__"

     




class BillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Billing
        fields = '__all__'


class UserSerilizers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
                    'username',
                    # 'first_name',
                    # 'last_name',
                    # 'email'
        ]
        # fields='__all__'

class ProfileSerializers(serializers.ModelSerializer):
    user = UserSerilizers()
    class Meta:
        model = Profile
        fields =  ['user','amount','credit_balance','profile_pic']
        

class RegisterSerializers(serializers.ModelSerializer):
    # email = serializers.EmailField(
    #     required =True ,
    #     validators = [UniqueValidator(queryset = User.objects.all())]
    # )
    password =serializers.CharField(write_only=True,required =True ,validators = [validate_password])
    password2 = serializers.CharField(write_only=True,required=True)

    class Meta:
        model = User 
        fields = ('username', 'password', 'password2',  'first_name', 'last_name')
        
        extra_kwargs ={
            'first_name':{'required':True},
            'last_name' : {'required':True}
        }

    def validate(self,attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self,validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            # email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name']
        )
       
        user.set_password(validated_data['password'])
        user.save()
       
        return user


class LoginSerializer(serializers.Serializer):
    
# ?username = serializers.CharField(write_only=True,required = True , ${blank=True, null=True})
    username = serializers.CharField(required=True)
    password = serializers.CharField( label="Password",
        # This will be used when the DRF browsable API is enabled
        
        trim_whitespace=False,
        write_only=True)

    class Meta:
        model = User
        fields = ( 'password',  'email')
        

    def validate(self,data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user =authenticate(request=self.context.get('request'),
                                username=username, password=password)
            
            if not user:
                raise serializers.ValidationError({'errormessage':'Unable to login with the information you have provided'})
            
        else:
            raise serializers.ValidationError({'errormessgae':'Must Inculde email and password'})

        data['user'] = user

        return data 

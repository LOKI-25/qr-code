from rest_framework import serializers
from api.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class QRCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qr
        fields = '__all__'


    
class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}


    
class UserLoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if not user:
            raise serializers.ValidationError('Invalid email or password')   
        refresh = RefreshToken.for_user(user)
        return {
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
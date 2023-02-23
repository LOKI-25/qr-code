from rest_framework import serializers
from api.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken



class QRCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qr
        fields = ['text']

    def create(self, validated_data):
        print(validated_data)
        validated_data['user'] = self.context['request'].user
        return Qr.objects.create(**validated_data)


    
class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}


    
class UserLoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password = serializers.CharField()

    

class UserSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(many=True)
    class Meta:
        model = User
        fields = '__all__'
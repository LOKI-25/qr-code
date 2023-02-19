from rest_framework import serializers
from api.models import *


class QRCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qr
        fields = ['id','user','text','qr_code']
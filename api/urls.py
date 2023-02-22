from django.urls import path
from django.conf import settings
from api.views import *



urlpatterns = [
    path('', QRCodeAPIView.as_view(), name='Create Data And Get QR'),
    path('register/', Registerapi.as_view(), name='Register User'),
    path('login/', UserLoginView.as_view(), name='login'),
    
]

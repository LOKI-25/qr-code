from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from api.views import *



urlpatterns = [
    # path('', views. ),
    path('', QRCodeAPIView.as_view(), name='Create Data And Get QR'),
]

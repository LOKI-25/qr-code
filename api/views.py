from rest_framework.response import Response
from api.serializers import QRCodeSerializer
from rest_framework import status
from api.models import *
from rest_framework import generics
# Create your views here.

class QRCodeAPIView(generics.ListCreateAPIView):
    serializer_class = QRCodeSerializer
    queryset = Qr.objects.all()

def post(self, request):
    serializer = QRCodeSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response({
            'status' : True,
            'message' : 'Success',
            'Data' : serializer.data},
            status=status.HTTP_201_CREATED)
    else :
        return Response({
            'status' : False,
            'message' : "Error"},
            status = status.HTTP_400_BAD_REQUEST)
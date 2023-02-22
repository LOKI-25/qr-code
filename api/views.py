from rest_framework.response import Response
from api.serializers import *
from rest_framework import status
from api.models import *
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView



# Create your views here.

class QRCodeAPIView(generics.ListCreateAPIView):
    serializer_class = QRCodeSerializer
    queryset = Qr.objects.all()
    permission_classes=[IsAuthenticated]

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
    
class Registerapi(generics.GenericAPIView):
    serializer_class = RegisterUserSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user":serializer.data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })
    
class UserLoginView(TokenObtainPairView):
    serializer_class = UserLoginSerializer
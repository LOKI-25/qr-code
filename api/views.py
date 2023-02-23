from rest_framework.response import Response
from api.serializers import *
from rest_framework import status
from api.models import *
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated




# Create your views here.

class QRCodeAPIView(generics.ListCreateAPIView):
    serializer_class = QRCodeSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        return Qr.objects.filter(user=self.request.user)

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
        a=serializer.save()
        refresh=RefreshToken.for_user(a)
        return Response({
            "user":serializer.data,
            "message": "User Created Successfully.  Now perform Login to get your token",
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        })
    
class UserLoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer
    queryset=User.objects.all()

    def post(self, request):
        print(request.data['username'],request.data['password'])
        user = User.objects.filter(username=request.data['username'],password=request.data['password']).first()
        print(user)
        if not user:
            raise serializers.ValidationError('Invalid username or password')   
        refresh = RefreshToken.for_user(user)
        return Response( {
            'access': str(refresh.access_token),
            'refresh': str(refresh),
            'message': 'Success',
        })

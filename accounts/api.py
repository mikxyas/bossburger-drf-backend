from .models import User
from rest_framework import viewsets, generics,permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import RegisterSerializer, LoginSerializer,UserSerializer


class UserAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = UserSerializer 
    def get_object(self):
        return self.request.user

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data) 
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user":UserSerializer(user, context=self.get_serializer_context()).data,
            "token":AuthToken.objects.create(user)[1]
        })

# Login Api

class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data) 
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        # sr_user = UserSerializer(user, context=self.get_serializer_context()).data 
        # token = AuthToken.objects.get_or_create(user=sr_user['pk'])
        return Response(user)

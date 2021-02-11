from rest_framework import viewsets, permissions
from .models import User
from .serializers import RegisterSerializer

class RegisterViewSet(viewsets.ModelViewSet):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        if user:
             return Response({
                "user": UserSerializer(user,
                context=self.get_serializer_context()).data
            })
        return Response

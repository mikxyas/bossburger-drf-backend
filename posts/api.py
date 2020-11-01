from rest_framework import viewsets, generics,permissions
from rest_framework.permissions import IsAdminUser,SAFE_METHODS
from .serializers import PostSerializer
from .models import Post
from rest_framework.response import Response

class IsAdminUserOrReadOnly(IsAdminUser):

    def has_permission(self, request, view):
        is_admin = super(
            IsAdminUserOrReadOnly, 
            self).has_permission(request, view)
        # Python3: is_admin = super().has_permission(request, view)
        return request.method in SAFE_METHODS or is_admin

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [
        IsAdminUserOrReadOnly
    ]
    serializer_class = PostSerializer
from rest_framework import viewsets, generics,permissions
from rest_framework.permissions import IsAdminUser,SAFE_METHODS
from .serializers import MenuItemSerializer
from .models import MenuItem
from rest_framework.response import Response

class IsAdminUserOrReadOnly(IsAdminUser):

    def has_permission(self, request, view):
        is_admin = super(
            IsAdminUserOrReadOnly, 
            self).has_permission(request, view)
        # Python3: is_admin = super().has_permission(request, view)
        return request.method in SAFE_METHODS or is_admin

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    permission_classes = [
        IsAdminUserOrReadOnly
    ]
    serializer_class = MenuItemSerializer

# class Open_ClosedViewSet(viewsets.ModelViewSet):
#     queryset = Open_Closed.objects.all()
#     permission_classes = [
#         permissions.AllowAny
#     ]
#     serializer_class = Open_ClosedSerializer
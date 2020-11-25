from rest_framework import viewsets, generics,permissions
from .serializers import OrderSerializer
from .models import Order
from rest_framework.response import Response
from accounts.models import User 
from accounts.serializers import UserSerializer 
from location.models import Location
from menu.models import MenuItem
from rest_framework.permissions import IsAdminUser,SAFE_METHODS

class IsAdminUserOrReadOnly(IsAdminUser):

    def has_permission(self, request, view):
        is_admin = super(
            IsAdminUserOrReadOnly, 
            self).has_permission(request, view)
        # Python3: is_admin = super().has_permission(request, view)
        return request.method in SAFE_METHODS or is_admin


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = OrderSerializer
    
    def get_queryset(self):
        user = self.request.user.id
        orders =  Order.objects.filter(customer=user)
        return orders
    
    def perform_create(self, serializer):
        menuItemId = self.request.data.get('order')
        menuItems = []
        for i in menuItemId:
            menuItem = MenuItem.objects.get(id=i)
            menuItems.append(menuItem)
        print(menuItems)
        # menuItems = MenuItem.objects.filter(id=menuItemId)
        user = User.objects.get(id=self.request.user.id)
        location = self.request.data.get('customer_location')
        return serializer.save(customer={user}, customer_location={location}, order=menuItems)
class AdminOrderViewSet(viewsets.ModelViewSet):
    permission_classes = [
        IsAdminUserOrReadOnly
    ]
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(delivered=False)

class AdminAllOrderViewSet(viewsets.ModelViewSet):
    permission_classes = [
        IsAdminUserOrReadOnly
    ]
    serializer_class = OrderSerializer

    def get_queryset(self):
        orders = Order.objects.all()
        return orders

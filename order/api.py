from rest_framework import viewsets, generics,permissions
from .serializers import OrderSerializer
from .models import Order
from rest_framework.response import Response
from accounts.models import User 
from accounts.serializers import UserSerializer 
from location.models import Location
from menu.models import MenuItem

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
        menuItems = MenuItem.objects.get(id__in=menuItemId)
        user = User.objects.get(id=self.request.user.id)
        location = self.request.data.get('customer_location')
        return serializer.save(customer={user}, customer_location={location}, order={menuItems})
class AdminOrderViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAdminUser
    ]
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(delivered=False)

class AdminAllOrderViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAdminUser
    ]
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.get.all()

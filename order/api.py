from rest_framework import viewsets, generics,permissions
from .serializers import OrderSerializer
from .models import Order
from rest_framework.response import Response
from accounts.models import User 
from accounts.serializers import UserSerializer 

class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = OrderSerializer
    
    def get_queryset(self):
        return self.request.user.customer.all()
    
    def perform_create(self, serializer):
        user = User.objects.get(id=self.request.user)
        return serializer.save(customer=user)
class AdminOrderViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAdminUser
    ]
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(delivered=False)

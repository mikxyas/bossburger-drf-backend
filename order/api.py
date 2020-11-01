from rest_framework import viewsets, generics,permissions
from .serializers import OrderSerializer
from .models import Order
from rest_framework.response import Response


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = OrderSerializer
    
    def get_queryset(self):
        return self.request.user.customer.all()
    
    def perform_create(self, serializer):
        return serializer.save(customer=self.request.user)
   
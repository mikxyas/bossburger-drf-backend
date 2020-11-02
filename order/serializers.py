from .models import Order
from rest_framework import serializers     
from location.models import Location

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['order', 'time_of_order', 'time_of_delivery', 'delivered', 'customer', 'customer_location']
from .models import Order
from rest_framework import serializers     
from location.models import Location
from accounts.serializers import UserSerializer
from location.serializers import LocationSerializer

class OrderSerializer(serializers.ModelSerializer):
    customer = UserSerializer(read_only=True, many=True)
    customer_location = LocationSerializer(read_only=True, many=True)
    class Meta:
        model = Order
        fields = '__all__'
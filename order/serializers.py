from .models import Order
from rest_framework import serializers     
from location.models import Location

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
from .models import MenuItem
from rest_framework import serializers, permissions

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'price', 'img', 'available', 'food_type']

# class Open_ClosedSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Open_Closed
#         fields = '__all__'


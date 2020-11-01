from .models import MenuItem
from rest_framework import serializers, permissions

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'
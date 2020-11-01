from rest_framework import serializers     
from .models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from knox.models import AuthToken


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email','name','phone_number')
        read_only_fields = ('email',)

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    
    class Meta:
        model = User
        fields = ('id','email','password', 'phone_number','name')
    def validate(self, attrs):
        email = attrs.get('email', '')

        if not email:
            raise serializers.ValidationError(
                self.default_error_messages)
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255, min_length=3) 
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)
    # tokens = serializers.SerializerMethodField()


    class Meta:
        model = User
        fields = ('email', 'password')

    def validate(self, attrs):
        email = attrs.get("email", "")
        password = attrs.get("password", "")
        user=auth.authenticate(email=email,password=password)
        if not user:
            raise AuthenticationFailed('Invalid Credentials')
        return {
            'email': user.email,
            'phone_number':user.phone_number,
            'name':user.name,
            'token':user.token()
        }
        return super().validate(attrs)
      
    
from django.contrib.auth.models import User
from rest_framework import serializers
from user.models import UserConfirmation
import random

def generate_confirmation_code():
    return str(random.randint(100000, 999999))

class UserCreateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True)

    def validate_username(self, username):
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError("Пользователь уже существует.")
        return username

class UserRegistrationSerializer(serializers.Serializer):
    username = serializers.CharField()
    confirmation_code = serializers.CharField()

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']
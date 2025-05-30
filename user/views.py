from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from user.models import UserConfirmation
from user.serializers import (
    UserCreateSerializer, 
    UserRegistrationSerializer, 
    generate_confirmation_code, 
    UserProfileSerializer
)
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

class RegisterUserView(APIView):
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.create_user(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password'],
            is_active=False
        )
        code = generate_confirmation_code()
        UserConfirmation.objects.create(user=user, confirmation_code=code)
        return Response({'confirmation_code': code}, status=status.HTTP_201_CREATED)

class ActivateUserView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            confirmation = UserConfirmation.objects.get(
                user__username=serializer.validated_data['username'],
                confirmation_code=serializer.validated_data['confirmation_code']
            )
        except UserConfirmation.DoesNotExist:
            return Response({'detail': 'Неверный код подтверждения.'}, status=400)

        user = confirmation.user
        user.is_active = True
        user.save()
        confirmation.delete()
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)
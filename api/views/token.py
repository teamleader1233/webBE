from rest_framework_simplejwt.views import (
    TokenObtainPairView, 
    TokenRefreshView as BaseTokenRefreshView,
)
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from django.conf import settings

from ..models.user import User


class TokenSingleView(TokenObtainPairView):
    def post(self, request: Request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        
        user = User.objects.get(username=request.data['username'])
        data = {
            'is_staff': user.is_staff,
        }

        response = Response(data, status=status.HTTP_200_OK)
        response.set_cookie(
            key=settings.SIMPLE_JWT['AUTH_COOKIE'],
            value=serializer.validated_data['access'],
            expires=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
            path=settings.SIMPLE_JWT['AUTH_COOKIE_PATH'],
            httponly=False,
            secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
            samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE'],
        )
        return response
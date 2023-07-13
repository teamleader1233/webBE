from django.http import HttpRequest, HttpResponse
from django.core.mail import send_mail, EmailMessage
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings

from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken

import jwt

from ..serializers.register import RegisterUserSerializer
from ..models.user import SvnUser


# Create your views here.
class RegisterCustomerAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = RegisterUserSerializer

    def post(self, request: HttpRequest, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        user = SvnUser.objects.get(email=request.data['email'])
        token = RefreshToken.for_user(user).access_token

        activation_link = ''.join([
            'http://' + get_current_site(request),
            reverse('email-verify'),
            '?token=' + str(token)
        ])
        description = f'{activation_link}'

        email = EmailMessage(
            subject='Kích hoạt tài khoản',
            body=description,
            from_email='kienphamsy257@gmail.com',
            to=[request.data['email']]
        )
        email.send()

        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )
    

class VerifyEmailAPIView(generics.GenericAPIView):
    def get(self, request: HttpRequest):
        token = request.GET.get('token')

        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
            user : SvnUser = SvnUser.objects.get(uuid=payload['uuid'])
            if not user.is_verified:
                user.is_verified = True
                user.save()
            return Response(
                {'status': 1, 'message': 'Email verified successfully'}, 
                status=status.HTTP_201_CREATED)
        
        except jwt.ExpiredSignatureError:
            return Response(
                {'status': 0, 'message': 'Token expired'},
                status=status.HTTP_400_BAD_REQUEST)
        
        except jwt.exceptions.DecodeError:
            return Response(
                {'status': 0, 'message': 'Invalid Token'},
                status=status.HTTP_400_BAD_REQUEST)
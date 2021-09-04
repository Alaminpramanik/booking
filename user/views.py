from django.contrib.auth.models import Permission
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from rest_framework import status

from .serializers import (
    UserRegistrationSerializer,
    ProfileSerializer,
    LoginSerializer,
    EmailVerificationSerializer,
    SetNewPasswordSerializer,
    ResetPasswordEmailRequestSerializer
)
from .models import User

import os
from django.conf import settings
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from .tasks import send_email_to_user
from django.urls import reverse, exceptions
from django.contrib.sites.shortcuts import get_current_site
from rest_framework.authtoken.models import Token


from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.shortcuts import redirect

from rest_framework.views import APIView
from drf_yasg import openapi


class UserRegistrationApiView(generics.CreateAPIView):
    """User registration api view."""
    permission_classes = (AllowAny, )
    serializer_class = UserRegistrationSerializer
    
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        user_data = serializer.data
        user = User.objects.get(email=user_data['email'])
        token, created = Token.objects.get_or_create(user=user)
        current_site = get_current_site(request).domain
        # relativeLink = reverse('email-verify')
        relativeLink = '/email-verify/?token=' + str(token)
        absurl = 'http://'+current_site + relativeLink

        email_body = 'Hi '+user.email + \
            ' Use the link below to verify your email \n' + absurl
        data = {'email_body': email_body, 'to_email': user.email,
                'email_subject': 'Verify your email'}

        send_email_to_user.delay(data)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class VerifyEmail(APIView):
    permission_classes = (AllowAny, )
    serializer_class = EmailVerificationSerializer
    token_param_config = openapi.Parameter(
        'token', in_=openapi.IN_QUERY, description='Description', type=openapi.TYPE_STRING)

    def get(self, request):
        token = request.query_params.get('token')
        try:
            payload = Token.objects.get(key=token)
            user = User.objects.get(id=payload.user_id)
            if not user.is_active:
                user.is_active = True
                user.save()
                return Response({'message': 'Successfully activated'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'User Already Activated'}, status=status.HTTP_200_OK)
        except exceptions as identifier:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)


class LoginApiView(generics.CreateAPIView):
    
    serializer_class = LoginSerializer
    permission_classes = (AllowAny, )
    # authentication_classes = ()

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, 'user': serializer.data.get('user')}, status=status.HTTP_200_OK)


class LogoutApiView(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class ProfileApiView(generics.RetrieveAPIView):

    permission_classes = (AllowAny, )
    authentication_classes = (TokenAuthentication, )
    serializer_class = ProfileSerializer

    def get_queryset(self):
        profile = User.objects.filter(id=self.kwargs.get('pk'))
        return Response({"profile": profile }, status=status.HTTP_200_OK)


class PasswordResetAPIView(generics.GenericAPIView):
    serializer_class = ResetPasswordEmailRequestSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        email = request.data.get('email', '')

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            current_site = get_current_site(request).domain
            # relativeLink = reverse(
            #     'password-reset-confirm', kwargs={'uidb64': uidb64, 'token': token})
            relativeLink = '/forgot-password-verify/?uid=' + str(uidb64) + "&token=" + str(token)
            redirect_url = request.data.get('redirect_url', '')
            absurl = 'http://'+current_site + relativeLink
            email_body = 'Hello,\nUse link below to reset your password\n{}&redirect_url={}'.format(absurl, redirect_url)
            data = {'email_body': email_body, 'to_email': user.email,
                    'email_subject': 'Reset your passsword'}
            send_email_to_user.delay(data)
            return Response({'message': 'We have sent you a link to reset your password'}, status=status.HTTP_200_OK)

        return Response({'message': 'We could not find User at this email address'}, status=status.HTTP_400_BAD_REQUEST)


class PasswordTokenCheckAPI(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def get(self, request, uidb64, token):

        redirect_url = request.GET.get('redirect_url')

        try:
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                if len(redirect_url) > 3:
                    return Response({'message': 'Invalid url', 'url': redirect_url+'?token_valid=False'}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({'message': 'url should not be empty', 'url': os.environ.get('FRONTEND_URL', '')+'?token_valid=False'}, status=status.HTTP_400_BAD_REQUEST)

            if redirect_url and len(redirect_url) > 3:
                return Response({'message': "validation successfull" }, status=status.HTTP_200_OK)
                # return redirect(redirect_url+'?token_valid=True&uidb64=' + uidb64 + '&token=' + token)
            else:
                return Response({'message': os.environ.get('FRONTEND_URL', '')+'?token_valid=False'}, status=status.HTTP_400_BAD_REQUEST)

        except DjangoUnicodeDecodeError as identifier:
            try:
                if not PasswordResetTokenGenerator().check_token(user):
                    return Response({'message': redirect_url+'?token_valid=False'}, status=status.HTTP_400_BAD_REQUEST)
                    
            except UnboundLocalError as e:
                return Response({'error': 'Token is not valid, please request a new one'}, status=status.HTTP_400_BAD_REQUEST)


class SetNewPasswordAPIView(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'success': True, 'message': 'Password reset success'}, status=status.HTTP_200_OK)


class UserProfileApiView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = User.objects.get(email=request.user)
        serializer = ProfileSerializer(instance=user)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)


class UserProfileUpdateApiView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = User.objects.get(email=request.user)
        serializer = ProfileSerializer(instance=user)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

    def put(self, request):
        user = User.objects.get(email=request.user)
        serializer = ProfileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.update(instance=user, validated_data=request.data)
        return Response({'success': True, 'message': 'Profile Updated successfully', 'data': serializer.data}, status=status.HTTP_200_OK)

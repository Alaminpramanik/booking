from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework import exceptions
from .models import User

from rest_framework.exceptions import AuthenticationFailed

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode


class UserRegistrationSerializer(ModelSerializer):
    """User Registration Serializer."""

    class Meta:
        model = User
        fields = ['email', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'},
            }
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
        

class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = User
        fields = ['token']


class ProfileSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'image']

        extra_kwargs = {
                'email': {
                    'read_only': True,
                }
            }

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        print('image  ', validated_data.get('image'))
        if validated_data.get('image'):
            instance.image = validated_data.get('image', instance.image)
        instance.save()

        return instance


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()
    user = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = [ 'email', 'password', 'user']
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'},
            }
        }

    def validate(self, data):
        email = data.get("email", "")
        password = data.get("password", "")

        if email and password:
            user = authenticate(email=email, password=password)
            if user:
                if user.is_active:
                    data["user"] = user
                else:
                    msg = "User is deactivated."
                    raise exceptions.ValidationError(msg)
            else:
                msg = "Unable to login with given credentials."
                raise exceptions.ValidationError(msg)
        else:
            msg = "Must provide username and password both."
            raise exceptions.ValidationError(msg)
        return data


class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()
    redirect_url = serializers.CharField(max_length=500, required=False)

    class Meta:
        fields = ['email']


class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(min_length=6, max_length=68, write_only=True)
    token = serializers.CharField(min_length=1, write_only=True)
    uidb64 = serializers.CharField(min_length=1, write_only=True)

    class Meta:
        fields = ['password', 'token', 'uidb64']

    def validate(self, attrs):
        try:
            password = attrs.get('password')
            token = attrs.get('token')
            uidb64 = attrs.get('uidb64')

            id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed('The reset link is invalid', 401)

            user.set_password(password)
            user.save()

            return user
        except Exception as e:
            raise AuthenticationFailed('The reset link is invalid', 401)

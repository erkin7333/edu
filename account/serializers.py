from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import User


class RegistrSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('image',)
        extra_kwargs = {
            'first_name': {
                'required': True
            },
            'last_name': {
                'required': True
            },
            'email': {
                'required': True
            },
        }


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30, required=True)
    password = serializers.CharField(max_length=30, required=True)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'image',)
        extra_kwargs = {
            'first_name': {
                'required': True
            },
            'last_name': {
                'required': True
            },
            'email': {
                'required': True
            },
        }


class AllProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=30)
    new_password = serializers.CharField(max_length=30)


    def validate_old_password(self, data):
        user = self.context.get('user')

        if not user.check_password(data):
            raise ValidationError({
                "old_password": "Eski parol xato"
            })
        return data

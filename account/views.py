from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.views import APIView
from .serializers import RegistrSerializer, LoginSerializer, ProfileSerializer, AllProfileSerializer, PasswordSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from .models import User


class RegistrationVIEW(APIView):
    permission_classes = (~IsAuthenticated,)

    def post(self, request):
        data = RegistrSerializer(data=request.data)
        if not data.is_valid():
            return Response({
                'status': "fail",
                'data': data.errors
            })
        user = data.save()
        user.set_password(data.validated_data.get('password'))
        user.save()

        return Response({
            'status': 'success'
        })


class LoginVIEW(APIView):
    permission_classes = (~IsAuthenticated,)

    def post(self, request):
        data = LoginSerializer(data=request.data)
        if not data.is_valid():
            return Response({
                'status': "fail",
                'data': data.errors
            })

        user = authenticate(request, **data.validated_data)
        if user is None:
            return Response({
                'status': "fail",
                'data': {
                    "password": ["Login va/yoki parol noto'g'ri"]
                }
            })
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "status": "success",
            "data": {
                "user": ProfileSerializer(user).data,
                'token': token.key
            }
        })


class Logout(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class ProfileVIEW(APIView):

    def get(self, request):
        return Response({
            "status": "success",
            "data": {
                "user": AllProfileSerializer(request.user).data
            }
        })

    def post(self, request):
        data = ProfileSerializer(data=request.data, instance=request.user)
        if not data.is_valid():
            return Response({
                'status': "fail",
                'data': data.errors
            })
        data.save()
        return Response({
            "status": "success"
        })


class PasswordChangeVIEW(APIView):
    def post(self, request):
        data = PasswordSerializer(data=request.data, context={
            "user": request.user
        })
        if not data.is_valid():
            return Response({
                "status": "fail",
                "data": data.errors
            })

        request.user.set_password(data.validated_data.get('new_password'))
        request.user.save()
        return Response({
            "status": "success"
        })


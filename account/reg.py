# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )
# from django.urls import path, include
# from . import views
#
# from knox import views as knox_view
#
# register_logout_url = [
#     path('register/', views.RegisterView.as_view()),
#     path('logout/', views.LogoutView.as_view()),
#     path('validate_activation_code/', views.CheckActivationCodeView.as_view()),
# ]
#
# urlpatterns = [
#     path('', include(register_logout_url)),
#     path('api/token/', TokenObtainPairView.as_view()),
#     path('api/token/refresh/', TokenRefreshView.as_view()),
# ]

# # VIEWS Qismi

from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework_simplejwt.tokens import RefreshToken
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth import get_user_model
from django.http import HttpResponse  # 122-row
from django.shortcuts import redirect
from .models import RegisterCheck
import random




# class RegisterView(APIView):
#     permission_classes = [permissions.AllowAny]
#     authentication_classes = []
#
#     def send_to_email(self, email, model, count, time=datetime.now()):
#         code = str(random.randint(100000, 999999))
#         if count <= 3:
#             if settings.DEBUG:
#                 send_mail('Activation code', 'Your activation code is: ' + code, 'no-replay@gmail.com',
#                           [email], fail_silently=False)
#             model.code = code
#             model.email = email
#             model.count = count + 1
#             model.time = time
#             model.save()
#             return Response({'data': {'status': 'activation code is sent'}})
#         else:
#             return Response({"status": "error", "cause": "please wait 5 minutes"})
#
#     def post(self, request):
#         user = get_user_model()
#         email = request.data.get('email')
#         if not email:
#             return Response(status=404, data={"error": "email not found"})
#         try:
#             user.objects.get(email=email)
#             return Response({'data': {'status': 'error', 'cause': f'{email} already exists'}})
#
#         except user.DoesNotExist:
#             try:
#                 register_check = RegisterCheck.objects.get(email=email)
#                 time_now = datetime.now()
#                 times = register_check.time
#                 time_1 = timedelta(hours=times.hour, minutes=times.minute, seconds=times.second)
#                 time_2 = timedelta(hours=time_now.hour, minutes=time_now.minute, seconds=time_now.second)
#                 time_delta = (time_2 - time_1)
#                 minutes = time_delta.total_seconds() // 60
#                 if register_check.count >= 3:
#                     if minutes >= 5:
#                         count = 0
#                         times = datetime.now()
#                     else:
#                         count = register_check.count
#                 else:
#                     count = register_check.count
#
#                 return self.send_to_email(email=email, model=register_check, count=count, time=times)
#
#             except:
#                 return self.send_to_email(model=RegisterCheck(), email=email, count=0)
#
#
#
# class LogoutView(APIView):
#     permission_classes = [permissions.AllowAny]
#
#     def post(self, request):
#         try:
#             refresh_token = request.data['refresh_token']
#             token_remove = RefreshToken(refresh_token)
#             token_remove.blacklist()
#             return Response({'data': {'status': 'logged out'}})
#         except:
#             return Response(status=300, data={"error": "you are already logged out"})
#
#
# class CheckActivationCodeView(APIView):
#     authentication_classes = [permissions.AllowAny]
#
#     # validating code from email
#     def post(self, request):
#         user = get_user_model()
#         data = request.data
#         email = data['email']
#         try:
#             x = RegisterCheck.objects.get(email=email)
#         except:
#             return Response({"data": {"error": "didn't send activation_code to email"}}, status=400)
#
#         try:
#             user.objects.get(email=email)
#             return Response({"data": {'error': 'email dublicate'}}, status=400)
#         except:
#             pass
#
#         if int(data['activation_code']) == int(x.code):
#             send_mail('Thank you for registration', "if you want more information you may visit fastlogz.com/support",
#                       'no-replay@gmail.com',
#                       [email], fail_silently=False)
#             new_user = user(email=data['email'], password=make_password(data['password']))
#             new_user.save()
#             return Response({'data': {'success': 'Thank you company registered'}}, status=200)
#         return Response({'data': {'error': "activation code didn't match"}}, status=400)
#


# MODEL QIsmi


# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.db import models
# from django.contrib.auth.base_user import BaseUserManager
# from django.conf import settings

# class Admin(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)
#
#
# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password, **extra_fields):
#         if not email:
#             raise ValueError('The Email must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save()
#         return user
#
#     def create_superuser(self, email, password, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_active', True)
#
#         if extra_fields.get('is_staff') is not True:
#             raise ValueError("Superuserda bo'lishi kerak is_staff=True.")
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError("Superuserda bo'lishi kerak is_superuser=True.")
#         return self.create_user(email, password, **extra_fields)
#
#
# class CustomUser(AbstractUser):
#     username = None
#     email = models.EmailField('email address', unique=True)
#     profession = models.ForeignKey("UserProfession", on_delete=models.CASCADE, null=True, blank=True)
#     speciality = models.ForeignKey("UserSpeciality", on_delete=models.CASCADE, null=True, blank=True)
#     mobile_number = models.CharField(max_length=20, null=True, blank=True)
#     image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#     objects = CustomUserManager()
#
#     def __str__(self):
#         return self.email
#
#
# class RegisterCheck(models.Model):
#     email = models.EmailField(unique=True)
#     time = models.TimeField(default=None, blank=True, null=True)
#     code = models.IntegerField()
#     count = models.IntegerField(default=0)
#
#
# class UserProfession(models.Model):
#     title = models.CharField(max_length=245, verbose_name="Profession name")
#
#     class Meta:
#         verbose_name = "User Profession"
#
#     def __str__(self):
#         return self.title
#
#
# class UserSpeciality(models.Model):
#     title = models.CharField(max_length=245, verbose_name="Speciality name:")
#
#     def __str__(self):
#         return self.title

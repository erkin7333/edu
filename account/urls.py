from django.urls import path, include
from . import views



app_name = 'account'



urlpatterns = [
    path('register/', views.RegistrationVIEW.as_view(), name='register'),
    path('login/', views.LoginVIEW.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('profile/', views.ProfileVIEW.as_view(), name='profile'),
    path('changepassword/', views.PasswordChangeVIEW.as_view(), name='changepassword')
]

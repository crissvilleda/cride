"""User Urls"""
#django
from django.urls import path

#views
from cride.users.views import UserLoginAPIView

urlpatterns = [
  path('users/login/',UserLoginAPIView, name='login'),
]
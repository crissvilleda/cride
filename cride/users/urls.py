"""User Urls"""
#django
from django.urls import path, include
#rest framework
from rest_framework.routers import DefaultRouter

#viewsets
from cride.users.views import users as users_views
router = DefaultRouter()
router.register(r'users',users_views.UserViewSet, basename='users')


urlpatterns = [
  path('', include(router.urls))
]
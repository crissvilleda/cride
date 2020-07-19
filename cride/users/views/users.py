"""Users views"""

#Django Rest Framework
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
#Serializers
from cride.users.serializers import (
  UserLoginSerializer, UserModelSerializer,
  UserSignUpSerializer, AccountVerificationSerializer)

class UserViewSet(viewsets.GenericViewSet):
  """User view set
    handle the view's actions for the user
  """

  def get_permissions(self):
    """Assign permitions to the user"""
    permissions = []
    if self.action in ['login', 'signup','verify']:
      permissions.append(AllowAny)
    return [permission() for permission in permissions]


  @action(detail=False, methods=['post'])
  def login(self, request, *args, **kwargs):
    """handle the login of the user"""
    serializer = UserLoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user, token = serializer.save()
    data = {
      'user': UserModelSerializer(user).data,
      'access_token': token
    }

    return Response(data, status=status.HTTP_201_CREATED)

  @action(detail=False, methods=['post'])
  def signup(self,request, *args, **kwargs):
    """handle the sign up of the user"""
    serializer = UserSignUpSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    data = UserModelSerializer(user).data
    return Response(data, status=status.HTTP_201_CREATED)

  @action(detail=False, methods=['post'])
  def verify(self,request, *args, **kwargs):
    """Handle the account verification"""
    serializer = AccountVerificationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    data = {'menssage': 'Congratulation, now go share rides'}
    return Response(data, status=status.HTTP_200_OK)


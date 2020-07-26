"""Users views"""

# Django Rest Framework
from rest_framework import status, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from cride.circles.models import Circle
# Circle Serializer
from cride.circles.serializers import CircleModelSerializer
# model
from cride.users.models import User
# user permission
from cride.users.permissions import IsAccountOwner
# User Serializer
from cride.users.serializers import (
    UserLoginSerializer, UserModelSerializer,
    UserSignUpSerializer, AccountVerificationSerializer)
from cride.users.serializers.profile import ProfileModelSerializer


class UserViewSet(
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet):
    """User view set
        handle the view's actions for the user
    """

    queryset = User.objects.filter(
        is_active=True, is_client=True
    )
    serializer_class = UserModelSerializer
    lookup_field = 'username'

    def get_permissions(self):
        """Assign permitions to the user"""
        permissions = []
        if self.action in ['login', 'signup', 'verify']:
            permissions.append(AllowAny)
        elif self.action in ['retrieve', 'update', 'partial_update']:
            permissions = [IsAuthenticated, IsAccountOwner]
        else:
            permissions = [IsAuthenticated]

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
    def signup(self, request, *args, **kwargs):
        """handle the sign up of the user"""
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def verify(self, request, *args, **kwargs):
        """Handle the account verification"""
        serializer = AccountVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {'menssage': 'Congratulation, now go share rides'}
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['put', 'patch'])
    def profile(self, request, *args, **kwargs):
        """update profile data """
        user = self.get_object()
        profile = user.profile
        partial = request.method == 'PATCH'

        serializer = ProfileModelSerializer(
            profile,
            data=request.data,
            partial=partial
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = UserModelSerializer(user).data
        return Response(data)

    def retrieve(self, request, *args, **kwargs):
        """Add Extra data to the response"""
        response = super(UserViewSet, self).retrieve(request, *args, **kwargs)
        circles = Circle.objects.filter(
            members=request.user,
            membership__is_active=True
        )
        data = {
            'user': response.data,
            'circles': CircleModelSerializer(circles, many=True).data
        }
        response.data = data

        return response

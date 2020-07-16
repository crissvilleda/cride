"""Users views"""

#Django Rest Framework
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
#Serializers
from cride.users.serializers import UserLoginSerializer

from django.views.decorators.csrf import csrf_exempt

class UserLoginAPIView(APIView):
  """User Login API View"""

  def post(self, request, *args, **kwargs):
    """Handle http request"""
    serializer = UserLoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user, token = serializer.save()
    data = {
      'user':'hola',
      'access_token': token
    }
    return Response(data, status=status.HTTP_201_CREATED )

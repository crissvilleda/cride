"""Circles views"""
#django_rest_framework
from rest_framework.decorators import api_view
from rest_framework.response import Response

#models
from cride.circles.models import Circle

#Serializers
from cride.circles.serializers import ( CircleSerializer,
  CreateCircleSerializer)

@api_view(['GET'])
def list_circles(request):
  """list circles."""
  circles = Circle.objects.filter(is_public=True)
  serializer = CircleSerializer(circles, many=True)
  return Response(serializer.data)


@api_view(['POST'])
def create_circle(request):
  """create circles"""
  serializer = CreateCircleSerializer(data=request.data)
  serializer.is_valid(raise_exception=True)
  data = serializer.data
  circle = Circle.objects.create(**data)
  return Response(CircleSerializer(circle).data)

  


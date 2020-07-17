"""Circle View"""
#django rest framework
from rest_framework import viewsets

#models
from cride.circles.models import Circle

#serializer
from cride.circles.serializers import CircleModelSerializer

class CircleViewSet(viewsets.ViewSet):
  queryset = Circle.objects.all()
  serializer_class = CircleModelSerializer
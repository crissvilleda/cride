""" Circle serializers"""
# Django rest framework
from rest_framework import serializers

#models
from cride.circles.models import Circle

class CircleModelSerializer(serializers.ModelSerializer):
  """ Circle model serializer"""
  
  class Meta:
    """meta class"""
    model = Circle
    fields =(
      'id', 'name', 'slug_name',
      'about', 'picture', 
      'rides_offered', 'rides_taken',
      'verified', 'is_public', 'is_limited',
      'members_limit'
    )


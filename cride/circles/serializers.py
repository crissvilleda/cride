"""Circle serializers."""
#django rest framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

#Circle models
from cride.circles.models import Circle

class CircleSerializer(serializers.Serializer):
  """Circle serializer"""
  name = serializers.CharField()
  slug_name = serializers.SlugField()
  rides_taken = serializers.IntegerField()
  rides_offered = serializers.IntegerField()
  members_limit = serializers.IntegerField()


class CreateCircleSerializer(serializers.Serializer):
  """Create circle serializer"""
  name = serializers.CharField(max_length=140)
  slug_name = serializers.CharField(
    max_length=40,
    validators=[
      UniqueValidator(queryset=Circle.objects.all())
    ]
  )
  about = serializers.CharField(
    max_length=255,
    required=False
  )
  picture = serializers.ImageField(
    required=False
  )
  verified = serializers.BooleanField()
  is_public = serializers.BooleanField()
  is_limited = serializers.BooleanField()
  members_limit = serializers.IntegerField()
  

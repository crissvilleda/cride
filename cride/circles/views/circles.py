"""Circle View"""
#django rest framework
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

#models
from cride.circles.models import Circle

#serializer
from cride.circles.serializers import CircleModelSerializer

#permissions
from cride.circles.permissions.circles import IsCircleAdmin

class CircleViewSet(viewsets.ModelViewSet):
  """circle View Set"""
  serializer_class = CircleModelSerializer
  lookup_field = 'slug_name'
  
  def get_queryset(self):
    """Restrict list to public-only."""
    queryset = Circle.objects.all()
    if self.action == 'list':
      return queryset.filter(is_public=True)
    return queryset

  def get_permissions(self):
    """Assign permissions based on actions """
    print('getting permitions')
    permissions = [IsAuthenticated]
    if self.action in ['update', 'partial_update']:
      permissions.append(IsCircleAdmin)
    return [ permission() for permission in permissions ]

  def destroy(self, request, *args, **kwargs):
    """Destroy Circle Function
    This functions has been override in order to stop the 
    ability of removing circles for the users
    
    """
    return Response(status= status.HTTP_204_NO_CONTENT)
  
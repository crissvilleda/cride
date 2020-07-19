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
from cride.circles.permissions.

class CircleViewSet(viewsets.ModelViewSet):
  """circle View Set"""
  queryset = Circle.objects.all()
  serializer_class = CircleModelSerializer
  lookup_field = 'slug_name'

  def get_permissions(self):
    """Assign permissions based on actions """

    permission = [IsAuthenticated]

    if self.action == 'list':


  def destroy(self, request, *args, **kwargs):
    """Destroy Circle Function
    This functions has been override in order to stop the 
    ability of removing circles for the users
    
    """
    return Response(status= status.HTTP_204_NO_CONTENT)
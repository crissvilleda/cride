"""Circle View"""
from rest_framework import status
# django rest framework
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


# models
from cride.circles.models import Circle
# permissions
from cride.circles.permissions.circles import IsCircleAdmin
# serializer
from cride.circles.serializers import CircleModelSerializer


class CircleViewSet(viewsets.ModelViewSet):
    """circle View Set"""
    serializer_class = CircleModelSerializer
    lookup_field = 'slug_name'
    # filters
    filter_backends = (SearchFilter, OrderingFilter,DjangoFilterBackend)
    search_fields = ('slug_name', 'name')
    ordering_fields = ('rides_offered', 'rides_taken', 'name',
                       'created', 'member_limit')
    #ordering = ('-members__count', '-rides_offered', '-rides_taken')
    filter_fields = ('verified','is_limited')

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
        return [permission() for permission in permissions]

    def destroy(self, request, *args, **kwargs):
        """Destroy Circle Function
        This functions has been override in order to stop the
        ability of removing circles for the users

        """
        return Response(status=status.HTTP_204_NO_CONTENT)

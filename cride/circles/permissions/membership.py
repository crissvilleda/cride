"""Membership permitions classes"""

# django rest framework
from rest_framework.permissions import BasePermission

from cride.circles.models import Membership


class IsActiveCircleMember(BasePermission):
    """Allow access only to circle members.
    Expect that the views implementing this perminssion
    have a circle attribute assigned
    """

    def has_permission(self, request, view):
        try:
            Membership.objects.get(
                user=request.user,
                circle=view.circle,
                is_active=True
            )
        except Membership.DoesNotExist:
            return False
        return True


class IsSelfMember(BasePermission):
    """Allow access only to member owners
    """

    def has_permission(self, request, view):
        """lets object permission great access"""
        obj = view.get_object()
        return self.has_object_permission(request, view, obj)

    def has_object_permission(self, request, view, obj):
        """Allow access if member owner by the request user"""
        return request.user == obj.user

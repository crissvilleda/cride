"""User Permission """

# Django rest framework
from rest_framework import permissions


class IsAccountOwner(permissions.BasePermission):
    """Allow access only to objects owned by the requesting user."""

    def has_object_permission(self, request, view, obj):
        """check obj and user are the same"""
        return request.user == obj

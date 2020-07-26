"""Membership Serializer"""

# django
from django.utils import timezone
# django rest Framework
from rest_framework import serializers

from cride.circles.models import Invitation
# models
from cride.circles.models import Membership
# serializer
from cride.users.serializers import UserModelSerializer


class MembershipModelSerializer(serializers.ModelSerializer):
    """Membership model serializer"""

    joined_at = serializers.DateTimeField(source='created', read_only=True)
    invited_by = serializers.StringRelatedField()
    user = UserModelSerializer(read_only=True)

    class Meta:
        """Meta class"""
        model = Membership
        fields = (
            'user', 'is_admin', 'is_active',
            'used_invitations', 'remaining_invitations',
            'invited_by', 'rides_taken', 'rides_offered',
            'joined_at'
        )
        read_only_fields = (
            'user', 'used_invitations', 'invited_by',
            'rides_taken', 'rides_offered'
        )


class AddMemberSerializer(serializers.Serializer):
    """Add member serializer.
    handle the addition of a new member to a circle.
    Circle object must be provided in the context.
    """

    invitation_code = serializers.CharField()
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def validate_user(self, data):
        """ Validate that user ins't member"""
        circle = self.context['circle']
        user = data
        query = Membership.objects.filter(
            circle=circle,
            user=user
        )
        if query.exists():
            raise serializers.ValidationError('User is already member of this circle')
        return data

    def validate_invitation_code(self, data):
        """ verify code exists and that it is related to the circle"""
        try:
            invitation = Invitation.objects.get(
                code=data,
                circle=self.context['circle'],
                used=False
            )

        except Invitation.DoesNotExist:
            raise serializers.ValidationError('Invalid invitation code.')
        self.context['invitation'] = invitation
        return data

    def validate(self, data):
        """verify circle is capable of accepting a new member"""
        circle = self.context['circle']
        if circle.is_limited and circle.members.count() >= circle.members_limit:
            raise serializers.ValidationError('Circle has reached its member limit')
        return data

    def create(self, data):
        """Create new circle member"""
        circle = self.context['circle']
        invitation = self.context['invitation']
        user = data['user']
        now = timezone.now()
        # member creations
        member = Membership.objects.create(
            user=user,
            profile=user.profile,
            circle=circle,
            invited_by=invitation.issued_by
        )
        member.save()
        # update invitation
        invitation.used_by = user
        invitation.used = True
        invitation.used_at = now
        invitation.save()

        # update issuer data
        issuer = Membership.objects.get(
            user=invitation.issued_by,
            circle=circle
        )
        issuer.used_invitations += 1
        issuer.remaining_invitations -= 1
        issuer.save()
        return member

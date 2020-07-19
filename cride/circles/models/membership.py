""""Membership Model"""
from django.db import models

#Utilities
from cride.utils.models import CRideModel


class Membership(CRideModel):
  """Membership Model
    A membership is the table that holds the
    relationshep between a user and circle

  """
  user = models.ForeignKey('users.User', on_delete=models.CASCADE)
  profile = models.ForeignKey('users.Profile',on_delete=models.CASCADE)
  circle = models.ForeignKey('circles.Circle', on_delete=models.CASCADE)
  is_admin = models.BooleanField(
    'circle admin',
    default=False,
    help_text="Circle admins can update circle's data and manage its members"
  )

  #invitations
  used_invitations = models.PositiveIntegerField(default=0)
  remaining_invitations = models.PositiveIntegerField(default=0)
  invited_by = models.ForeignKey(
    'users.User',
    null=True,
    on_delete= models.SET_NULL,
    related_name='invited_by'
  )

  #stats
  rides_taken = models.PositiveIntegerField(default=0)
  rides_offered = models.PositiveIntegerField(default=0)

  #status
  is_active = models.BooleanField(
    'active_status',
    default=True,
    help_text='Only active users are allowed to interact in the circle.'
  )
  def __str__(self):
    """Return username and circle"""
    return f'@{self.user.username} at #{self.circle.slug_name} '


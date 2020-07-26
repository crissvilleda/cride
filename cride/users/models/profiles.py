"""Profile  Model"""

# django
from django.db import models
# Utilities
from cride.utils.models import CRideModel


class Profile(CRideModel):
    """ Profile model.
    A Profile holds a user's public data like biography, picture
    and stadistics.
    """
    user = models.OneToOneField(
        'users.User',
        on_delete=models.CASCADE,
    )
    picture = models.ImageField(
        'profile pictures',
        upload_to='users/pictures/',
        blank=True,
        null=True
    )
    biography = models.TextField(
        max_length=500,
        blank=True
    )

    # stats
    rides_taken = models.PositiveIntegerField(
        default=0
    )
    rides_offered = models.PositiveIntegerField(
        default=0
    )
    reputation = models.FloatField(
        default=5.0,
        help_text='Users reputation base on de rides taken and offered'
    )

    def __str__(self):
        """return user's string representation"""
        return str(self.user)

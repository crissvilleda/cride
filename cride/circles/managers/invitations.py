"""Circle invitation manager"""

# Utilities
import random
from string import ascii_letters, digits

# Django
from django.db import models


class InvitationManager(models.Manager):
    """Invitation manager.
    used to handle de creation
    """
    CODE_LENGTH = 50

    def create(self, **kwargs):
        """handle code creation"""
        pool = ascii_letters + digits + ',-+@$%&*'
        code = kwargs.get('code', ''.join(random.choices(pool, k=self.CODE_LENGTH)))
        while self.filter(code=code).exists():
            code = ''.join(random.choices(pool, k=self.CODE_LENGTH))
        kwargs['code'] = code
        return super(InvitationManager, self).create(**kwargs)

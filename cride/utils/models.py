"""Django Models Utilities..   """

#Django
from django.db import models

class CRideModel(models.Model):
  """comparte ride base model.
  
  CRideModel acts as an abstract base class from which every other
  model in the proyect will inherit. this class provides
  every table with the following attributes:
    +created(DateTime): Store the datetime the object was created
    +modified(DateTime): Store the last datetime the object was modified
  """
  created = models.DateTimeField('created at', 
  auto_now_add=True,
  help_text='Date time on which the object was created'
  )
  modified = models.DateTimeField(
    'modified at',
    auto_now=True,
    help_text='Date time on which the object was last modified'
    )

from django.db import models


# Create your models here.
class AbstractTimeStampedModel(models.Model):
    
    """ TIme Stamped Model"""

    created = models.DateTimeField(auto_now_add=True)  # when created -> automatically add new time
    updates = models.DateTimeField(auto_now=True)  # when updated -> automatically get the new time

    class Meta:
        # abstract model : a model that does not go to DB
        abstract = True


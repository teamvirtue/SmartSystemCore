from django.db import models
from django.conf import settings
from django_extensions.db.models import TimeStampedModel

# Create your models here.
ENUMCHOICES = (
    ('y', 'On'),
    ('n', 'Off'),
)
ENUMGENDER = (
    ('M', 'Male'),
    ('F', 'Female'),
)

class Unit(models.Model):
    unit_for = models.CharField(max_length=45)
    unit = models.CharField(max_length=45)

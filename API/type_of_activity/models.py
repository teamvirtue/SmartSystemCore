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
ENUMFOOD = (
    ('N', 'Not Applicable'),
    ('F', 'Flexitarian'),
    ('P', 'Pascatarian'),
    ('V', 'Vegetarian'),
    ('W', 'Vegan'),
)

class Type_Of_Activity(models.Model):
  activity_type = models.CharField(max_length=45, primary_key=True)
  activity_description = models.CharField(max_length=200, null=True)
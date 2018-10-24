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

class List_Of_All_Possible_Appliances(models.Model):
  appliance_name = models.CharField(max_length=200)
  maximum_kwh = models.FloatField()
  minimum_kwh = models.FloatField()
  last_brightness = models.IntegerField(null=True)
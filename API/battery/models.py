from django.db import models
from django.conf import settings
from django_extensions.db.models import TimeStampedModel
from building.models import Building

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

class Battery(models.Model):
  building_id = models.ForeignKey(Building, on_delete=models.CASCADE, primary_key=True)
  percentage_charged = models.FloatField()
  system_status =  models.CharField(max_length=1, choices=ENUMCHOICES)

from django.db import models
from django.conf import settings
from django_extensions.db.models import TimeStampedModel
from list_of_all_possible_appliance.models import List_Of_All_Possible_Appliances

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
class Appliance_Water_Meter(models.Model):
  avg_water_consumed = models.FloatField()
  meter_status = models.CharField(max_length=1, choices=ENUMCHOICES)
  appliance_id = models.ForeignKey(List_Of_All_Possible_Appliances, on_delete=models.CASCADE)

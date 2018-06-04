from django.db import models
from django.conf import settings
from django_extensions.db.models import TimeStampedModel
from appliance_water_meter.models import Appliance_Water_Meter

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

class Appliance_Water_Meter_Readings(TimeStampedModel):
  water_consumed = models.FloatField()
  reading_time = models.DateTimeField()
  hot_water_reading = models.FloatField()
  cold_water_reading = models.FloatField()
  meter_id = models.ForeignKey(Appliance_Water_Meter, on_delete=models.CASCADE)

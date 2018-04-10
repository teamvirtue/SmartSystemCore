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

class Weather(TimeStampedModel):
  building_id = models.ForeignKey(Building, on_delete=models.CASCADE)
  reading_time = models.DateTimeField()
  temperature = models.FloatField(null=True)
  humidity = models.FloatField(null=True)
  windspeed = models.IntegerField()
  wind_direction = models.IntegerField()
  solar_rediation = models.FloatField(null=True)
  amount_of_CO2 = models.FloatField(null=True)

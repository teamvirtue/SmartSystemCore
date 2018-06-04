from django.db import models
from django.conf import settings
from django_extensions.db.models import TimeStampedModel
from room_water_meter.models import Room_Water_Meter
# Create your models here.
ENUMCHOICES = (
    ('y', 'On'),
    ('n', 'Off'),
)
ENUMGENDER = (
    ('M', 'Male'),
    ('F', 'Female'),
)

class Room_Water_Meter_Readings(TimeStampedModel):
  water_consumed = models.FloatField()
  reading_time = models.DateTimeField()
  hot_water_reading = models.FloatField()
  cold_water_reading = models.FloatField()
  meter_id = models.ForeignKey(Room_Water_Meter, on_delete=models.CASCADE)
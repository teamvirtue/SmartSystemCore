from django.db import models
from django.conf import settings
from django_extensions.db.models import TimeStampedModel
from room.models import Room
from flat.models import Flat

# Create your models here.
ENUMCHOICES = (
    ('y', 'On'),
    ('n', 'Off'),
)
ENUMGENDER = (
    ('M', 'Male'),
    ('F', 'Female'),
)

class Room_Reading(models.Model):
  reading_time = models.DateTimeField(unique=True)
  flat_id = models.ForeignKey(Flat, on_delete=models.CASCADE)
  room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
  temperature = models.FloatField(null=True)
  humidity = models.FloatField(null=True)
  amount_of_CO2 = models.FloatField(null=True)

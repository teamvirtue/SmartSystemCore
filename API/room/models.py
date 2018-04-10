from django.db import models
from django.conf import settings
from django_extensions.db.models import TimeStampedModel
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

class Room(models.Model):
  flat_id = models.OneToOneField(Flat, on_delete=models.CASCADE)
  room_id = models.CharField(max_length=45, unique=True)
  room_name = models.CharField(max_length=45)
  last_humidity = models.FloatField(null=True)
  last_temperature = models.FloatField(null=True)
  last_amount_CO2 = models.FloatField(null=True)
  last_reading_time = models.DateTimeField()
  nr_of_appliances = models.IntegerField()

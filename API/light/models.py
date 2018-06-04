from django.db import models
from django.conf import settings
from django_extensions.db.models import TimeStampedModel
from room.models import Room

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

class Light(models.Model):
  room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
  color_temperature = models.IntegerField()
  brightness = models.IntegerField()
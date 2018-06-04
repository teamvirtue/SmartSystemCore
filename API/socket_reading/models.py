from django.db import models
from django.conf import settings
from django_extensions.db.models import TimeStampedModel
from sockets.models import Sockets

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

class Socket_Reading(TimeStampedModel):
  power_consumed = models.FloatField(null=True)
  reading_time = models.DateTimeField()
  socket_id = models.ForeignKey(Sockets, on_delete=models.CASCADE)

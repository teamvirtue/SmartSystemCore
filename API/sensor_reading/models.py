from django.db import models
from django.conf import settings
from django_extensions.db.models import TimeStampedModel
from sensor.models import Sensor
from unit.models import Unit

# Create your models here.
ENUMCHOICES = (
    ('y', 'On'),
    ('n', 'Off'),
)
ENUMGENDER = (
    ('M', 'Male'),
    ('F', 'Female'),
)

class Sensor_Reading(models.Model):
	sensor_id = models.OneToOneField(Sensor, on_delete=models.CASCADE, unique=True)
	unit_id = models.OneToOneField(Unit, on_delete=models.CASCADE, unique=True)
	which_appliance = models.CharField(max_length=45)

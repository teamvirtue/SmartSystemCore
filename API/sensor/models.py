from django.db import models
from django.conf import settings
from django_extensions.db.models import TimeStampedModel

# Create your models here.
ENUMCHOICES = (
    ('y', 'On'),
    ('n', 'Off'),
)
ENUMGENDER = (
    ('M', 'Male'),
    ('F', 'Female'),
)

class Sensor(models.Model):
	sensor_name = models.CharField(max_length=45)
	sensor_function = models.CharField(max_length=200)

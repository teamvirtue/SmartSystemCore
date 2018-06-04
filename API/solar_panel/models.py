from django.db import models
from django.conf import settings
from django_extensions.db.models import TimeStampedModel
from battery.models import Battery
from building.models import Building
from grid.models import Grid
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

class Solar_Panel(models.Model):
  battery_id = models.ForeignKey(Battery, on_delete=models.CASCADE)
  building_id = models.ForeignKey(Building, on_delete=models.CASCADE)
  grid_id = models.ForeignKey(Grid, on_delete=models.CASCADE)
  energy_generated = models.FloatField()
  system_status = models.CharField(max_length=1, choices=ENUMCHOICES)

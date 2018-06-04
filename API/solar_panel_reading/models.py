from django.db import models
from django.conf import settings
from django_extensions.db.models import TimeStampedModel
from solar_panel.models import Solar_Panel
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

class Solar_Panel_Reading(TimeStampedModel):
  solar_panel_id = models.ForeignKey(Solar_Panel, on_delete=models.CASCADE, primary_key=True)
  energy_generated = models.FloatField()
  send_to_grid = models.CharField(max_length=1, choices=ENUMCHOICES)
  timestamp = models.DateTimeField()


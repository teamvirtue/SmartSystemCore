from django.db import models
from django.conf import settings
from django_extensions.db.models import TimeStampedModel
from family.models import Family

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
class Weekdays(TimeStampedModel):
  day_of_the_week = models.CharField(max_length=45, primary_key=True)
  family_id = models.ForeignKey(Family, on_delete=models.CASCADE)
  work_day_start = models.TimeField()
  work_day_end = models.TimeField()
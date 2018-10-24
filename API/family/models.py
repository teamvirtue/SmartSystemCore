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
ENUMFOOD = (
    ('N', 'Not Applicable'),
    ('F', 'Flexitarian'),
    ('P', 'Pascatarian'),
    ('V', 'Vegetarian'),
    ('W', 'Vegan'),
)

class Family(models.Model):
  house_id = models.ForeignKey(Flat, on_delete=models.CASCADE)
  number_of_members = models.IntegerField()
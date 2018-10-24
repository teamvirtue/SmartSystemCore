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

class Building(models.Model):
     city = models.CharField(max_length=50)
     street = models.CharField(max_length=45)
     postcode = models.CharField(max_length=45)
     country = models.CharField(max_length=45)
     nr_Of_Floors = models.IntegerField()
     building_name = models.CharField(max_length=45)

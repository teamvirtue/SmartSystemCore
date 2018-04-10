from django.db import models
from django.conf import settings
from django_extensions.db.models import TimeStampedModel
from building.models import Building

# Create your models here.
ENUMCHOICES = (
    ('y', 'On'),
    ('n', 'Off'),
)
ENUMGENDER = (
    ('M', 'Male'),
    ('F', 'Female'),
)

class Flat(TimeStampedModel):
    floor_nr = models.IntegerField()
    time_created = models.DateTimeField()
    time_updated = models.DateTimeField()
    flat_type = models.CharField(max_length=45)
    nr_of_people = models.IntegerField()
    building_id = models.ForeignKey(Building, on_delete=models.CASCADE)
    flat_rating = models.FloatField(null=True)

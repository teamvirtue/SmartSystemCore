from django.db import models
from django.conf import settings
from django_extensions.db.models import TimeStampedModel
from flat.models import Flat
from room.models import Room
from appliance_in_building.models import List_Of_All_Appliance_in_building

# Create your models here.
ENUMCHOICES = (
    ('y', 'On'),
    ('n', 'Off'),
)

class Appliance(TimeStampedModel):
    flat_id = models.OneToOneField(Flat, on_delete=models.CASCADE, unique=True, max_length=45)
    room_id = models.OneToOneField(Room, on_delete=models.CASCADE, unique=True, max_length=45)
    appliance_id = models.CharField(unique=True, max_length=45)
    appliance_type_id = models.OneToOneField(List_Of_All_Appliance_in_building, on_delete=models.CASCADE, unique=True)
    appliance_status = models.CharField(max_length=1, choices=ENUMCHOICES)
    last_appliance_energy_consumed = models.FloatField(null=True)
    last_reading_time = models.DateTimeField()
    last_water_reading = models.FloatField(null=True)

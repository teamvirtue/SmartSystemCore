from django.db import models
from django.conf import settings
from django_extensions.db.models import TimeStampedModel
from flat.models import Flat
from room.models import Room
from appliance.models import Appliance
from appliance_in_building.models import List_Of_All_Appliance_in_building



# Create your models here.
ENUMCHOICES = (
    ('y', 'On'),
    ('n', 'Off'),
)

class Appliance_Reading(TimeStampedModel):
    reading_time = models.DateTimeField(unique=True)
    flat_id = models.OneToOneField(Flat, on_delete=models.CASCADE, max_length=45)
    room_id = models.OneToOneField(Room, on_delete=models.CASCADE, max_length=45)
    appliance_id = models.ForeignKey(Appliance, on_delete=models.CASCADE, max_length=45)
    appliance_type_id = models.ForeignKey(List_Of_All_Appliance_in_building, on_delete=models.CASCADE)
    appliance_energy_consumed = models.FloatField(null=True)
    cold_water_reading = models.FloatField(null=True)
    hot_water_reading = models.FloatField(null=True)

from django.db import models
from django.conf import settings
from django_extensions.db.models import TimeStampedModel


# Create your models here.
ENUMCHOICES = (
    ('y', 'On'),
    ('n', 'Off'),
)

class List_Of_All_Appliance_in_building(models.Model):
    appliance_type_id = models.AutoField(primary_key=True,unique=True)
    appliance_name = models.CharField(max_length=45)
    appliance_power = models.IntegerField()

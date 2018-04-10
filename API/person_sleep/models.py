from django.db import models
from django.conf import settings
from django_extensions.db.models import TimeStampedModel
from personal_details.models import Personal_details
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

class Person_Sleep(TimeStampedModel):
     personId = models.OneToOneField(Personal_details, on_delete=models.CASCADE)
     flat_id = models.OneToOneField(Flat, on_delete=models.CASCADE)
     sleep_from = models.DateTimeField()
     sleep_till = models.DateTimeField()
     duration = models.TimeField()

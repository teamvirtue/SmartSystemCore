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

class Personal_details(TimeStampedModel):
    flat_id = models.OneToOneField(Flat, on_delete=models.CASCADE)
    birthdate = models.DateField()
    food_preference = models.CharField(max_length=45)
    last_sleep_from = models.DateTimeField()
    last_sleep_till = models.DateTimeField()
    first_name = models.CharField(max_length=45)
    middle_name = models.CharField(max_length=45, null=True)
    gender = models.CharField(max_length=1, choices=ENUMGENDER)
    age = models.IntegerField()
    email = models.CharField(max_length=45, null=True)
    phone_nr = models.CharField(max_length=45, null=True)

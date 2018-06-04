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

class Personal_Details(TimeStampedModel):
  family_id = models.OneToOneField(Family, on_delete=models.CASCADE, primary_key=True)
  birthdate = models.DateField()
  food_preference = models.CharField(max_length=1, choices=ENUMFOOD)
  last_sleep_from = models.DateTimeField()
  last_sleep_till = models.DateTimeField()
  first_name = models.CharField(max_length=45)
  middle_name = models.CharField(max_length=45, null=True)
  last_name = models.CharField(max_length=45)
  gender =  models.CharField(max_length=1, choices=ENUMGENDER)
  age = models.IntegerField()
  email = models.CharField(max_length=45, null=True)
  phone_nr= models.CharField(max_length=45, null=True)
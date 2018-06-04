from django.db import models
from django.conf import settings
from django_extensions.db.models import TimeStampedModel
from type_of_activity.models import Type_Of_Activity
from personal_detail.models import Personal_Details 
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

class Person_Activity(TimeStampedModel):
  activity_start_time = models.DateTimeField()
  activity_end_time = models.DateTimeField()
  activity_duration = models.TimeField()
  activity_type = models.ForeignKey(Type_Of_Activity, on_delete=models.CASCADE)
  person_id = models.ForeignKey(Personal_Details, on_delete=models.CASCADE)
  family_id = models.ForeignKey(Family, on_delete=models.CASCADE)
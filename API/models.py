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

class Flat(TimeStampedModel):
    floor_nr = models.IntegerField()
    time_created = models.DateTimeField()
    time_updated = models.DateTimeField()
    flat_type = models.CharField(max_length=45)
    nr_of_people = models.IntegerField()
    building_id = models.ForeignKey(Building, on_delete=models.CASCADE)
    flat_rating = models.FloatField(null=True)

class Room(models.Model):
  flat_id = models.OneToOneField(Flat, on_delete=models.CASCADE)
  room_id = models.CharField(max_length=45, unique=True)
  room_name = models.CharField(max_length=45)
  last_humidity = models.FloatField(null=True)
  last_temperature = models.FloatField(null=True)
  last_amount_CO2 = models.FloatField(null=True)
  last_reading_time = models.DateTimeField()
  nr_of_appliances = models.IntegerField()

class Room_Reading(models.Model):
  reading_time = models.DateTimeField(unique=True)
  flat_id = models.ForeignKey(Flat, on_delete=models.CASCADE)
  room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
  temperature = models.FloatField(null=True)
  humidity = models.FloatField(null=True)
  amount_of_CO2 = models.FloatField(null=True)

class Weather(TimeStampedModel):
  building_id = models.ForeignKey(Building, on_delete=models.CASCADE)
  reading_time = models.DateTimeField()
  temperature = models.FloatField(null=True)
  humidity = models.FloatField(null=True)
  windspeed = models.IntegerField()
  wind_direction = models.IntegerField()
  solar_rediation = models.FloatField(null=True)
  amount_of_CO2 = models.FloatField(null=True)

class List_Of_All_Appliance_in_building(models.Model):
    appliance_type_id = models.AutoField(primary_key=True,unique=True)
    appliance_name = models.CharField(max_length=45)
    appliance_power = models.IntegerField()

class Appliance(TimeStampedModel):
    flat_id = models.OneToOneField(Flat, on_delete=models.CASCADE, unique=True, max_length=45)
    room_id = models.OneToOneField(Room, on_delete=models.CASCADE, unique=True, max_length=45)
    appliance_id = models.CharField(unique=True, max_length=45)
    appliance_type_id = models.OneToOneField(List_Of_All_Appliance_in_building, on_delete=models.CASCADE, unique=True)
    appliance_status = models.CharField(max_length=1, choices=ENUMCHOICES)
    last_appliance_energy_consumed = models.FloatField(null=True)
    last_reading_time = models.DateTimeField()
    last_water_reading = models.FloatField(null=True)


class Appliance_Reading(TimeStampedModel):
    reading_time = models.DateTimeField(unique=True)
    flat_id = models.OneToOneField(Flat, on_delete=models.CASCADE, max_length=45)
    room_id = models.OneToOneField(Room, on_delete=models.CASCADE, max_length=45)
    appliance_id = models.ForeignKey(Appliance, on_delete=models.CASCADE, max_length=45)
    appliance_type_id = models.ForeignKey(List_Of_All_Appliance_in_building, on_delete=models.CASCADE)
    appliance_energy_consumed = models.FloatField(null=True)
    cold_water_reading = models.FloatField(null=True)
    hot_water_reading = models.FloatField(null=True)

class Sensor(models.Model):
	sensor_name = models.CharField(max_length=45)
	sensor_function = models.CharField(max_length=200)

class Unit(models.Model):
    unit_for = models.CharField(max_length=45)
    unit = models.CharField(max_length=45)

class Sensor_Reading(models.Model):
	sensor_id = models.OneToOneField(Sensor, on_delete=models.CASCADE, unique=True)
	unit_id = models.OneToOneField(Unit, on_delete=models.CASCADE, unique=True)
	which_appliance = models.CharField(max_length=45)

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

class Person_Sleep(TimeStampedModel):
     personId = models.OneToOneField(Personal_details, on_delete=models.CASCADE)
     flat_id = models.OneToOneField(Flat, on_delete=models.CASCADE)
     sleep_from = models.DateTimeField()
     sleep_till = models.DateTimeField()
     duration = models.TimeField()

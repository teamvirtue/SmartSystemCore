from django.db import models
from django.conf import settings
from django_extensions.db.models import TimeStampedModel

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

class Grid(models.Model):
  total_power_stored = models.FloatField()

class Solar_Panel(models.Model):
  battery_id = models.ForeignKey(Battery, on_delete=models.CASCADE)
  building_id = models.ForeignKey(Battery, on_delete=models.CASCADE)
  grid_id = models.ForeignKey(Grid, on_delete=models.CASCADE)
  energy_generated = models.FloatField()
  system_status = models.CharField(max_length=1, choices=ENUMCHOICES)

class Solar_Panel_Reading(TimeStampedModel):
  solar_panel_id = models.ForeignKey(Solar_Panel, on_delete=models.CASCADE, primary_key=True)
  energy_generated = models.FloatField()
  send_to_grid = models.CharField(max_length=1, choices=ENUMCHOICES)
  timestamp = models.DateTimeField()

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



class Person_Activity(TimeStampedModel):
  activity_start_time = models.DateTimeField()
  activity_end_time = models.DateTimeField()
  activity_duration = models.TimeField()
  activity_type = models.ForeignKey(Types_Of_Activities, on_delete=models.CASCADE)
  person_id = models.ForeignKey(Personal_Details, on_delete=models.CASCADE)
  family_id = models.ForeignKey(Family, on_delete=models.CASCADE)

class Types_Of_Activities(models.Model):
  activity_type = models.CharField(max_length=45, primary_key=True)
  activity_description = models.CharField(max_length=200, null=True)

class Battery(models.Model):
  building_id = models.ForeignKey(Building, on_delete=models.CASCADE, primary_key=True)
  percentage_charged = models.FloatField()
  system_status =  models.CharField(max_length=1, choices=ENUMCHOICES)

class Weekdays(TimeStampedModel):
  day_of_the_week = models.CharField(max_length=45, primary_key=True)
  family_id = models.ForeignKey(Family, on_delete=models.CASCADE)
  work_day_start = models.Timefield()
  work_day_end = models.TimeField()

class Family(models.Model):
  house_id = models.ForeignKey(Flat, on_delete=models.CASCADE)
  number_of_members = models.IntegerField()

class Water_System(models.Model):
  house_id = models.ForeignKey(Flat, on_delete=models.CASCADE, primary_key=True)
  total_usage = models.FloatField()
  system_status = models.CharField(max_length=1, choices=ENUMCHOICES)


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
    building_id = models.ForeignKey(Building, on_delete=models.CASCADE)
    flat_rating = models.FloatField(null=True)
    energy_budget = models.FloatField()

class Room(models.Model):
  flat_id = models.OneToOneField(Flat, on_delete=models.CASCADE)
  room_name = models.CharField(max_length=45)
  last_humidity = models.FloatField(null=True)
  last_temperature = models.FloatField(null=True)
  last_amount_CO2 = models.FloatField(null=True)
  last_reading_time = models.DateTimeField()
  nr_of_appliances = models.IntegerField()
  last_lux = models.FloatFiled()
  night_mode = models.CharField(max_length=1, choices=ENUMCHOICES)


class Room_Reading(models.Model):
  reading_time = models.DateTimeField(unique=True)
  room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
  temperature = models.FloatField(null=True)
  humidity = models.FloatField(null=True)
  amount_of_CO2 = models.FloatField(null=True)
  lux = models.FloatField()


class Room_Water_Meter(models.Model):
  room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
  avg_water_consumed = models.FloatField()
  meter_status = models.CharField(max_length=1, choices=ENUMCHOICES)

class Room_Water_Meter_Readings(TimeStampedModel):
  water_consumed = models.FloatField()
  reading_time = models.DateTimeField()
  hot_water_reading = models.FloatField()
  cold_water_reading = models.FloatField()
  meter_id = models.ForeignKey(Room_Water_Meter, on_delete=models.CASCADE)

class Appliance_Water_Mater(models.Model):
  avg_water_consumed = models.FloatField()
  meter_status = models.CharField(max_length=1, choices=ENUMCHOICES)
  appliance_id = models.ForeignKey(List_Of_All_Possible_Applieances, on_delete=models.CASCADE)
  

class Appliance_Water_Meter_Readings(TimeStampedModel):
  water_consumed = models.FloatField()
  reading_time = models.DateTimeField()
  hot_water_reading = models.FloatField()
  cold_water_reading = models.FloatField()
  meter_id = models.ForeignKey(Appliance_Water_Mater, on_delete=models.CASCADE)

class List_Of_All_Possible_Appliances(models.Model):
  appliance_name = models.CharField(max_length=200)
  maximum_kwh = models.FloatField()
  minimum_kwh = models.FloatField()
  last_brightness = models.IntegerField(null=True)

class Appliance_Brightness(TimeStampedModel):
  appliance_id = models.ForeignKey(List_Of_All_Possible_Applieances, on_delete=models.CASCADE)
  brightness = models.IntegerField()
  start_time = models.DateTimeField()
  end_time = models.DateTimeField()

class Socket_Readings(TimeStampedModel):
  power_consumed = models.FloatField(null=True)
  reading_time = models.DateTimeField()
  socket_id = models.ForeignKey(Sockets, on_delete=models.CASCADE)

class Sockets(models.Model):
  appliance_id = models.ForeignKey(List_Of_All_Possible_Applieances, on_delete=models.CASCADE)
  room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
  socket_status = models.CharField(max_length=1, choices=ENUMCHOICES)
  avg_power_consumed = models.FloatField() 
  socket_name = models.CharField(max_length=45)

class Light(models.Model):
  room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
  color_temperature = models.IntegerField()
  brightness = models.IntegerField()

class Sensor(models.Model):
  sensor_name = models.CharField(max_length=45)
  sensor_function = models.CharField(max_length=200)
  sensor_location = models.CharField(max_length=200)
  reads_for = models.CharField(max_length=45)

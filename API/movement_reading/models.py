from django.db import models

class MovementReading(models.Model):
	sensor_id = models.IntegerField()
	value = models.IntegerField()

from django.db import models

class MovementReading(models.Model):
	sensor_id = models.IntegerField()
	value = models.IntegerField()
	reading_time = models.DateTimeField(auto_now_add=True)

from rest_framework import serializers
from .models import Sensor_Reading

class Sensor_ReadingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sensor_Reading
        fields = "__all__"

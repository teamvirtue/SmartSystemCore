from rest_framework import serializers
from .models import Room_Water_Meter_Readings

class Room_Water_Meter_ReadingsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room_Water_Meter_Readings
        fields = "__all__"

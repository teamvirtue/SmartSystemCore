from rest_framework import serializers
from .models import Appliance_Water_Meter_Readings

class Appliance_Water_Meter_ReadingsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Appliance_Water_Meter_Readings
        fields = "__all__"

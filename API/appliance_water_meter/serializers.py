from rest_framework import serializers
from .models import Appliance_Water_Meter

class Appliance_Water_MeterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Appliance_Water_Meter
        fields = '__all__'

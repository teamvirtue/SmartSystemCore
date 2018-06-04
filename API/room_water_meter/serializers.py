from rest_framework import serializers
from .models import Room_Water_Meter

class Room_Water_MeterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room_Water_Meter
        fields = "__all__"

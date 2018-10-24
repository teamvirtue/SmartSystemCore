from rest_framework import serializers
from .models import Battery

class BatterySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Battery
        fields = '__all__'

from rest_framework import serializers
from .models import Appliance_Brightness

class Appliance_BrightnessSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Appliance_Brightness
        fields = "__all__"

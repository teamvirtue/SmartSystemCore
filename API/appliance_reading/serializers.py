from rest_framework import serializers
from .models import Appliance_Reading

class Appliance_ReadingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Appliance_Reading
        fields = "__all__"

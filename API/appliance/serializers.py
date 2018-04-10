from rest_framework import serializers
from .models import Appliance

class ApplianceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Appliance
        fields = "__all__"

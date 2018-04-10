from rest_framework import serializers
from .models import List_Of_All_Appliance_in_building

class List_Of_All_Appliance_in_buildingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = List_Of_All_Appliance_in_building
        fields = "__all__"

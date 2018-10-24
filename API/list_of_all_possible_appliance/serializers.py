from rest_framework import serializers
from .models import List_Of_All_Possible_Appliances

class List_Of_All_Possible_AppliancesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = List_Of_All_Possible_Appliances
        fields = "__all__"

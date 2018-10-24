from rest_framework import serializers
from .models import Personal_Details

class Personal_DetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Personal_Details
        fields = "__all__"

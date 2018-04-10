from rest_framework import serializers
from .models import Personal_details

class Personal_detailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Personal_details
        fields = '__all__'

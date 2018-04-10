from rest_framework import serializers
from .models import Person_Sleep

class Person_SleepSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person_Sleep
        fields = '__all__'

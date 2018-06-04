from rest_framework import serializers
from .models import Person_Activity

class Person_ActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person_Activity
        fields = "__all__"

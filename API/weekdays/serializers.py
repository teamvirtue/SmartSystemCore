from rest_framework import serializers
from .models import Weekdays

class WeekdaysSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Weekdays
        fields = "__all__"

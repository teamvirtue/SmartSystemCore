from rest_framework import serializers
from .models import MovementReading

class MovementReadingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MovementReading
        fields = "__all__"

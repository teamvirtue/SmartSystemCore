from rest_framework import serializers
from .models import Room_Reading

class Room_ReadingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room_Reading
        fields = "__all__"

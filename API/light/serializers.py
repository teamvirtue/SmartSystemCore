from rest_framework import serializers
from .models import Light

class LightSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Light
        fields = "__all__"

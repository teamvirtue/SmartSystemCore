from rest_framework import serializers
from .models import Unit

class UnitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Unit
        fields = "__all__"

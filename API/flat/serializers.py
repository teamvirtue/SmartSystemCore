from rest_framework import serializers
from .models import Flat

class FlatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Flat
        fields = "__all__"

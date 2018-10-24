from rest_framework import serializers
from .models import Grid

class GridSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Grid
        fields = "__all__"

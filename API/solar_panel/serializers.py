from rest_framework import serializers
from .models import Solar_Panel

class Solar_PanelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Solar_Panel
        fields = '__all__'

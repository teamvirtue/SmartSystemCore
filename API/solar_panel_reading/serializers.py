from rest_framework import serializers
from .models import Solar_Panel_Reading

class Solar_Panel_ReadingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Solar_Panel_Reading
        fields = '__all__'

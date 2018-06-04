from rest_framework import serializers
from .models import Socket_Reading

class Socket_ReadingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Socket_Reading
        fields = "__all__"

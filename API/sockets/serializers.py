from rest_framework import serializers
from .models import Sockets

class SocketsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sockets
        fields = "__all__"

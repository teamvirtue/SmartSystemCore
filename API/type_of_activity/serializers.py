from rest_framework import serializers
from .models import Type_Of_Activity

class Type_Of_ActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Type_Of_Activity
        fields = "__all__"

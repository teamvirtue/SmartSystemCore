from rest_framework import serializers
from .models import Family

class FamilySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Family
        fields = "__all__"

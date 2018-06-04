from django.shortcuts import render, HttpResponse
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import Appliance_Water_Meter_ReadingsSerializer
from .models import Appliance_Water_Meter_Readings
from rest_framework.reverse import reverse
from rest_framework.views import APIView
import json
#views here.
class Appliance_Water_Meter_ReadingsViewSet(viewsets.ModelViewSet):
    queryset = Appliance_Water_Meter_Readings.objects.all()
    serializer_class = Appliance_Water_Meter_ReadingsSerializer

from django.shortcuts import render, HttpResponse
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import Appliance_Water_MeterSerializer
from .models import Appliance_Water_Meter
from rest_framework.reverse import reverse
from rest_framework.views import APIView
import json
#views here.
class Appliance_Water_MeterViewSet(viewsets.ModelViewSet):
    queryset = Appliance_Water_Meter.objects.all()
    serializer_class = Appliance_Water_MeterSerializer

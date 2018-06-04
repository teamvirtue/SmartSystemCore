from django.shortcuts import render, HttpResponse
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import Room_Water_MeterSerializer
from .models import Room_Water_Meter
from rest_framework.reverse import reverse
from rest_framework.views import APIView
import json
#views here.
class Room_Water_MeterViewSet(viewsets.ModelViewSet):
    queryset = Room_Water_Meter.objects.all()
    serializer_class = Room_Water_MeterSerializer

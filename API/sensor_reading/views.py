from django.shortcuts import render, HttpResponse
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import Sensor_ReadingSerializer
from .models import Sensor_Reading
from rest_framework.reverse import reverse
from rest_framework.views import APIView
import json
#views here.
class Sensor_ReadingViewSet(viewsets.ModelViewSet):
    queryset = Sensor_Reading.objects.all()
    serializer_class = Sensor_ReadingSerializer

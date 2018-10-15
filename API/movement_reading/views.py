from django.shortcuts import render, HttpResponse
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import MovementReading
from .serializers import MovementReadingSerializer
from rest_framework.reverse import reverse
from rest_framework.views import APIView
import json
#views here.
class MovementReadingViewSet(viewsets.ModelViewSet):
    queryset = MovementReading.objects.all()
    serializer_class = MovementReadingSerializer


class MovementReadingSensorRealtimeViewSet(viewsets.ModelViewSet):
    serializer_class = MovementReadingSerializer
    def get_queryset(self):
        sensor = self.kwargs['sensor']
        queryset = MovementReading.objects.filter(sensor_id=sensor).order_by('-id')[:1]
        return queryset


class MovementReadingSensorAllViewSet(viewsets.ModelViewSet):
    serializer_class = MovementReadingSerializer
    def get_queryset(self):
        sensor = self.kwargs['sensor']
        queryset = MovementReading.objects.filter(sensor_id=sensor)
        return queryset

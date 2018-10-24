from django.shortcuts import render, HttpResponse
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import Appliance_BrightnessSerializer
from .models import Appliance_Brightness
from rest_framework.reverse import reverse
from rest_framework.views import APIView
import json
#views here.
class Appliance_BrightnessViewSet(viewsets.ModelViewSet):
    queryset = Appliance_Brightness.objects.all()
    serializer_class = Appliance_BrightnessSerializer

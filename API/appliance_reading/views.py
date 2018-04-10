from django.shortcuts import render, HttpResponse
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import Appliance_ReadingSerializer
from .models import Appliance_Reading
from rest_framework.reverse import reverse
from rest_framework.views import APIView
import json
#views here.
class Appliance_ReadingViewSet(viewsets.ModelViewSet):
    queryset = Appliance_Reading.objects.all()
    serializer_class = Appliance_ReadingSerializer

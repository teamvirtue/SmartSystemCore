from django.shortcuts import render, HttpResponse
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import  ApplianceSerializer
from .models import Appliance
from rest_framework.reverse import reverse
from rest_framework.views import APIView
import json
#views here.
class ApplianceViewSet(viewsets.ModelViewSet):
    queryset = Appliance.objects.all()
    serializer_class = ApplianceSerializer

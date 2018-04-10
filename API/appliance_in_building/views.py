from django.shortcuts import render, HttpResponse
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import List_Of_All_Appliance_in_buildingSerializer
from .models import List_Of_All_Appliance_in_building
from rest_framework.reverse import reverse
from rest_framework.views import APIView
import json

class List_Of_All_Appliance_in_buildingViewSet(viewsets.ModelViewSet):
    queryset = List_Of_All_Appliance_in_building.objects.all()
    serializer_class = List_Of_All_Appliance_in_buildingSerializer

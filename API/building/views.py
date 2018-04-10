from django.shortcuts import render, HttpResponse
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import BuildingSerializer
from .models import Building
from rest_framework.reverse import reverse
from rest_framework.views import APIView
import json
#views here.
class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

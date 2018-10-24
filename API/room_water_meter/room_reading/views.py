from django.shortcuts import render, HttpResponse
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import Room_ReadingSerializer
from .models import Room_Reading
from rest_framework.reverse import reverse
from rest_framework.views import APIView
import json
#views here.
class Room_ReadingViewSet(viewsets.ModelViewSet):
    queryset = Room_Reading.objects.all()
    serializer_class = Room_ReadingSerializer

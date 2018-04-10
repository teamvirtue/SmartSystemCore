from django.shortcuts import render, HttpResponse
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import Person_SleepSerializer
from .models import Person_Sleep
from rest_framework.reverse import reverse
from rest_framework.views import APIView
import json
#views here.
class Person_SleepViewSet(viewsets.ModelViewSet):
    queryset = Person_Sleep.objects.all()
    serializer_class = Person_SleepSerializer

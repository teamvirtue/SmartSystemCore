from django.shortcuts import render, HttpResponse
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import Type_Of_ActivitySerializer
from .models import Type_Of_Activity
from rest_framework.reverse import reverse
from rest_framework.views import APIView
import json
#views here.
class Type_Of_ActivityViewSet(viewsets.ModelViewSet):
    queryset = Type_Of_Activity.objects.all()
    serializer_class = Type_Of_ActivitySerializer

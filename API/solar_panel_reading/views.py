from django.shortcuts import render, HttpResponse
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import Solar_Panel_ReadingSerializer
from .models import Solar_Panel_Reading
from rest_framework.reverse import reverse
from rest_framework.views import APIView
import json
#views here.
class Solar_Panel_ReadingViewSet(viewsets.ModelViewSet):
    queryset = Solar_Panel_Reading.objects.all()
    serializer_class = Solar_Panel_ReadingSerializer

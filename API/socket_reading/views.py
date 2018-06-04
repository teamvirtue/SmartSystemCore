from django.shortcuts import render, HttpResponse
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import Socket_ReadingSerializer
from .models import Socket_Reading
from rest_framework.reverse import reverse
from rest_framework.views import APIView
import json
#views here.
class Socket_ReadingViewSet(viewsets.ModelViewSet):
    queryset = Socket_Reading.objects.all()
    serializer_class = Socket_ReadingSerializer

from django.shortcuts import render, HttpResponse
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import SocketsSerializer
from .models import Sockets
from rest_framework.reverse import reverse
from rest_framework.views import APIView
import json
#views here.
class SocketsViewSet(viewsets.ModelViewSet):
    queryset = Sockets.objects.all()
    serializer_class = SocketsSerializer

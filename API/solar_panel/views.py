from django.shortcuts import render, HttpResponse
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import Solar_PanelSerializer
from .models import Solar_Panel
from rest_framework.reverse import reverse
from rest_framework.views import APIView
import json
#views here.
class Solar_PanelViewSet(viewsets.ModelViewSet):
    queryset = Solar_Panel.objects.all()
    serializer_class = Solar_PanelSerializer

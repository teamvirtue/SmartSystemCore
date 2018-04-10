from django.shortcuts import render, HttpResponse
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import Personal_detailsSerializer
from .models import Personal_details
from rest_framework.reverse import reverse
from rest_framework.views import APIView
import json
#views here.
class Personal_detailsViewSet(viewsets.ModelViewSet):
    queryset = Personal_details.objects.all()
    serializer_class = Personal_detailsSerializer

from django.shortcuts import render, HttpResponse
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import Personal_DetailsSerializer
from .models import Personal_Details
from rest_framework.reverse import reverse
from rest_framework.views import APIView
import json
#views here.
class Personal_DetailsViewSet(viewsets.ModelViewSet):
    queryset = Personal_Details.objects.all()
    serializer_class = Personal_DetailsSerializer



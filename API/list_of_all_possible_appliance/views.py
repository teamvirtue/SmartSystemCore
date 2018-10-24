from django.shortcuts import render, HttpResponse
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import List_Of_All_Possible_AppliancesSerializer
from .models import List_Of_All_Possible_Appliances
from rest_framework.reverse import reverse
from rest_framework.views import APIView
import json
#views here.
class List_Of_All_Possible_AppliancesViewSet(viewsets.ModelViewSet):
    queryset = List_Of_All_Possible_Appliances.objects.all()
    serializer_class = List_Of_All_Possible_AppliancesSerializer

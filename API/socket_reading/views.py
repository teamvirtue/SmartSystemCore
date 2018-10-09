from django.shortcuts import render, HttpResponse
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import Socket_ReadingSerializer
from .models import Socket_Reading
from room.models import Room
from sockets.models import Sockets
from sockets.serializers import SocketsSerializer
from room.serializers import RoomSerializer
from rest_framework.reverse import reverse
from rest_framework.views import APIView
import json


# views here.


class Socket_ReadingViewSet(viewsets.ModelViewSet):
    queryset = Socket_Reading.objects.all()
    serializer_class = Socket_ReadingSerializer


class Socket_ReadingRoomIdRealtimeViewSet(viewsets.ModelViewSet):

    serializer_class = Socket_ReadingSerializer
    def get_queryset(self):
        identifier = self.kwargs['identifier']
        queryset = Socket_Reading.objects.filter(socket_id=identifier).order_by('-id')[:1]
        return queryset

class Socket_ReadingRoomRoomnameRealtimeViewSet(viewsets.ModelViewSet):
    serializer_class = Socket_ReadingSerializer
    def get_queryset(self):
        identifier = self.kwargs['identifier']
        room = Room.objects.filter(room_name=identifier).first()
        sockets = Sockets.objects.filter(room_id=room.id)
        queryset = Socket_Reading.objects.filter(socket_id__in=sockets.values("id")).order_by('-id')[:1]
        return queryset

class Socket_ReadingRoomIdAllViewSet(viewsets.ModelViewSet):
    serializer_class = Socket_ReadingSerializer
    def get_queryset(self):
        identifier = self.kwargs['identifier']
        queryset = Socket_Reading.objects.filter(socket_id=identifier)
        return queryset

class Socket_ReadingRoomRoomnameAllViewSet(viewsets.ModelViewSet):
    serializer_class = Socket_ReadingSerializer
    def get_queryset(self):
        identifier = self.kwargs['identifier']
        room = Room.objects.filter(room_name=identifier).first()
        sockets = Sockets.objects.filter(room_id=room.id)
        queryset = Socket_Reading.objects.filter(socket_id__in=sockets.values("id"))
        return queryset


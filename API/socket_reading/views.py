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




class Socket_ReadingAllRoomsRealtimeViewSet(viewsets.ModelViewSet):
    queryset = Socket_Reading.objects.raw('select distinct on(socket_id_id) * from socket_reading_socket_reading order by socket_id_id,reading_time desc;');
    serializer_class = Socket_ReadingSerializer

class Socket_ReadingAllRoomsAllViewSet(viewsets.ModelViewSet):
    queryset = Socket_Reading.objects.all()
    serializer_class = Socket_ReadingSerializer

#roomname realtime
class Socket_ReadingRoomRoomnameRealtimeViewSet(viewsets.ModelViewSet):
    serializer_class = Socket_ReadingSerializer

    def get_queryset(self):
        identifier = self.kwargs['identifier']
        room = Room.objects.filter(room_name=identifier).first()
        sockets = Sockets.objects.filter(room_id=room.id)
        queryset = Socket_Reading.objects.filter(socket_id__in=sockets.values("id")).order_by('-socket_id','-created').distinct("socket_id")
        return queryset


#roomname all

class Socket_ReadingRoomRoomnameAllViewSet(viewsets.ModelViewSet):
    serializer_class = Socket_ReadingSerializer

    def get_queryset(self):
        identifier = self.kwargs['identifier']
        room = Room.objects.filter(room_name=identifier).first()
        sockets = Sockets.objects.filter(room_id=room.id)
        queryset = Socket_Reading.objects.filter(socket_id__in=sockets.values("id"))
        return queryset

#id realtime
class Socket_ReadingRoomIdRealtimeViewSet(viewsets.ModelViewSet):
    serializer_class = Socket_ReadingSerializer

    def get_queryset(self):
        identifier = self.kwargs['identifier']
        queryset = Socket_Reading.objects.filter(socket_id=identifier).order_by('-id')[:1]
        return queryset

#id all
class Socket_ReadingRoomIdAllViewSet(viewsets.ModelViewSet):
    serializer_class = Socket_ReadingSerializer

    def get_queryset(self):
        identifier = self.kwargs['identifier']
        queryset = Socket_Reading.objects.filter(socket_id=identifier)
        return queryset


class Socket_ReadingCleanOldViewSet(viewsets.ModelViewSet):
    queryset = Socket_Reading.objects.all()
    serializer_class = Socket_ReadingSerializer

    def destroy(self, request, *args):
        pass
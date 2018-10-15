"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.urls import path
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from . import views


router = routers.DefaultRouter()
router.register('socket_readings', views.Socket_ReadingViewSet)
router.register(r'(?P<identifier>[0-9]*)/realtime',views.Socket_ReadingRoomIdRealtimeViewSet,base_name="realtime")
router.register(r'(?P<identifier>[0-9]*)/realtime',views.Socket_ReadingRoomRoomnameRealtimeViewSet,base_name="realtime")

router.register(r'(?P<identifier>[0-9]*)/all',views.Socket_ReadingRoomIdAllViewSet,base_name="all")
router.register(r'(?P<identifier>[0-9]*)/all',views.Socket_ReadingRoomRoomnameAllViewSet,base_name="all")


router.register('cleanOld',views.Socket_ReadingCleanOldViewSet,base_name="clean")

router.register('Allrooms/realtime',views.Socket_ReadingAllRoomsRealtimeViewSet,base_name="clean")
router.register('Allrooms/all',views.Socket_ReadingAllRoomsAllViewSet,base_name="clean")

urlpatterns = [
    path('', include(router.urls)),
]

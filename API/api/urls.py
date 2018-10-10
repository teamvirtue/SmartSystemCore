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
from django.contrib import admin
from django.conf.urls import  url, include
from django.contrib.auth.models import User
from django.urls import path, re_path
from rest_framework import routers, serializers, viewsets
from building.views import BuildingViewSet
from flat.views import FlatViewSet
from movement_reading.views import MovementReadingViewSet
from room.views import RoomViewSet
from sensor.views import SensorViewSet
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.authtoken import views as drf_views
from grid.views import GridViewSet
from appliance_brightness.views import Appliance_BrightnessViewSet
from appliance_water_meter.views import Appliance_Water_MeterViewSet
from battery.views import BatteryViewSet
from family.views import FamilyViewSet
from light.views import LightViewSet
from list_of_all_possible_appliance.views import List_Of_All_Possible_AppliancesViewSet
from person_activity.views import Person_ActivityViewSet
from personal_detail.views import Personal_DetailsViewSet
from room_water_meter_reading.views import Room_Water_Meter_ReadingsViewSet
from socket_reading.views import Socket_ReadingViewSet
from solar_panel.views import Solar_PanelViewSet
from solar_panel_reading.views import Solar_Panel_ReadingViewSet
from type_of_activity.views import Type_Of_ActivityViewSet
from weekdays.views import WeekdaysViewSet
from sockets.views import SocketsViewSet



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
# Routers provide an easy way of automatically determining the URL conf.


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'flat', FlatViewSet)
router.register(r'building', BuildingViewSet)
router.register(r'room', RoomViewSet)
router.register(r'sensor', SensorViewSet)
router.register(r'grid', GridViewSet)
router.register(r'appliace_brightness', Appliance_BrightnessViewSet)
router.register(r'appliance_water_meter', Appliance_Water_MeterViewSet)
router.register(r'battery', BatteryViewSet)
router.register(r'family', FamilyViewSet)
router.register(r'light', LightViewSet)
router.register(r'list_of_all_possible_appliance', List_Of_All_Possible_AppliancesViewSet)
router.register(r'person_activity',Person_ActivityViewSet )
router.register(r'personal_details', Personal_DetailsViewSet)
router.register(r'room_water_meter_reading',Room_Water_Meter_ReadingsViewSet )
router.register(r'socket_reading',Socket_ReadingViewSet )
router.register(r'solar_panel', Solar_PanelViewSet)
router.register(r'solar_panel_reading',Solar_Panel_ReadingViewSet )
router.register(r'type_of_activity', Type_Of_ActivityViewSet)
router.register(r'weekdays', WeekdaysViewSet)
router.register(r'sockets', SocketsViewSet)
router.register(r'movement_reading', MovementReadingViewSet)


#router.register(r'accounts', AccountViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/auth/token/', obtain_jwt_token),
    # path('appliance/',include('appliance.urls')),
    # path('appliance_in_building/',include('appliance.urls')),
    # path('appliance_reading/',include('appliance_reading.urls')),
    # path('building/',include('building.urls')),
    # path('flat/',include('flat.urls')),
    # path('person_sleep/',include('person_sleep.urls')),
    # path('personal_details/',include('personal_details.urls')),
    # path('room/',include('room.urls')),
    # path('room_reading/',include('room_reading.urls')),
    # path('sensor/',include('sensor.urls')),
    # path('sensor_reading/',include('sensor_reading.urls')),
    # path('unit/',include('unit.urls')),
    # path('weather/',include('weather.urls')),
	path('socket_reading/',include('socket_reading.urls')),
    path('', include(router.urls)),

 ]

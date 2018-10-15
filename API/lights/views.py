from django.http import HttpResponse
from rest_framework import generics, viewsets
import subprocess


class LightsViewSet(viewsets.ViewSet):
    def execute(self, *args, **kwargs):
        group = kwargs['group']
        mode = kwargs['mode']
        subprocess.call('sudo python2 ~/dali/dali.py -group {} -{}'.format(group, mode), shell=True)
        return HttpResponse("Executed Dali function")

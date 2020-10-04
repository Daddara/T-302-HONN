import json
from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse
from .gateway.service import Service


# Create your views here.

def forecast(_request):
    service = Service('Reykjavik')
    #gateway = WeatherApiWeatherGateway(service1)
    data, err = service.service_get_weather_forecast()

    # In order to allow non-dict objects to be serialized set the safe parameter to False.
    return HttpResponse(data.to_j(), content_type='application/json')


def current(_request):
    service = Service('Reykjavik')

    #gateway = WeatherApiWeatherGateway(service1)

    # We are currently hard coding Reykjavik. We would need to add a location service
    # or something else to request the location and that would just make
    # this class more complicated and the gateway less clear
    data, err = service.service_get_weather_current()

    return JsonResponse(data.__dict__, safe=False)

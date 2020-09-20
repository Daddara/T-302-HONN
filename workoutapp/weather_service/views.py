import json
from django.core import serializers
from django.http import HttpResponse

from django.http import JsonResponse

from .gateway.weather_gateway import WeatherGateway
from .gateway.weather_gateway import WeatherApiWeatherGateway


# Create your views here.
def forecast(_request):
    gateway = WeatherApiWeatherGateway()
    # In order to allow non-dict objects to be serialized set the safe parameter to False.
    data, err = gateway.get_weather_forecast('Reykjavik')

    return HttpResponse(data.to_j(), content_type='application/json')


def current(_request):
    gateway = WeatherApiWeatherGateway()

    data, err = gateway.get_weather_current('Reykjavik')

    return JsonResponse(data.__dict__, safe=False)

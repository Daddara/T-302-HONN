import json
from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse
from .__init__ import WEATHER_GATEWAY_STUB, WEATHER_API_WEATHER_GATEWAY
# Create your views here.


def forecast(_request):
    data, err = WEATHER_API_WEATHER_GATEWAY.get_weather_forecast('Reykjavik')
    # In order to allow non-dict objects to be serialized set the safe parameter to False.
    if data is None:
        return JsonResponse({}, status=400)
    return HttpResponse(data.to_j(), content_type='application/json')


def current(_request):
    # We are currently hard coding Reykjavik. We would need to add a location service
    # or something else to request the location and that would just make
    # this class more complicated and the gateway less clear
    data, err = WEATHER_API_WEATHER_GATEWAY.get_weather_current('Reykjavik')
    if data is None:
        return JsonResponse({}, status=400)
    return JsonResponse(data.__dict__, safe=False)




from django.urls import path

from . import views

urlpatterns = [
    path('forecast', views.forecast, name='weather_api_v1')
]
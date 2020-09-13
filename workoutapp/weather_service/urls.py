from django.urls import path

from . import views

urlpatterns = [
    path('forcast/', views.results, name='weather_api_v1')
]
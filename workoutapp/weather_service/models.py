from django.db import models
import datetime


class WeatherData(models.Model):
    Lat = models.FloatField()
    Lon = models.FloatField()
    CreatedAt = models.DateTimeField(auto_now_add=True)
    ValidUntil = models.DateTimeField()
    Data = models.CharField()
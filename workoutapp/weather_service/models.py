from django.db import models


class WeatherData(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    valid_until = models.DateTimeField()

    data_date = models.DateTimeField()
    temp_c = models.FloatField()
    wind_kph = models.FloatField()
    precipitation_mm = models.FloatField()
    cloud = models.IntegerField()
    visibility_km = models.FloatField()

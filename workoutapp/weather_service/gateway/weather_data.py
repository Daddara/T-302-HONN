import json
from json import JSONEncoder
from typing import Any


class CommonWeatherData:
    def __init__(
            self,
            date_time: int,
            lat: float,
            lon: float,
            name: str):
        self.date_time = date_time
        self.lat = lat
        self.lon = lon
        self.name = name


class CurrentWeatherData(CommonWeatherData):
    def __init__(
            self,
            date_time: int,
            lat: float,
            lon: float,
            name: str,
            temp_c: float,
            wind_kph: float,
            precipitation_mm: float,
            cloud: int,
            visibility_km: float):

        CommonWeatherData.__init__(self, date_time, lat, lon, name)

        self.temp_c = temp_c
        self.wind_kph = wind_kph
        self.precipitation_mm = precipitation_mm
        self.cloud = cloud
        self.visibility_km = visibility_km


class ForecastWeatherData(CommonWeatherData):
    def __init__(
            self,
            date_time,
            lat: float,
            lon: float,
            name: str,
            days: []):

        CommonWeatherData.__init__(self, date_time, lat, lon, name)

        self.days = days


class ForecastDayWeatherData:
    def __init__(
            self,
            date_time: int,
            min_temp_c: float,
            max_temp_c: float,
            avg_temp_c: float,
            max_wind_kmh: float,
            precipitation_mm: float,
            avg_visibility_km: float,
            chance_rain: float,
            chance_snow: float):

        super().__init__()
        self.date_time = date_time
        self.min_temp_c = min_temp_c
        self.max_temp_c = max_temp_c
        self.avg_temp_c = avg_temp_c
        self.max_wind_kmh = max_wind_kmh
        self.precipitation_mm = precipitation_mm
        self.avg_visibility_km = avg_visibility_km
        self.chance_rain = chance_rain
        self.chance_snow = chance_snow
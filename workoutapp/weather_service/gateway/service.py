from .weather_gateway import WeatherGateway
from .weather_gateway import WeatherApiWeatherGateway


class Service:
    def __init__(self, location):
        self.gateway = WeatherApiWeatherGateway()
        self.location = location

    def service_get_weather_forecast(self):
        return self.gateway.get_weather_forecast(self.location)

    def service_get_weather_current(self):
        return self.gateway.get_weather_current(self.location)


from .gateway.weather_gateway import WeatherApiWeatherGateway, WeatherGatewayStub, WeatherService

WEATHER_SERVICE = WeatherService(WeatherGatewayStub())

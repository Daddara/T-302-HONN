import datetime
import random
import urllib.request, urllib.error
import json
import time

from .weather_data import CurrentWeatherData
from .weather_data import ForecastWeatherData
from .weather_data import ForecastDayWeatherData
# from .weather_data import WeatherWarnings


class WeatherGatewayError:
    """An error class for all possible errors that might occur in the gateway"""

    STRING_FORMAT = '[{}] {}: {}'

    ERR_TYPE_HTTP = 'HTTP'
    ERR_TYPE_PARSING = 'PARSING'

    def __init__(
            self,
            err_type: str,
            err_sub_id: int = 0,
            err_text: str = "<NO TEXT>"):
        """Initializes the error object"""
        self.err_type = err_type
        self.err_sub_id = err_sub_id
        self.err_text = err_text

    def get_error_str(self):
        """Creates a string with the error information"""
        return WeatherGatewayError.STRING_FORMAT.format(
            self.err_type,
            self.err_sub_id,
            self.err_text
        )

    def print_err(self):
        """Prints the error string to the console"""
        print(self.get_error_str())


class WeatherGateway:
    """This is the base interface to access weather data"""

    def get_weather_current(self, city: str) -> (CurrentWeatherData, WeatherGatewayError):
        """Get the current weather data

        Parameters
        ----------
        city : str
            The city the weather should be loaded for.

        Returns the current weather data as a CurrentWeatherData
        -------
        """
        pass

    def get_weather_forecast(self, city: str, days: int = 3) -> (ForecastWeatherData, WeatherGatewayError):
        """Get the weather forecast for x days

        Parameters
        ----------
        city : str
            The city the weather should be loaded for.
        days : int
            The amount of days to load for the forecast. (default: 3)

        Returns the forecast weather data as a ForecastWeatherData
        -------
        """
        pass

#    def get_weather_warnings(self, city: str) -> WeatherWarnings:
#        """Get the weather warnings for the input city
#
#        Parameters
#        ----------
#        city : str
#            The city the weather should be loaded for.
#
#        Returns the weather warnings as a WeatherWarnings
#        -------
#        """
#        pass


class WeatherApiWeatherGateway(WeatherGateway):

    CURRENT_URL = 'https://api.weatherapi.com/v1/current.json?key={}&q={}'
    FORECAST_URL = 'https://api.weatherapi.com/v1/forecast.json?key={}&q={}&days={}'
    ALERT_URL = 'https://api.weatherapi.com/v1/forecast.json?key={}&q={}&days=1'

    def __init__(self):
        WeatherGateway.__init__(self)
        self.api_key = 'b0cf0f6686224ec6a9f164627201209'

        # TODO xFrednet 2020.09.12: Load the API key from somewhere else this isn't the nicest way

    def get_weather_current(self, city: str) -> (CurrentWeatherData, WeatherGatewayError):
        url = WeatherApiWeatherGateway.CURRENT_URL.format(
            self.api_key,
            city
        )

        data, error = WeatherApiWeatherGateway._send_request(url)
        if error is not None:
            return data, error

        return WeatherApiWeatherGateway._parse_current_weather_data(data)

    @staticmethod
    def _parse_current_weather_data(data) -> (CurrentWeatherData, WeatherGatewayError):
        try:
            response = json.loads(data)

            location_data = response["location"]
            current_data = response["current"]

            return CurrentWeatherData(
                date_time=int(current_data["last_updated_epoch"]),
                lat=float(location_data["lat"]),
                lon=float(location_data["lon"]),
                name=location_data["name"],
                temp_c=float(current_data["temp_c"]),
                wind_kph=float(current_data["wind_kph"]),
                precipitation_mm=float(current_data["precip_mm"]),
                cloud=int(current_data["cloud"]),
                visibility_km=float(current_data["vis_km"]),
            ), None

        except:
            return None, WeatherGatewayError(
                WeatherGatewayError.ERR_TYPE_PARSING,
                0,
                "IDK, bad documentation an such, you should never see this (Hello @Test)"
            )

    def get_weather_forecast(self, city: str, days: int = 3) -> (ForecastWeatherData, WeatherGatewayError):
        # An interesting thing. The forecast of WeatherAPI is broken. Even when I try
        # it on https://www.weatherapi.com/api-explorer.aspx. It will always only return
        # three days. Super funny and interesting if you ask me but it causes some tests to fail #58
        # -.- ~xFrednet 2020.09.17
        days = 3

        url = WeatherApiWeatherGateway.FORECAST_URL.format(
            self.api_key,
            city,
            days
        )

        data, error = WeatherApiWeatherGateway._send_request(url)
        if error is not None:
            return data, error

        return WeatherApiWeatherGateway._parse_forecast_weather_data(data)

    @staticmethod
    def _parse_forecast_weather_data(data):
        try:
            response = json.loads(data)

            location_data = response["location"]
            json_days = response["forecast"]["forecastday"]
            forecast_days = []

            for json_day in json_days:
                json_day_sub = json_day['day']
                forecast_days.append(
                    ForecastDayWeatherData(
                        date_time=int(json_day['date_epoch']),
                        min_temp_c=float(json_day_sub['mintemp_c']),
                        max_temp_c=float(json_day_sub['maxtemp_c']),
                        avg_temp_c=float(json_day_sub['avgtemp_c']),
                        max_wind_kmh=float(json_day_sub['maxwind_kph']),
                        precipitation_mm=float(json_day_sub['totalprecip_mm']),
                        avg_visibility_km=float(json_day_sub['avgvis_km']),
                        chance_rain=float(json_day_sub['daily_chance_of_rain']) / 100.0,
                        chance_snow=float(json_day_sub['daily_chance_of_snow']) / 100.0
                    ))

            return ForecastWeatherData(
                date_time=int(time.time()),
                lat=float(location_data["lat"]),
                lon=float(location_data["lon"]),
                name=location_data["name"],
                days=forecast_days
            ), None

        except:
            return None, WeatherGatewayError(
                WeatherGatewayError.ERR_TYPE_PARSING,
                0,
                "IDK, bad documentation an such, you should never see this (Hello @Test)"
            )

    @staticmethod
    def _send_request(url) -> (str, WeatherGatewayError):
        try:
            data = urllib.request.urlopen(url).read()
            return data, None
        except urllib.error.HTTPError as e:
            error_text = None

            if e.code == 401:
                # Unauthorized: happens when the API key is outdated.
                error_text = 'The API key is invalid'
            if e.code == 400:
                # Bad Request: Happens when the city is invalid.
                error_text = 'The city name is invalid'

            return None, WeatherGatewayError(
                WeatherGatewayError.ERR_TYPE_HTTP,
                e.code,
                error_text
            )
        # TODO xFrednet 2020.09.12: More error handling


class WeatherGatewayStub(WeatherGateway):
    def __init__(self):
        super().__init__()

    def get_weather_current(self, city: str) -> (CurrentWeatherData, WeatherGatewayError):
        """Service view for current weather. Returns hardcoded"""
        dummy_data = self.generate_current_weather(city=city)
        return dummy_data, None

    def get_weather_forecast(self, city: str, days: int = 3) -> (ForecastWeatherData, WeatherGatewayError):
        """Service view for weather forecast. Returns randomized data or an random error"""
        dummy_data = self.generate_days_forecast(city=city, days=days)
        return dummy_data, None

    @staticmethod
    def generate_current_weather(city: str) -> CurrentWeatherData:
        """Randomly created dummy data, represents numbers in realistic range"""
        return CurrentWeatherData(
            date_time=int(datetime.datetime.now().timestamp()),
            lat=45.00,
            lon=45.00,
            name=city,
            temp_c=10.00,
            wind_kph=22.00,
            precipitation_mm=40.00,
            cloud=25,
            visibility_km=24.00,
        )

    @staticmethod
    def generate_days_forecast(city: str, days: int) -> ForecastWeatherData:
        forecast_days = []
        for i in range(days):
            if i == 0:
                forecast_day = datetime.datetime.now()
            else:
                forecast_day = datetime.datetime.now() + datetime.timedelta(days=i)
            forecast_days.append(
                ForecastDayWeatherData(
                    date_time=int(forecast_day.timestamp()),
                    min_temp_c=-15.00,
                    max_temp_c=15.00,
                    avg_temp_c=7.50,
                    precipitation_mm=40.00,
                    max_wind_kmh=28.00,
                    avg_visibility_km=45.00,
                    chance_rain=26.00,
                    chance_snow=0.22,
                )
            )

        return ForecastWeatherData(date_time=int(time.time()),
                                   lat=-45,
                                   lon=45,
                                   name=city,
                                   days=forecast_days)

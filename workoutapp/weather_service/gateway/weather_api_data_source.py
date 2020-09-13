import urllib.request, urllib.error
import json
import datetime

from .weather_data import CurrentWeatherData


class WeatherApiDataSource:

    BASE_URL = 'https://api.weatherapi.com/v1/forecast.json?key={}&q={}&days=3'

    def __init__(self):
        # TODO xFrednet 2020.09.12: Load the API key from somewhere else this isn't the nicest way
        self.api_key = 'b0cf0f6686224ec6a9f164627201209'

    def load_data(self, lat, lon):
        url = WeatherApiDataSource.BASE_URL.format(
            self.api_key,
            '{},{}'.format(lat, lon)
        )

        data = None
        error = None

        try:
            data = urllib.request.urlopen(url).read()
        except urllib.error.HTTPError as e:
            if e.code == 401:
                # Unauthorized: happens when the API key is outdated.
                error = '401 The API key is invalid'
            if e.code == 400:
                # Bad Request: Happens when the city is invalid.
                error = '400 The city name is invalid'
        # TODO xFrednet 2020.09.12: More error handling

        mapped_data = self._try_map_to_weather_data(data)
        return mapped_data, (mapped_data is not None), error

    @staticmethod
    def _try_map_to_weather_data(response_json):
        if response_json is None:
            return None

        try:
            response = json.loads(response_json)

            location_data = response["location"]
            current_data = response["current"]

            return CurrentWeatherData(
                date_time=datetime.datetime.fromtimestamp(int(current_data["last_updated_epoch"])),
                lat=float(location_data["lat"]),
                lon=float(location_data["lon"]),
                temp_c=float(current_data["temp_c"]),
                wind_kph=float(current_data["wind_kph"]),
                precipitation_mm=float(current_data["precip_mm"]),
                cloud=int(current_data["cloud"]),
                visibility_km=float(current_data["vis_km"]),
            )
        except:
            return None

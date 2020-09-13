import datetime

from .weather_data import CurrentWeatherData


class TestDataSource:

    def __init__(self, data_queue):
        self.data_queue = data_queue

    def load_data(self, lat, lon):
        return self.data_queue.pop(), True, None

    @staticmethod
    def create_test_data(lat, lon):
        return CurrentWeatherData(
            datetime.datetime.now(),
            lat=lat,
            lon=lon,
            temp_c=10.0,
            wind_kph=5.0,
            precipitation_mm=3.0,
            cloud=50,
            visibility_km=12.5
        )
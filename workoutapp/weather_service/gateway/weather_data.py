
class CommonWeatherData:
    def __init__(
            self,
            date_time,
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
            date_time,
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


class ForecastWeatherData:
    def __init__(self):
        pass


class WeatherWarnings:
    pass

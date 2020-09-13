
class CurrentWeatherData:
    def __init__(
            self,
            date_time,
            lat: float,
            lon: float,
            temp_c: float,
            wind_kph: float,
            precipitation_mm: float,
            cloud: int,
            visibility_km: float):
        self.date_time = date_time
        self.lat = lat
        self.lon = lon
        self.temp_c = temp_c
        self.wind_kph = wind_kph
        self.precipitation_mm = precipitation_mm
        self.cloud = cloud
        self.visibility_km = visibility_km



class CacheDataSource:

    def __init__(self):
        self.cache = []

    def new_weather_data_callback(self, data):
        self.cache.append(data)

    def load_data(self, lat, lon):
        if len(self.cache):
            return self.cache.pop(), False, None
        else:
            return None, False, None

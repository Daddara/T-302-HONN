import urllib.request, urllib.error

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

        return data, (data is not None), error
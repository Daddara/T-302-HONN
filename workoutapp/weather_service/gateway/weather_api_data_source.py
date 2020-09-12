import urllib.request

class WeatherApiDataSource:

    BASE_URL = 'https://api.weatherapi.com/v1/forecast.json?key={}&q={}&days=3'

    def __init__(self):
        # TODO xFrednet 2020.09.12: Load the API key from somewhere else this isn't the nicest way
        self.api_key = 'b0cf0f6686224ec6a9f164627201209'

    def load_data(self, city):

        url = WeatherApiDataSource.BASE_URL.format(
            self.api_key,
            city
        )

        request = urllib.request.urlopen(url)

        # TODO xFrednet 2020.09.12: Error handling
        data = request.read()

        return data, True

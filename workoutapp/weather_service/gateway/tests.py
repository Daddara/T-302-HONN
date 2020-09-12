import unittest

from .weather_api_data_source import WeatherApiDataSource

class TestDataSources(unittest.TestCase):
    def test_weather_api_data_source(self):
        data_source = WeatherApiDataSource()

        data, is_new, error = data_source.load_data(city='Reykjavik')

        self.assertTrue(is_new)
        self.assertIsNotNone(data)
        self.assertIsNone(error)

    def test_weather_api_invalid_key(self):
        data_source = WeatherApiDataSource()
        data_source.api_key = 'hello_api'

        data, is_new, error = data_source.load_data(city='Reykjavik')

        self.assertFalse(is_new)
        self.assertIsNone(data)
        self.assertIsNotNone(error)

    def test_weather_api_invalid_city(self):
        data_source = WeatherApiDataSource()

        # You don't like this name? What are you gonna do about it *music*
        # ... I should really, really stop listening to music during development
        # and stop listening the voices in my head that say that this is funny...
        # Anyways how is your day MR reviewer? ~xFrednet
        data, is_new, error = data_source.load_data(city='MyLittleTestTown')

        self.assertFalse(is_new)
        self.assertIsNone(data)
        self.assertIsNotNone(error)

if __name__ == '__main__':
    unittest.main()
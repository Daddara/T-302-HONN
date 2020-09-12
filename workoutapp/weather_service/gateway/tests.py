import unittest

from .weather_api_data_source import WeatherApiDataSource

class TestDataSources(unittest.TestCase):
    def test_weather_api_data_source(self):
        data_source = WeatherApiDataSource()

        data, is_new = data_source.load_data(city='Reykjavik')

        self.assertTrue(is_new)
        self.assertIsNotNone(data)

if __name__ == '__main__':
    unittest.main()
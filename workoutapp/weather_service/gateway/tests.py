import unittest
import datetime

from .weather_api_data_source import WeatherApiDataSource
from .weather_data import CurrentWeatherData
from .weather_gateway import WeatherGateway
from .cache_data_source import CacheDataSource
from .test_data_source import TestDataSource

class TestWeatherApiDataSource(unittest.TestCase):
    def test_weather_api_data_source(self):
        return
        data_source = WeatherApiDataSource()

        data, is_new, error = data_source.load_data(64.15, -21.95)

        self.assertTrue(is_new)
        self.assertIsNotNone(data)
        self.assertIsNone(error)

    def test_weather_api_invalid_key(self):
        return
        data_source = WeatherApiDataSource()
        data_source.api_key = 'hello_api'

        data, is_new, error = data_source.load_data(64.15, -21.95)

        self.assertFalse(is_new)
        self.assertIsNone(data)
        self.assertIsNotNone(error)

    def test_weather_api_invalid_city(self):
        return
        data_source = WeatherApiDataSource()

        # You don't like this name? What are you gonna do about it *music*
        # ... I should really, really stop listening to music during development
        # and stop listening the voices in my head that say that this is funny...
        # Anyways how is your day MR reviewer? ~xFrednet
        data, is_new, error = data_source.load_data(64.15, -21.95)

        self.assertFalse(is_new)
        self.assertIsNone(data)
        self.assertIsNotNone(error)

    def test_map_data(self):
        test_data = '''{
            "location": {
                "lat": 64.15,
                "lon": -21.95
            },
            "current": {
                "last_updated_epoch": 1599929110,
                "last_updated": "2020-09-12 16:45",
                "temp_c": 12.0,
                "wind_kph": 16.9,
                "precip_mm": 0.2,
                "humidity": 50,
                "cloud": 75,
                "vis_km": 10.0
            }
        }'''

        result: CurrentWeatherData = WeatherApiDataSource._try_map_to_weather_data(test_data)

        self.assertEqual(result.date_time, datetime.datetime.fromtimestamp(int(1599929110)))
        self.assertEqual(result.lat, 64.15)
        self.assertEqual(result.lon, -21.95)
        self.assertEqual(result.temp_c, 12.0)
        self.assertEqual(result.wind_kph, 16.9)
        self.assertEqual(result.precipitation_mm, 0.2)
        self.assertEqual(result.cloud, 75)
        self.assertEqual(result.visibility_km, 10.0)

        # Invalid syntax
        self.assertIsNone(WeatherApiDataSource._try_map_to_weather_data('{dwa,dwa}'))

        # Invalid syntax
        self.assertIsNone(WeatherApiDataSource._try_map_to_weather_data('''{
            "xfrednet": "awesome",
            "test": "boring",
            "stupid_test_data": "essential"
        }'''))


class TestCacheDataSource(unittest.TestCase):
    def test_caches_data(self):
        cache_src = CacheDataSource()
        test_src = TestDataSource(
                [
                    TestDataSource.create_test_data(0, 0),
                    TestDataSource.create_test_data(1, 1)
                ]
            )

        gateway = WeatherGateway([cache_src, test_src])
        gateway.register_new_data_listener(cache_src)

        data1 = gateway.get_data(0, 0)
        data2 = gateway.get_data(1, 1)

        self.assertIsNotNone(data1)
        self.assertEqual(data1, data2)

        self.assertTrue(len(test_src.data_queue) == 1)


if __name__ == '__main__':
    unittest.main()
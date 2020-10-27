import unittest
import datetime

from .weather_gateway import WeatherApiWeatherGateway, WeatherGatewayStub
from .weather_gateway import WeatherGatewayError


class TestWeatherApiDataSource(unittest.TestCase):
    def test_get_current_weather(self):
        data_source = WeatherApiWeatherGateway()
        data, error = data_source.get_weather_current('Reykjavik')
        self.assertIsNotNone(data)
        self.assertIsNone(error)
        self.assertEqual(data.name, 'Reykjavik')
        # I can't test the rest because well look out the window the
        # weather in Reykjavik is constantly changing ^^
        # Well we could test for rain to get a 50% success rate xD ~xFrednet 2020.09.16

    def test_get_current_weather_invalid_key(self):
        data_source = WeatherApiWeatherGateway()
        data_source.api_key = 'invalid_key'

        data, error = data_source.get_weather_current('Reykjavik')

        self.assertIsNone(data)
        self.assertIsNotNone(error)
        self.assertEqual(error.err_type, WeatherGatewayError.ERR_TYPE_HTTP)
        self.assertEqual(error.err_sub_id, 401)
        self.assertNotEqual(error.err_text, '<NO TEXT>')

    def test_get_current_weather_invalid_city(self):
        data_source = WeatherApiWeatherGateway()

        # You don't like this name? What are you gonna do about it *music*
        # ... I should really, really stop listening to music during development
        # and stop listening the voices in my head that say that this is funny...
        # Anyways how is your day MR reviewer? ~xFrednet
        # I have no and I mean NO idea what I was thinking when I wrote the first question...
        # But I'll leave it in for fun ~xFrednet 2020.09.16
        data, error = data_source.get_weather_current('some_invalid_city')

        self.assertIsNone(data)
        self.assertIsNotNone(error)
        self.assertEqual(error.err_type, WeatherGatewayError.ERR_TYPE_HTTP)
        self.assertEqual(error.err_sub_id, 400)
        self.assertNotEqual(error.err_text, '<NO TEXT>')

    def test_current_weather_parsing(self):
        test_data = '''{
                    "location": {
                        "name": "Reykjavik",
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

        data, error = WeatherApiWeatherGateway._parse_current_weather_data(test_data)

        self.assertEqual(data.date_time, int(1599929110))
        self.assertEqual(data.lat, 64.15)
        self.assertEqual(data.lon, -21.95)
        self.assertEqual(data.name, 'Reykjavik')
        self.assertEqual(data.temp_c, 12.0)
        self.assertEqual(data.wind_kph, 16.9)
        self.assertEqual(data.precipitation_mm, 0.2)
        self.assertEqual(data.cloud, 75)
        self.assertEqual(data.visibility_km, 10.0)

        # Invalid syntax
        data, error = WeatherApiWeatherGateway._parse_current_weather_data('{life is like a roller coaster')
        self.assertIsNone(data)
        self.assertIsNotNone(error)
        self.assertEqual(error.err_type, WeatherGatewayError.ERR_TYPE_PARSING)
        self.assertEqual(error.err_sub_id, 0)

        # Missing members aka. no members (Who killed them???)
        # I should stop working for now... nawww ~xFrednet 2020.09.16
        data, error = WeatherApiWeatherGateway._parse_current_weather_data('''{
                    "location": "ru",
                    "test": "boring",
                    "stupid_test_data": "essential"
                }''')
        self.assertIsNone(data)
        self.assertIsNotNone(error)
        self.assertEqual(error.err_type, WeatherGatewayError.ERR_TYPE_PARSING)
        self.assertEqual(error.err_sub_id, 0)

    def test_get_forecast_data(self):
        data_source = WeatherApiWeatherGateway()
        data, error = data_source.get_weather_forecast('Reykjavik', days=4)
        self.assertIsNotNone(data)
        self.assertIsNone(error)
        self.assertEqual(data.name, 'Reykjavik')
        # Funny story explained in the API class. The api is broken and will always return
        # three days ^^. Tracked by #58 ~xFrednet
        # self.assertEqual(len(data.days), 4)


class TestWeatherApiWeatherGatewayStub(unittest.TestCase):
    def setUp(self) -> None:
        self.weather_gateway = WeatherGatewayStub()

    def test_get_current_weather(self):
        data, error = self.weather_gateway.get_weather_current('Reykjavik')
        if error is None:
            self.assertIsNotNone(data)
            self.assertEqual(data.name, 'Reykjavik')
        else:
            self.assertIsNotNone(error)

    def test_get_forecast(self):
        data, error = self.weather_gateway.get_weather_forecast('Reykjavik', days=4)
        if error is None:
            self.assertIsNotNone(data)
            self.assertEqual(data.name, 'Reykjavik')
        else:
            self.assertIsNotNone(error)

    def tearDown(self) -> None:
        self.weather_gateway = None


if __name__ == '__main__':
    unittest.main()

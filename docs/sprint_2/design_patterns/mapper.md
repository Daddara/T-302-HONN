# Mapper

## Definition
A mapper is an layer between two subsystems which basically works like a translator. It can for instance map data from one data structure to a different data structure or some map some other functionality. A mapper enables systems to work together while also working independent (vgl. Fowler 2011, S. 473f).

## Use within the project

### Weather API
The weather api uses a gateway to access an external service to retrieve weather data.

[WeatherAPI.com](WeatherAPI.com) provides a lot of data about the weather like the current moon phases and so on. We only want to display a subset of this data like the temperature, if it's raining or not and so on. Using the data in the provided format would make us dependent on the service and would take unnecessary memory. We therefor map the received data onto our own data structures defined in [weather_data.py](workoutapp/weather_service/gateway/weather_data.py). This mapping is also done by the `WeatherApiWeatherGateway` in [weather_gateway.py](workoutapp/weather_service/gateway/weather_gateway.py).

This mapping has the advantage that we can relay on our own data structure. This also enables us to later switch the API we would just have to reimplement the gateway and data mapper.

# Sources

* Fowler, Marting 2011: Patterns of Enterprise Application Architecture. United States: Pearson Education, Inc. 2011. ISBN 0-321-12742-0
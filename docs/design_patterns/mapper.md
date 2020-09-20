# Mapper

## Definition
A mapper is an layer between two subsystems which basically works like a translator. It can for instance map data from one data structure to a different data structure or some map some other functionality. A mapper enables systems to work together while also working independent (vgl. Fowler 2011, S. 473f).

A simple example of a mapper is the gateway design pattern. This design pattern is also used in our application. The documentation can be found here: [gateway.md](docs/design_patterns/gateway.md)

## Use within the project

### Weather API
The weather api uses a gateway to access an external service to retrieve weather data. This access is already an implementation of the mapper pattern in the form of a gateway. This is documented in [gateway.md](docs/design_patterns/gateway.md).

Here I want to focus on the mapping of the data. [WeatherAPI.com](WeatherAPI.com) provides

# Sources

* Fowler, Marting 2011: Patterns of Enterprise Application Architecture. United States: Pearson Education, Inc. 2011. ISBN 0-321-12742-0
# Single responsibility in the weather gateway

## Definition
The single responsibility principle states that every class, module and functions should only have one functionality and there for only be responsible for one thing i.e. have a single responsibility. The scope of this principle vary among definitions. The original statement from Robert C. Martin (also the one we use in our lectures) states that:

> a class should have one and only one reason to change, that “reason to change” is its responsibility

This has focussed on a single class but it can be widened to larger scopes like a module. Note that the responsibility has to be cut down and defined for the target scope. The following responsibility of _managing a web server_ would be way too large for a single class as is contains a lot of partial responsibilities. It would make the the class very complex and bloated. But a module has a larger scope and could have such a responsibility without going against the _single responsibility principle_.

## Use withing the project

### Weather gateway class
The [WeatherApiWeatherGateway](workoutapp/weather_service/gateway/weather_gateway.py) class is an implementation of the [gateway design pattern](docs/sprint_2/design_patterns/gateway.md). In this role it has the the responsibility of

* _Wrapping the functionality of weatherAPI.com into a class interface that can be sued by the rest of the application_

The responsibility of this class includes the connection and translation between our application and the WeatherAPI.com. This is a fairly large responsibility for a single class by the single responsibility principle. This should also still fall in the frame because:
* This is the only responsibility of the class it does nothing besides it's responsibility
* The gateway pattern is defined to be used with only one class this shows that the responsibility is layed out for just one class.
* Spreading the responsibility over several classes would actually make the implementation more complicated. The goal of this pattern is to keep the code simple and maintainable. This implementation is therefor also inline with the goal of the principle :)

### Weather service module
The weather service module it self also follows the single responsibility pattern. It's responsibility is a bit larger than the one of the weather gateway but still focussed on just one function:

* _Provide a single defined interface to retrieve current weather data for the frontend_

This responsibility includes the functions of the weather gateway as well as the handling of http requests and responding in the correct way. This would way to large for a single class but is reasonable for a module like this one. 

### Payment
The single responsibility of the payment system have been documented by _Ægir Máni Hauksson_(@hauks96) in [single_responsibility_payment.txt](docs/sprint_3/lecture_aspects/single_responsibility/single_responsibility_payment.txt)
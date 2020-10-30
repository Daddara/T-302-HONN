# How we would refactor one component into a microservice.

## Definition
Martin Fowler gives no real definition in his presentation about this topic. He instead lists of some common characteristics that most systems with a microservice architecture fulfill. This list includes the following aspects:
1. Componentization via services
2. Organized around business capabilities
3. Products not Projects
4. Smart endpoints and dumb pipes
5. Decentralized Governance
6. Decentralized Data Management
7. Infrastructure Automation
8. Design for failure
9. Evolutionary Design   

These aspects don't state a size of these services. He him self states that there is no real definition(Fowler 2015). 

## Some background information
We want to give some background information about our application before we go into detail on which component we would refactor into a microservice and how. Our current system uses a Django backend and most views are rendered using the Django template system. This system was good to get the website up quickly and to write most code in Python. It is, however, not optimized for microservices due to the constant page reloading.

The problems with constant reloading can be seen with the weather service. The data is always queried from the frontend to enable a more modula system and faster loading times. This causes a lot of unnecessary requests to the same endpoint to get the weather. A microservice architecture with our backend rendering would cause a lot of requests to always retrieve the same data. We would therefor only advice this refactoring if we also switch to a frontend based application. 

Martin Fowler also states that in most cases small to medium sized systems like ours are probably better of using a monolith architecture to figure everything out (Fowler 2015). 

## Microservices

### Our current microservice
The last sprint had a task to implement or identify a second component in our system. We decided to implement a frontend logging server as a new server that can run completely independently on a different server or machine. It also has it's own database and all communication between the components goes over the defined API. The documentation of this component was provided in the last sprint.

This component checks almost all aspects of the definition with the exception of 7. _Infrastructure Automation_. This point can currently not be fulfilled by any of our microservices due to a missing devops team. If we would deploy our application with this or other microservices we would also assign same developers to handle the operations of our system. A part of this job would be to implement a automatic scaling and starting setup. We currently only have a `run-server.sh` script to handle the server startup. 

### Separating another component
We've already mentioned that we created a weather service to display the current weather data in the frontend. This component is currently a part of your main monolith server. However, it can super easily be separated from the main server to be a microservice. It would be a service to provide weather data and nothing more. The service doesn't even use a database this also checks point 6. for having a _Decentralized Data Management_.

The refactoring of this component would be super simple. We would create a new Django server. We can than copy the weather_service module from the `workoutapp` server over. We would than need to change the frontend to request the weather data from our new separated server instead. There are no additional steps that needs to be taken, as the service was already designed to be separable from the main application. This shows that early design can save some work in the future.

## Devops
As mentioned before we can currently not fullfil the point 7. _Infrastructure Automation_. We have scripts to run the server automatically but that's all the _automation_ we've created so far. A real implementation should have more applications along with automatic routing. Having a registered domain with load balancing servers would a big focus in the actual setup it self.

## Meta requirements
Martin Fowler also mentioned that a microservice architecture should have basic monitoring and rapid application development. There is currently no monitoring implementation in our application. We would therefor create a new microservice that monitors our other services and reports unexpected behavior. This component would of course also need to be monitored. A solution for this would be at least two other monitoring services that monitor the entire application along with each other. A failure of on monitor service would therefor leave us with two running systems reporting the failure.

## Sources
1. Fowler, Martin. 2014: Microservices, GOTO 2014. 
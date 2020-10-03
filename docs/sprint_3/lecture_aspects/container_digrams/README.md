# Container Diagram

## Definition
A container diagram displays _High-level technology choices_

### A Container
* Unit of deployment
* Unit of packing
* Unit of reuse (the same container image can be used as a component of many different services)
* Unit of resource allocation
* Unit of scaling

### Intention
* Helps identify overall shape
* High-level technology decisions
* How are responsibilities distributed across the system
* How container communicate with one another
* For developers, tell where the code is

## Our diagrams:
Our application is deployed as a single container. We render our application in the backend and deliver it as a whole to the frontend. The result is a architecture with a lot of dependencies between each module. You could probably deliver some modules on different systems but it would still need a lot of the same code and access to the same database.

The exception to this is the weather_service. This module is completely independent as it is only acced from the frontend and doesn't access anything outside of it self.

We decided to create three diagrams as a result of this:
* 2x of our main container [Diagram 1](https://www.hostpapa.ca/blog/blog/wp-content/uploads/2019/05/image5.png) [Diagram 2](https://miro.medium.com/max/2646/1*847Jp_9BIkm95T42f1Wczw.png)
* 1x of the weather service container [Diagram](https://landingi-client.staginglab.pl/wp-content/uploads/2020/06/404-1024x534-1.png)
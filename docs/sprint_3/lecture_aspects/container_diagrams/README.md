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

### Useful information
* Purpose: “reads data from”, “sends reports to”, etc
* Communication method: Web Service, RESTful, RMI, JMS, etc
* Communication style: synchronous, asynchronous, etc
* Protocols and port: HTTP, HTTPS, SOAP, SMTP, etc

### Boundaries
* IT systems and users that are outside the boundaries of the system

## Our diagrams:
Our application consists out of two containers and two external services. Our backend uses Django. Django handles the connection to the database. The used database it configured using a settings file. We use a local MySQL database for development and we would use a PostgresSQL database in production. Our application is not developed to support micro services it is for that reason a single big application.

Also note that our application uses a service stub for the PayPal interface. The diagrams show the target architecture :). 

We were unsure how to create two reasonable container diagrams from our application. We've decided to have two team members create a container diagram and have it reviewed in a MR to fullfil this requirement and to maybe see if one diagram goes more in depth into a different aspect. 

* [Diagram 1](https://www.hostpapa.ca/blog/blog/wp-content/uploads/2019/05/image5.png)
* [Diagram 2](docs/sprint_3/lecture_aspects/container_diagrams/container_diagram_2.png)

### Diagram 2
![Diagram 2](docs/sprint_3/lecture_aspects/container_diagrams/container_diagram_2.png)
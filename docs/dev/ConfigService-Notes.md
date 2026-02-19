# ConfigService Notes

ED: this page can probably be deleted. Everything worth saving has been moved to [ConfigService](ConfigService.md).

#### Introduction

A configuration service may be the solution if you need more flexibility than the more traditional file based approaches. Such a service makes it possible to 

- use different transport protocols and formats. 
- share properties between applications. (for example ensure that two applications use the same url for a JMS-server.) 
- apply rules and other business logic before selecting which properties to return. 
- let the user setup a monolithic configuration and let the service extract the relevant configuration for a specific application and return a transformed version of the monolithic configuration. 
- set up a GUI for changing the properties.
- switch implementation without changing the clients, as long as the interface is kept stable. See for example [Evolving Service Endpoint](../OWSOA/Evolving-Service-Endpoint-Pattern.md) for more information. 
- add cache support 
    - merge is a possible issue, but can be handled in the service

The list of possibilities above is not meant as a complete list in any way. The idea was just to indicate that introducing a configuration service gives you a lot more flexibility. 

A wide range of technology can be used to implement such a service. For example JMX RPC:  

- JMX-RPC - [Spring supported JMX-RPC](http://static.springframework.org/spring/docs/2.5.x/reference/jmx.html#jmx-proxy) 

#### Design 

###### Integration with applications 

We have identified three options for integration with applications

- Wire it up with Spring (spring modules + commons-configuration seems the easiest implementation) 
- Fetch programmatically 
- Use a bootstrap class to fetch the configuration before starting the application using System.exec on the original main class. 

###### The configuration functionality 

**TODO**: link to multi-dimensional configuration system (formerly known as [staged-spring](http://projects.kaare-nilsen.com/wiki/staged-spring)). 

###### Versioning 

We can achieve traceability and versioning by indexing the configuration. Using [Lucene](http://lucene.apache.org/) as backend should achieve this goal and will additionally give us advanced search functionality for "_free"_. 

###### Client to change configuration 

[Constretto](http://constretto.org/projects/show/constretto)  multi-dimensional configuration system (formerly known as [staged-spring](http://projects.kaare-nilsen.com/wiki/staged-spring)). 

The visualizer was neat. :)

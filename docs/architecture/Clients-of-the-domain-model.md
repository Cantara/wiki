# Clients of the domain model

### Interacting with the domain model

How should clients access the domain model? That depends on the type of client and the underlying [architecture](DDD<sub>~friendly</sub>~architectures.md).

#### Local clients

The optimal solution is client code accessing the domain objects directly. This requires that the client code, for example code in the user interface, and the domain logic lives in the same virtual machine and in the same application context. Say you have a single web application consisting of Struts2, Spring, and Hibernate. The client code, which is Struts2 actions and for example jsp's, can directly interact with any object within the domain layer. An action class can call methods on a Repository for retrieving required objects, it can create a new domain object if the object has a public constructor, and so forth. There is no need for a separate layer between the clients and the domain model.

Some [more discussions](http://domaindrivendesign.org/discussion/messageboardarchive/DomainLayerAccessFromJSPsAndHandlers.html) on this topic are found on the [domaindrivendesign.org](http://domaindrivendesign.org) web site.

#### Remote clients

Remote clients such as web services, swing front-ends, and in the good old days web applications using remote EJBs, must use detached domain objects since the objects are serialized on the network.

##### Alternative #1
A common practice is to add an extra layer, here referred to as the application service layer, between the client and the domain model. The layer is responsible for giving the clients a facade to the domain model, and for mapping domain objects into pure data structures (DTO) and vica versa. The service facade interface should not contain any domain objects.

This certainly adds quite a bit of code and extra work for the developers. The benefit of the application service layer is that you remove the possible misuse and uncertainty of how the objects work on the client side. The client data objects will not be automatically persisted when altered, and they will not always be able to locate the associated services and events. Making the intention clear is always a good thing. Plus that you avoid lazy-loading errors because you convert all objects with all the necessary attributes before returning to the client.

This new layer is also an advantage when the client is not developed as part of the same development team making the domain model (Yes, organizational structures does influence the system design). It can often make it possible to keep the client interface intact and stable while smaller changes are made to the internal domain model.

##### Alternative #2
Critics of the first approach have at least two valid arguments: It reduces the benefit of DDD since this is only fully functioning within the domain layer itself (or any other local clients), and that it may eventually result in duplicated code on the remote client side. If domain objects should be working independently of where the code is executed, then we must either implement remote calls within the domain objects themselves or proxying all domain objects put on the client side. This is of course technical feasible, but not recommended as it brings along all the problems of remote method invocations. 

### Adding UI capabilities to the domain objects

The domain model should not be concerned with specific features needed by the user interface. Remember the [layer dependencies](Package<sub>~structure</sub>~and-layers.md) for domain objects. Nevertheless, the UI layer often needs added functionality or other smaller improvements to the objects. Most often for presentation purposes.

Available techniques:
- Decorator
- Subclassing
- Helper classes
- Mixins
- Win the argument: Yes, it is certainly domain logic, and should be put inside the domain object.

# Seamless integration of JAX-WS and Spring Framework

> ℹ️ 

# The problem

The main problem of integrating Spring and JAX<sub>~WS is that Spring can't control lifecycles of WebService endpoints and handlers in a Java EE environment. That makes autoinjection of dependencies in WebService endpoints and handlers almost impossible without some extra effort. It may sound strange but there is no good portable way to integrate Spring and JAX</sub>~WS. By portable I mean fully Java EE 5 compatible. This will be a core requirement for leveraging all benefits of JAX-WS and JBI.

There exist some projects such as [JAX<sub>~WS Commons](https://jax</sub><sub>ws</sub><sub>commons.dev.java.net/spring/). However, they don't satisfy our requirements. JAX</sub><sub>WS Commons, for example, is not portable in a Java EE 5 environment and is mainly intended for non</sub><sub>EE environments such as Tomcat, embedding the JAX</sub><sub>WS RI as part of the web application. Spring framework provides also some [support](http://static.springframework.org/spring/docs/2.5.x/reference/remoting.html#remoting</sub><sub>web</sub><sub>services</sub><sub>jaxws</sub><sub>export</sub><sub>servlet) for JAX</sub>~WS. Its main limitation is that it supports only configuring WebService endpoints and can't do anything with handlers.

Almost all efforts on integrating Spring and JAX<sub>~WS (including the two approaches mentioned above) are based on deployment of a JAX</sub>~WS web service as a web application and placing Spring application contexts in web.xml. Realizing that for 99% of developers a web service is the same as a web application, it sounds as a reasonable choice. However, there are no such requirements in JAX-WS standard. Assuming that a web service is a web application can lead to dangerouse dependencies on HTTP protocol and SOAP. Such web services will be difficult (or even impossible) to intergrate with JBI JavaEE Service Engine.

# The proposed solution
![Spring_and_JAX<sub>~WS.jpg](Spring_and_JAX</sub><sub>WS</sub><sub>jpg.md)(Spring_and_JAX</sub>~WS.jpg)

The main features of the proposed solution are:
- Total independence of the servlet framework
- One Spring context for each JAX-WS endpoint
- Automatic customizable creation and destroying of Spring contexts
- Automatic autowiring of JAX-WS endpoints
- Spring<sub>~configured service locators for JAX</sub>~WS handlers

Each JAX<sub>~WS endpoint can have its own Spring context. It can be registered in SpringContextRegistry which is a static map where the key is a WS endpoint id and the value is a Spring context created for that WS endpoint. The WS endpoint id is represented with QName of form \[WSs target namespace, WSs name\](WSs</sub><sub>target</sub><sub>namespace</sub><sub>WSs</sub><sub>name.md). SpringContextRegistry ensures that Spring contexts are not shared among different JAX</sub>~WS endpoints and that each JAX-WS endpoint will have exactly one Spring context.

The lifecycle of a JAX-WS endpoint is exclusively managed by Java 5 EE container. The only means of interfering in this process are lifecycle callback methods provided by Java 5 EE. Methods annotated with @PostConstruct are called after the Java 5 EE runtime is finished with objects initialization but before the object is used for the first time. Methods annotated with @PreDestroy are called before the Java 5 EE runtime can utilize the object.

SpringAwareProvider is an abstract class implementing JAX<sub>~WS endpoint interface javax.xml.ws.Provider. It has two responsibilities. The first responsibility is to manage Spring contexts for JAX</sub><sub>WS endpoints with lifecycle callback methods. It uses @PostConstruct method to create a new Spring context and to register it in a SpringContextRegistry when a new JAX</sub><sub>WS endpoint is loaded by Java 5 EE runtime. It uses @PreDestroy method to remove the Spring context from SpringContextRegistry when JAX</sub>~WS endpoint is unloaded by Java 5 EE runtime. SpringAwareProvider has several protected methods for describing how a particular Spring context should be created. The actual WS endpoints can override these methods to customize creation of Spring contexts.

Another responsibility of SpringAwareProvider is to use the newly created Spring context to autowire properties of JAX<sub>~WS endpoints. This is done in @PostConstruct method after the Spring context is created. This requires that a Spring bean representing JAX</sub>~WS endpoint is defined in the Spring context. The beans name can be customized by the JAX-WS endpoint.

Each JAX<sub>~WS handler can serve several JAX</sub><sub>WS endpoints which use different Spring contexts. This makes Spring injection of properties into JAX</sub><sub>WS handlers impossible (at least without locking of the entire handler and thus making it single</sub><sub>threaded). The solution is to use _getter injection_ of _service locators_ instead. A service locator is a Spring</sub><sub>configured bean that knows which services a particular handler needs. This implies that for each JAX</sub>~WS handler we would need to create a special service locator. It is also possible to create a single service locator that knows about all available services and use the same service locator for all handlers. I think that in practice the combination of these two approaches will be the most reasonable.

The term _getter injection_ means that instead of modifying the objects internals by setting some value we intercept a call to getter method and return whatever we want. It can be implemented in multiple ways. The simplest solution in our case is to allow all JAX-WS handlers extend an abstract class ServiceLocatorAwareHandler. Its getServiceLocator(...) method returns the correct instance of service locator (from the correct Spring context) for each client request.

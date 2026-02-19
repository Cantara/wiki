# Self Monitoring Service Pattern

### Problem

An overview over which services are used by which clients, and the frequency of their usage, is needed in order to be able to do impact analysis of what the consequences are when making changes to the contract of a service.

### Context

Enterprise with many services. Nobody has a total overview of which services are used by which clients.

### Forces

- The services are implemented in many different technologies (MQ, CORBA, Java RMI, web services, CICS, etc), which means that there is no EAI/ESB product that can provide a solution to the problem.

### Solution

Enforce a service usage protocol that requires a client to identify itself by using a [Security Token](/web/20210120142306/https://wiki.cantara.no/display/OWSOA/Security+Token "Security Token"). The token should contain enough data to identify the client in a unique manner. The service will then log this data in some appropriate format, which in turn is used to generate reports regarding the usage of the service.

### Resulting Context

When implemented, the enterprise will have a automatically updated overview of usage patterns of the services.

### Rationale

TBD

### Related patterns

- <http://www.eaipatterns.com/ControlBus.html>

### Discussion

**ESB solution?** In the forces section we state that no EAI/ESB products support this "out of the box". This the case as far as we know, but if anybody knows about ESB's that provide this, then please tell us.

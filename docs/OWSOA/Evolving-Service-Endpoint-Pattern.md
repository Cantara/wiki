# Evolving Service Endpoint Pattern

### Problem

Core Services will over time aquire a large number of clients in the Enterprise. Changes to the Core Service contract will increase in cost for every new client if the service cannot take responsibility for supporing the legacy clients and new clients concurrently behind its boundry.

### Context

This pattern applies to implementation of Core Services. Core Services are in the lower end of the service stack and is by nature less evolvable. Core Services must have the ability to change without significant ripple effects for clients. In order to assure this Core Services should adhere to this pattern to support continous support of legacy clients during change.

Core Services also often have dependencies to one or more underlying systems.

### Forces

- Changes in the businessdefinition of the Domain Object being delivered
- New requirements from clients
- Evolving request protocols and/or formats from clients
- Changes in underlying systems, like upgrades may call for the support of new features.

### Solution

A set of stereotype classes implement the responsibility required in for this pattern:

#### Class Diagram

#### Sequence Diagram

|  | Will be updated for the new version of the class diagram |

#### DomainPersistenceServiceEndpoint

The DomainPersistenceServiceEndpoint stereotype is responsible for exposing the single active operation for the service:

The DomainPersistenceServiceEndpoint is responsible for calling the OperationInterpreter to retrieve the corresponding Command.

#### OperationInterpreter

The OperationInterpreter is responsible for mapping the requestOperation from the CoreServiceEndpoint to a concrete command and provide the command with the appropriate PayloadInterpreter for the requestOperation. The Operation Interpreter acts as a Factory for the commands based on the requestOperation input.

#### Command

The command is responsible for calling the PayloadInterpreter to produce a payload that is understood by the DSP (See Enterprise Repository Pattern). When the PayloadInterpreter has succeeded in interpreting the payload the command calls the DSP to execute the operation. The command will ensure to use the same PayloadInterpreter to map the response from the DSP before returning.

#### PayloadInterpreter

The payload interpreter is responsible for mapping incoming requestPayload from the CoreServiceEndpoint to a format understood by the DPS and for mapping the response from the DPS back to the dialect used by the caller.

### Resulting Context

When exposed, the CoreServiceEndpoint will enable the service implementation to evolve at the same time as it may continue to support existing clients.

### Rationale

TBD

### Related patterns and implementations

- [Consumer-Driven Contracts: A Service Evolution Pattern](http://martinfowler.com/articles/consumerDrivenContracts.html)
- [Service Dialect Adapter pattern implemented as JAX-WS handler](/web/20210621073324/https://wiki.cantara.no/display/OWSOA/Service+Dialect+Adapter+pattern+implemented+as+JAX-WS+handler "Service Dialect Adapter pattern implemented as JAX-WS handler")

### Extensions / Advanced Scenarios

#### Business Rule Autodocumentation

#### CoreServiceEndpoint Receipt Strategy

In order to improve the clients ability to evolve with the Core Service a receipt response may be implemented. The receipt may implement the following:

- Warnings
- Errors
- ResponsePayload
- Incentives for upgrading

#### NotUnderstood Tracking Pattern

The [NotUnderstood Tracking Pattern] can extend the Evolving Service Endpoint Pattern to assure that the service keeps track of communication that it doesn't understand. This pattern uses a Log and Alert strategy for any request that it cannot serve. If the Receipt Strategy is in place one would naturally express this situation in the receipt and also include the most understood format as a Template (Example) in the response so that the client can analyze the primary request format and adjust accordingly. This will in some degree produce a self-documenting service and will be a strong productivity factor in integration scenarios where developers tune their clients to request properly.

#### Evolving Service Validation Pattern

The [Evolving Service Validation Pattern] enables complex validation logic for requests to the service to be handled internally. This pattern ensures that all rules are exposed to clients, but implementation of the logic is maintained and enforced by the service itself. Clients may implement their own enforcement of the logic, or rely on the service validation operations to validate requests.

The [Evolving Service Validation Pattern] is targeted at enforcing complex businesslevel validation logic and should be used in context with the [Enterprise Domain Repository Pattern](/web/20210621073324/https://wiki.cantara.no/display/OWSOA/Enterprise+Domain+Repository+Pattern "Enterprise Domain Repository Pattern").

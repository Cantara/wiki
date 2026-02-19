# Agent pattern

### Name

Agent pattern or Agent architecture

### Problem

We want access to functionality or data offered by and application or database, but the application/database does not offer the endpoints we want and we do not want to modify the existing application/database. Typical inadequacies which can be addressed:

- HTTP only, HTTPS not supported
- Synchronous endpoints, but want asynchronous
- No payload encryption

Incoming traffic is not possible or unwanted due to firewalls and routing policies.

### Context

### Forces

### Solution

Implement a standalone application, an agent, with integrates with the application or database you want to extend with new integration functionality. The agent will act as a communication proxy between the target application/database and the outside world.   
The agent will initiate all communication, and all communication is HTTPS based. Firewalls must allow *outgoing* HTTPS traffic (port 443), but can block all incoming traffic.

The agent must have direct access to the endpoints offered by the legacy application and should be deployed on the same machine or at least on a machine as close to the target machine as possible.

The agent will typically *poll* an incoming queue for requests to process and publish any outgoing messages to another queue, but these endpoints might also be a REST endpoint or similar.

The agent may also run a web server and expose SOAP, REST or json-over-http endpoints.

### Resulting Context

### Examples

The diagram shows how the agent integrates with your system and four examples of services on the target network to integrate with;

- Agent --> SOAP service
- Agent --> queue (no security mechanisms, so cannot be exposed outside the LAN)
- Agent --> SQL database
- Agent expose a web server which another on-premise application can call.

*[Diagram: agent-architecture]*

### Rationale

### Related Patterns

[Proxy pattern](https://en.wikipedia.org/wiki/Proxy_pattern)

Also related to [Edge computing](https://en.wikipedia.org/wiki/Edge_computing)

### Known Uses

### Credits

This pattern was (to my knowledge) first described by Thor Henning Hetland June 2015.

Documentation template from <http://www.opengroup.org/public/arch/p4/patterns/patterns.htm>

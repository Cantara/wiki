# Integration architecture and testability

- Webservices - synchronous - not a big problem, but often more cumbersome than e.g. asynchronous JMS. **Todo**: elaborate 

- Direct integration with RDBMS - big, big problem 

- Logical queues implemented using database table - theoretically not a problem, but there is no infrastructure support for the Queue concept, so misuse happens. 

- Integration with custom hardware - testability must be built-into the architecture 

- Integration with services which cannot easily be managed (e.g. [dev:Control state](../dev/Control<sub>~state.md)) - testability must be built</sub>~into the architecture 

- Application containers - poor testability with most implementations 

- ESB - poor testability with most implementations 

- JNDI - not a problem 

- JMS - not a problem 

- Key-value stores - not a problem 

- LDAP?

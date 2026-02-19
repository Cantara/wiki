# ConfigService

#### TODO

- Does something like this exist already? 

- Ask Kaare about current state of [Constretto wiki](https://constretto.jira.com/wiki/display/CC/Constretto), [Constretto @ GitHub](https://github.com/constretto). 

#### API 

- getValue(String key, String identityParm...)

- getConfigContext(String contextId, String identityParm...) 

- getConfigContexts(String identityParm...) 

###### Identity 

- Use a SSO service to obtain a token for identity. 

- Environment variables like IP address, serviceId (e.g. com.company:app1:1.2.3), environment, 
    - No authentication really 

#### Integration 

- Stateless 

- Synchronous 

- Multiple endpoints 
    - E.g. JSON, XML, JMX/MBeans  

- Use environment variable to obtain the url to the ConfigService. 

#### Configuration consumer  

Usage does not require a client library, but we could create a library to reuse a few nice features. 

- Local configuration cache 

- Separate booted from running state
    - Infer a _booted_ as a separate state from _running_. Can implement retry-functionality to improve reliability. (Can try to initialize the Spring AppContext later if it fails because an external service is unavailable. 
    - Catch exceptions related to state change from booted to running and handle these appropriately. 
    - Don't get stuck in _failed_ state. If we don't try to recover or something from a failure, it is better to just do a System.exit() and die. 

#### Server 

- Possible to share configuration parameters between applications/nodes. 
    - A single entry to update a property, even if it is used multiple places. 
    - Example: Two services that communicates with JMS need to use the same JMS-server.

- Node specific configuration must be possible

- A configuration must be connected to a version
    - Traceability: Possible to save a configuration so it can be restored later. 
    - We can achieve traceability and versioning by indexing the configuration. Using [Lucene](http://lucene.apache.org/) as backend should achieve this goal and will additionally give us advanced search functionality for "_free"_. 

- Isolation between environments 
    - Ensure that test environments do not affect production or each other. 

- Separate different types of configuration
    - See [Configuration Categorization](Configuration-Categorization.md)

- Concept of a _context_ which can be given a name/id 
    - The idea is to support multiple sets of configuration for a single client. 

#### Configuration admin client 

- GUI to add, remove and change configuration. 

- JMX 

#### Old notes 

[ConfigService Notes](ConfigService-Notes.md)

[ConfigService Notes2](ConfigService-Notes2.md)

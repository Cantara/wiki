# ConfigService Notes2

ED: this page can probably be deleted. Everything worth saving has been moved to [ConfigService](ConfigService.md).

## Configuration 

#### Requirements, drivers and goals 

- Possible to share configuration parameters between applications/nodes. 
    - A single entry to update a property, even if it is used multiple places. 
    - Example: Two services that communicates with JMS need to use the same JMS-server.

- Node specific configuration must be possible

- A configuration must be connected to a version
    - Traceability: Possible to save a configuration so it can be restored later. 
    - EditAsNew is a niceToHave feature

- Isolation between environments 
    - Ensure that test environments do not affect production or each other. 

- Separate different types of configuration
    - See [Configuration Categorization](Configuration-Categorization.md)

- IoC is popular these days, especially Spring, the configuration strategy must thus integrate nicely with Spring. 

- A **nice to have** feature: Configuration that can be overridden should show what syntax to use. (E.g. a file with key=value as comments) 

**Resources**: [Basic configuration tactics](Basic<sub>~configuration</sub>~tactics.md). 

#### Implementation 

ConfigService + Commons<sub>~Configuration + spring</sub>~module-commons

The complexity of the ConfigService can be reduced if the applications handle some of the configuration. 
For example let each application check whether all required external services are configured correctly and are available (otherwise die and log an error message). 

## ConfigService 

- ConfigService implemented as client<sub>~server with JMX</sub>~RPC as transport protocol. 

- Use [Configuration Categorization](Configuration-Categorization.md) as basis for a tree/graph based XML structure. Properties are inherited from nodes closer to the root and can be overridden in a leaf node. 

- Use XML and an XSD schema allows using standard tools for verifying syntax. (Config verification) 

- Each category is given an ID. Put together, the IDs for each level identifies an unique configuration. 

- Store a copy of the configuration locally to avoid single-point of failure. Notify (logging) when using a possible stale configuration or when a local version differs from the version pulled from ConfigService. 

#### Questions 

- How to persist the configurations?

- How to implement versioning? 
    - Let Lucene index the whole structure

- Is there an Open Source XML editor that can be embedded in a Java or web gui available? 

- Which type of service according to [OWSOA:Service Categories](../OWSOA/Service-Categories.md)? 
    - CS

- How to obtain the url to the ConfigService? 
    - environment variable 

- How should the ConfigService API look like? 
    - Need to be evolvable

# Neo4j deployment alternatives

Docs: http://docs.neo4j.org/chunked/milestone/ha.html

#### Embedded database 

- Each application node embeds a Neo4j database. 
- Can utilize Neo4j native Java API and Spring datagraph. 
- A batch job (implemented in any language) reads from a standalone Neo4j server which expose a REST interface and updates a relational database (e.g. Oracle, MySQL, PostgreSQL) for reporting purposes. 

Is this deployment architecture possible with Neo4j? 

Can both java nodes write to different Neo4j databases using the native Java api? 
"A slave will handle writes by synchronizing with the master to preserve consistency. " 

**[Diagram: neo4j](../Diagram/neo4j.md)**

#### Standalone Neo4j cluster

- Each application communicates using the REST API. 
    - Is Spring datagraph useful when using the REST API?
- A batch job (implemented in any language) reads from a standalone Neo4j server which expose a REST interface and updates a relational database (e.g. Oracle, MySQL, PostgreSQL) for reporting purposes. 

**[Diagram: neo4j_cluster](../Diagram/neo4j_cluster.md)**

#### Event sourcing

All changes to the domain model must be modeled as events. This may or may not be suited for your context. 

**[Diagram: neo4j_eventsourcing](../Diagram/neo4j_eventsourcing.md)**

1. Eventlogg og Rapportering i RDBMS
1. Nåtilstand i Neo4j
1. All skriving gjennom en EventHandlerService. 
1. Lesing fra applikasjonsnoder rett mot Neo4j. 
1. App (eller supportapps) kan også bygge oppå eventlog for å svare på audit-spørsmål.

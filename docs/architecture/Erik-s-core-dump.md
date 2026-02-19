# Erik's core dump

In what contexts is it useful to consider non RDBMS based products? 
Which products? 

- Useful technical NoSQL pattern overview: [http://horicky.blogspot.com/2009/11/nosql-patterns.html](http://horicky.blogspot.com/2009/11/nosql-patterns.html)

- One interface for each property 

- Concrete implementations with different combinations of properties. Each combo should be optimized for a certain context. 
    - E.g. [NoSQL alternative to RDBMS - CRUD app](NoSQL-alternative-to-RDBMS-CRUD-app.md)
    - Extreme performance (JavaSpace, Coherence)
    - Extreme scalability (Google Bigtable, key-value stores) - scale for size 

- Every implementation follow the [SOA Design Rules](../KM/Design-Time-Governance-SOA-Design-Rules.md) for a Core Service. Perhaps traits or mixins can be used to reuse certain properties (e.g. [P41. A service shall provide heartbeat and traffic monitoring](../KM/P41-A-service-shall-provide-heartbeat-and-traffic-monitoring.md)). 

- By adhering to design guidelines for a CS we achieve
    1. We can continue to add more CS and ACS later without a total rewrite. 
    1. It is easier to know what and how to design and implement the service. 
    1. HOWEVER, this approach must be _easier_ than standard use of Oracle db. This will probably mean that there should be implementations for the most common contexts available for reuse.

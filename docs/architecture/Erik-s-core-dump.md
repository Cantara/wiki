# Erik's core dump

In what contexts is it useful to consider non RDBMS based products? 
Which products? 

- Useful technical NoSQL pattern overview: [http://horicky.blogspot.com/2009/11/nosql<sub>~patterns.html](http://horicky.blogspot.com/2009/11/nosql</sub>~patterns.html)

- One interface for each property 

- Concrete implementations with different combinations of properties. Each combo should be optimized for a certain context. 
    - E.g. [NoSQL alternative to RDBMS - CRUD app](NoSQL<sub>~alternative</sub><sub>to</sub><sub>RDBMS</sub>~CRUD-app.md)
    - Extreme performance (JavaSpace, Coherence)
    - Extreme scalability (Google Bigtable, key-value stores) - scale for size 

- Every implementation follow the [SOA Design Rules](../KM/Design<sub>~Time</sub><sub>Governance</sub><sub>SOA</sub><sub>Design</sub><sub>Rules.md) for a Core Service. Perhaps traits or mixins can be used to reuse certain properties (e.g. [P41. A service shall provide heartbeat and traffic monitoring](../KM/P41</sub><sub>A</sub><sub>service</sub><sub>shall</sub><sub>provide</sub><sub>heartbeat</sub><sub>and</sub>~traffic-monitoring.md)). 

- By adhering to design guidelines for a CS we achieve
    1. We can continue to add more CS and ACS later without a total rewrite. 
    1. It is easier to know what and how to design and implement the service. 
    1. HOWEVER, this approach must be _easier_ than standard use of Oracle db. This will probably mean that there should be implementations for the most common contexts available for reuse.

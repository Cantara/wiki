# scale large data in the infrastructure layer

Case: Web crawling
Problem: Downloads teh intarwebs. Process teh intarwebs.

Scenario: fat servers

- Reliable, expensive, high-end servers
- => assume reliability => low fault tolerance
- Local disks, no RAID
- Partitioned by domain name part of URL
- Hierarchical network (to compensate for lack of switch bandwidth)
- Consequences: failures are more expensive

Scenario: Skinny servers:

- Commodity, consumer grade, cheap servers
- => assume frequent failures => fault tolerant software
- Abundance of CPU and to some extent RAM
- Communication-heavy, chatty
- Consequences: more moving parts => higher management overhead (can compensate w/ Puppet, Chef, etc and other automation)

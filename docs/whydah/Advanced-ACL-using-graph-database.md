# Advanced ACL using graph database

Use case: A company communicates with a lot of sensors, for example power meters to measure power consumption for private households. Data can be collected from the sensors and they have an administration API to allow changing each meter's configuration. The company want its applications to collect the data, process the data and administrate the meters. Some reports are sold to human users directly, some raw measurements are sold to the company's partners and the company use the data for different purposes internally (preventive maintenance, optimizing configuration, etc.).

Keywords:

- Graph database
  - Physical location of meters (Street address, city, country)
  - Organization structure (company which owns the lines, company which currently bills the household)
  - Access Control tree (read data, write config changes)

- Whydah

#### Design overview

**TODO**: Describe in detail what data is stored in the graph database and what is stored in Whydah.

The general design is to use Whydah for authentication and authorization and use a graph database to handle the extra dimension of *resources*. There must be some shared data which uniquely identifies what set of resources a given user or application is allowed to access. It is also natural to imagine several roles (e.g. read and write) associated with a resource.

- ~~Alternative 1~~: Model the resources as an application in Whydah and use the role concept for the different access modes.
  - This makes it necessary to store a reference to all resources within Whydah.
  - Poor performance scalability
  - Bad mapping to human's mental model
  - Misuse of Whydah

- Alternative 2: Model users and applications and the relations to the resources (access roles) in the graph database.
  - It "feels" like a bad idea to duplicate userId and applicationId in the graph database.
  - It would be nice to have all "roles" in Whydah and nowhere else.
  - **Choice**: only have a single role/relation between user/application and resource OR have several (e.g. read and write).
  - I think we landed on *has\_access* and an additional *no\_access* (deny) relationship.
  - **Resources** (think of it as data) is a new dimension which is not supported in Whydah. Organization structure (of resources) is normally a tree structure.
  - Normally different couplings to the tree structure of resources; i.e. we have a graph.

So, userIds, applicationIds and resource access roles are stored in the graph. The user or applicationToken is used when querying for a set of resources.

---

- Customer organization structure

- Resource ownership

- A user or application has relations to a resource, but fine-grained access within an application is NOT supported.
  - No roles in the graph, roles only live in Whydah.
  - No coupling between user and application in the graph, those relations live in Whydah.

### Use cases / queries

- List resources a given user/application *has\_access\_to*

- List resources *owned\_by* an organizational unit

- List users/applications which *has\_access\_to* an organizational unit

- List users which *belongs\_to* an organizational unit

- List organizational units with resource count *owned\_by*/*franchised\_by* an organizational unit

### Graph

- Franchise vs owned\_by

- has\_access (read, write is handled by the applications)

###### Stores (resources)

[Dot syntax for stores graph example](/web/20230208100847/https://wiki.cantara.no/display/whydah/Dot+syntax+for+stores+graph+example "Dot syntax for stores graph example")

###### Production company

[Dot syntax for Production company graph example](/web/20230208100847/https://wiki.cantara.no/display/whydah/Dot+syntax+for+Production+company+graph+example "Dot syntax for Production company graph example")

###### Franchise organization

[Dot syntax for Franchise organization graph example](/web/20230208100847/https://wiki.cantara.no/display/whydah/Dot+syntax+for+Franchise+organization+graph+example "Dot syntax for Franchise organization graph example")

###### Combined with access and admin rights

[Dot syntax for combined graph example](/web/20230208100847/https://wiki.cantara.no/display/whydah/Dot+syntax+for+combined+graph+example "Dot syntax for combined graph example")

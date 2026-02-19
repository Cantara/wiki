# Real SOA versus REST

This is an interesting question. There are in fact one key similarity between Real SOA (unlike most other SOA strategies) and REST, and that is that Real SOA puts resources/business data as first class citizens of the architecture (ACS and CS category services) which mimics the resource-oriented architecture of most successful REST approaches. Other than that, REST is mainly an architectural style where Real SOA is an architecture, so a feature-by-feature comparison does not provide much value.

**REST is an architectural style which has 4 fundamental constraints:**

1. Identification of resources
2. Manipulation of resources through representations
3. Self-descriptive messages
4. Hypermedia as the engine of application state

Our question is: Can we design a system using Real SOA architectural rules and conforming to REST architectural constraints. This question can be answered by looking at how each REST constraint is supported by Real SOA.

| REST constraint | Applicable to Real SOA | Comment |
| --- | --- | --- |
| 1. Identification of resources |  | All Real SOA services can be identified/ID |
| 2. Manipulation of resources through representations |  | Real SOA manifests the each service should be able to support multiple interfaces (ESE and the like) |
| 3. Self-descriptive messages |  | Just implementation details of the service endpoint |
| 4. Hypermedia as the engine of application state |  | Implementation detail, but real SOA services should be reusable/building blocks which means that coupling to clients workflows must be minimal. Services with hypermedia workflow suggestions are best suited for H2A services in Real SOA. Rickard Øberg [suggest](http://www.jroller.com/rickard/entry/the_domain_model_as_rest) an additional Use-case strategy for designing REST endpoints, which separates the CS/ACS and the A2A/H2A REST strategies which make REST a compatible implementation strategy for real SOA. |

The fourth REST architectural constraint is obviously conflicting with Real SOA architectural rules. Actually it conflicts with all SOA approaches because of the general mismatch between SOA and REST mindsets. Reusablity of services is one of the main SOA requirements. It allows the composition of services to create new services and this is a good thing. It also allows the clients to create new workflows of services and the number of these workflows is potentially unlimited. Thus, a well designed SOA framework can grow very easy both in the number of services and the number of clients.

The RESTful services **are** workflows themselves. After each invocation they tell the client what to do next. Each client may want to have each own workflow and that requirement constraints the degree of service reuse. This means that **reusability can not be a goal of the RESTful services**. (This also raises some discussions of separation of workflow responsibility between the REST services and the clients of the REST services which have yet to been defined clearly within the REST community.)

Another way to look at this is by the following anology: static vs. dynamic view of the system. SOA is focused on the static view of the system. It defines where the data/functionality can be found and is not very concerned about the data movement. REST provides the dynamic view of the system. Its main focus is the movement of data across the system.

These differences between SOA and REST don't mean that Real SOA and REST are completely incompatible. Instead, they are complementary. RESTful services can be built on top of SOA services and act as client-aware proxies to SOA services. This will work very well with Real SOA because Real SOA fully supports the three first fundamental REST constraints.

**Note** REST-style endpoints are excellent candidates for endpoints in Real SOA, both self standing and as complementary endpoints to WS-\* endpoints and other protocols.

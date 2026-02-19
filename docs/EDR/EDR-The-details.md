# EDR - The details

### Problem

Most enterprises have several systems which own parts of a domain object. The data from these systems might be disjoint, as well as overlapping. The data quality and SLA requirements for each system are often of diversified quality. We need a standardized way to handle multi-source domain objects, and to extend the Domain repository to handle the real-world CRUD of todays enterprises.

### Context

The exposure of services that provide an Enterprise Domain Repository usually form the Core Services in an architecture based on the Service Categorization model. This pattern should be applied to establish maintainable Core Services which can support multiple providers of data for domain-object construction. The Domain Objects exposed usually map to core business terminology such as:

- Customer
- Contract
- Product
- Order

The Enterprise Domain Repository pattern is usually applied where multiple systems are candidates for delivering parts of data to construct a Domain Object. This pattern may be combined with the [Evolving Service Endpoint Pattern](/web/20210922165625/https://wiki.cantara.no/display/OWSOA/Evolving+Service+Endpoint+Pattern "Evolving Service Endpoint Pattern") to construct a complete service for distributed exposure.

Enterprise Domain Repository should not be used to map several domain objects into a single domain object. A Agregated Core Service is the apropiate solution for this kind of mapping.

### Forces

- Business definition of a Domain Object requires data from disparate systems
- Need for integrating multiple core systems cause high complexity
- Integrating directly from clients towards core systems reduces system evolvability
- Services exposed with higher granularity and larger responsibilities grow too complex over time

### Solution

The Enterprise Domain Repository's main responsibility is to provide unified access to Domain Objects in the Enterprise. To achieve this the repository must maintain control of the objects and the providers that supply the data that constructs them. This implies that the Enterprise Domain Repository has to take some form of responsibility for correlation of providersystem identificators.

Another major responsibility is to take decisions on field mapping configuration between the providersystem representations of the data.

| Legend |  |  |
| --- | --- | --- |
| Element | Responsibility | Details |
| EvolvingServiceEndpoint | Representing the Domain Persistence Service | Uses the Enterprise Domain Respository |
| RepositoryController | Call ProviderController and DomainObject factory and manage Repository | The main public interface for the Enterprise Domain Repository |
| Correlator | Correlate the ProviderObjects for the RepositoryController and provide logical Ids | the implementation supplying Id correlation services to the Repository |
| Repository | Keep a store of DomainObjects as cache or efficient query store | May be implemented in memory or presistent |
| ProviderController | Keep track of registered controllers and execute cross-provider calls | Supports the Correlator and the RepositoryController |
| Provider | Encapsulate all complexity in calling the underlying system the provider represents | The provider representing a core system |
| ProviderObject | Expose relevant fields from the provider specific representations of data | The object containing Provider Specific data |
| DomainObjectFactory | Construct the domain object | Construct the domain object based on input from the Repository Controller |
| DomainObject | Expose the main DomainObject definition managed by the Enterprise Domain Respository |  |

#### Repository Controller

The primary responsibility of the Repository Controller is to deliver Domain Objects to its clients and to receive Domain Objects to persist through its providers.

#### Domain Object

Domain Object holds data and business functionallity. In this context the Domain Object will hold data that resides in  
different core systems.  
The Domain Object can be serialized, and then passed on to the client. This approach enables the client to perform operationg  
on the actual Domain Object.

#### Correlator

The Repository Controller must support ID correlation between Providers used by the EDR. This is vital in order to construct Domain Objects from multiple Provider Objects. The ID correlation mechanism may be an internal implementation or external package designed for this purpose.

#### Repository

The Repository is responsible for storing the Domain Objects in a persistent or non-persistent store. This store may be in-memory cache, file/xml-based persistence or a database. In many cases it can prove useful to have a persistent store which will give opportunities for scaling and better performance.

#### Provider Pattern

The Provider pattern is used to abstract communication with underlying systems. The providers should be focused and specialized on delivering only the required Provider Objects required by the Repository Controller to construct the Domain Objects. The main responsibility of the Provider is to deliver Provider Objects from one and only one source system to the Repository Controller in a coherent manner and abstract all complexity of the underlying system to the Repository Controller.

#### Provider Object

The Provider Object is a representation identical to, or tightly coupled to the semantics of the underlying system. In many cases it may be reasonable to implement the Provider Object using the Aggregate pattern in order to hide unnecessary complexity from the underlying system towards the Repository Controller.

We recomend that the Provider Object has two different id's. Provider Id is the same Id as are found in the Core system. The second id, Logical Provider Id is created by the Correlator.

### Resulting Context

The Enterprise Domain Repository Pattern provides a clear separation of concerns between system specific integration complexity, ID Correlation between systems, repository management, field mapping and merging strategies. The Repository Controller provides a clean repository analogy to the containing service, leaving the service responsibilities clean and abstracted away from integration complexity.

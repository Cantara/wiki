# Enterprise Domain Repository

**How can we manage domain objects created with data from multiple back-ends?**

### Problem

Most enterprises have several systems which own parts of a domain object.  
The data from these systems might be disjoint or partly, sometimes even completely, overlapping. The  
data quality and SLA requirements for each system are often very different.   
We need a standardized way to handle multi-source domain objects, and to extend the Domain repository to handle the real-world CRUD of today's enterprises.

Forces:

- Business definition of a Domain Object requires data from disparate systems.
- Need for integrating multiple core systems cause high complexity.
- Integrating directly from clients towards core systems reduces system evolvability.

### Solution

Use a single service which hides all the complexity of reading and writing, management of multiple data sources, handle composition of the domain object and caching strategies.

|  |  |  |
| --- | --- | --- |
| Application This pattern should be applied to establish maintainable Services which can support domain-object construction where the data is maintained in more than one back-end system. Typical domain-objects might be:   - Customer - Contract - Product - Order    You need to create a service with several components, each responsible for a single task. The tasks are: - Domain object composition. - Domain object caching. - Data retrieval and update from a single back-end system. - Key management. |  | Impacts The addition of the different components introduces design and development effort and using the resulting service may lead to performance overhead. |

|  |  |  |
| --- | --- | --- |
| Principles [Service Composability](http://www.soaprinciples.com/service_composability.asp),[Service Loose Coupling](http://www.soaprinciples.com/service_loose_coupling.asp), [Service Abstraction](http://www.soaprinciples.com/service_abstraction.asp) (all from Erl)  Use Enterprise Domain Repository to build a single Domain Object as a [Core Service](http://wiki.community.objectware.no/display/OWSOA/CS). Enterprise Domain Repository should not be used to map several domain objects into a single domain object. An [Aggregated Core Service](http://wiki.community.objectware.no/display/OWSOA/ACS) is the appropriate solution for this kind of mapping. (principles from Objectware Community)  An example illustrating this if if you have a Product domain object, created from two provider objects ShipProduct and ShipProductDescriptions. |  | Architecture Service, The Enterprise Domain Repository Pattern provides a clear separation of concerns between system specific integration complexity, Key Correlation between systems, repository management, field mapping and merging strategies. The Repository Controller provides a clean repository analogy to the containing service, leaving the service responsibilities clean and abstracted away from integration complexity. |

### Problem described

Most enterprises have several systems which own parts of a domain object. The data from these systems might be disjoint, but often it is partly or completely overlapping. The data quality and SLA requirements for each system are often very different. We need a standardized way to handle multi-source domain objects, and to extend the Domain repository to handle the real-world CRUD of today's enterprises.

### Solution described

The Enterprise Domain Repository's main responsibility is to provide unified access to Domain Objects in the Enterprise. To achieve this the repository must maintain control of the objects and the providers that supply the data that constructs them. This implies that the Enterprise Domain Repository has to take some form of responsibility for correlation of multiple providers system identifications.

Another major responsibility is to take decisions on field mapping configuration between the provider system representations of the data.

| Legend |  |  |
| --- | --- | --- |
| Element | Responsibility | Details |
| EvolvingServiceEndpoint | Representing the Domain Persistence Service | Uses the Enterprise Domain Respository (This is an extention, and not required) |
| RepositoryController | Call ProviderController and DomainObject factory and manage Repository | The main public interface for the Enterprise Domain Repository |
| Correlator | Correlate the ProviderObjects for the RepositoryController and provide logical Ids | the implementation supplying Id correlation services to the Repository |
| Repository | Keep a store of DomainObjects as cache or efficient query store | May be implemented in memory or presistent |
| ProviderController | Keep track of registered controllers and execute cross-provider calls | Supports the Correlator and the RepositoryController |
| Provider | Encapsulate all complexity in calling the underlying system the provider represents | The provider representing a core system |
| ProviderObject | Expose relevant fields from the provider specific representations of data | The object containing Provider Specific data |
| DomainObjectFactory | Construct the domain object | Construct the domain object based on input from the Repository Controller |
| DomainObject | Expose the main DomainObject definition managed by the Enterprise Domain Respository |  |

**Repository Controller**

The primary responsibility of the Repository Controller is to deliver Domain Objects to its clients and to receive Domain Objects from providers as well as to persist Domain Objects through its providers.  
Domain Object  
Domain Object holds data and business functionallity. In this context the Domain Object will hold data that resides in different core systems.  
The Domain Object can be serialized, and then passed on to the client. This approach enables the client to perform operating  
on the actual Domain Object.

**Correlator**

The Repository Controller must support Key correlation between Providers used by the EDR. This is vital in order to construct Domain Objects from multiple Provider Objects. The Key correlation mechanism may be an internal implementation or an external package designed for this purpose.

**Repository**

The Repository is responsible for storing the Domain Objects in a persistent or non-persistent store. This store may be an in-memory cache, a file/xml-based persistence or a database. In many cases it can prove useful to have a persistent store which will give opportunities for scaling and better performance.  
Provider Pattern

The Provider pattern is used to abstract communication with underlying systems. The providers should be focused and specialized on delivering only the required Provider Objects required by the Repository Controller to construct the Domain Objects. The main responsibility of the Provider is to deliver Provider Objects from one and only one source system to the Repository Controller in a coherent manner and abstract all complexity of the underlying system to the Repository Controller.  
Provider Object

The Provider Object is a representation identical to, or tightly coupled to the semantics of the underlying system. In many cases it may be reasonable to implement the Provider Object using the Aggregate pattern in order to hide unnecessary complexity from the underlying system towards the Repository Controller.

We recomend that the Provider Object has two different keys. Provider Key is the same Key the one found in the Core system. The second Key, Logical Provider Key is created by the Correlator.

To fully support data updates one of three strategies must be selected:

- All updates, from all clients must pass through this service.
- The service must receive update notification events from the back-ends.
- Short lifetime of cached objects.

### Related patterns

- [Entity abstraction](http://soapatterns.org/entity_abstraction.asp)

### Extensions

This pattern may be combined with the [Evolving Service Endpoint Pattern](http://wiki.community.objectware.no/display/OWSOA/Evolving+Service+Endpoint+Pattern) to construct a complete service for distributed exposure.

### Attribution

- Objectware Community Wiki (wiki.community.objectware.no)

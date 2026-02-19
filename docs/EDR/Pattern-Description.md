# Pattern Description

### Problem

Most enterprises have several systems which own parts of a domain object. The data from these systems might be disjoint, as well as overlapping. The data quality and SLA requirements for each system are often of diversified quality. We need a standardized way to handle multi-source domain objects, and to extend the Domain repository to handle the real-world CRUD of todays enterprises.

### Context

The exposure of services that provide an Enterprise Domain Repository usually form the Core Services in an architecture based on the Service Categorization model. This pattern should be applied to establish maintainable Core Services which can support multiple providers of data for domain-object construction. The Domain Objects exposed usually map to core business terminology such as:

- Customer
- Contract
- Product
- Order

The Enterprise Domain Repository pattern is usually applied where multiple systems are candidates for delivering parts of data to construct a Domain Object. This pattern may be combined with the Evolving Service Endpoint Pattern to construct a complete service for distributed exposure.

Enterprise Domain Repository should not be used to map several domain objects into a single domain object. A Aggregated Core Service is the apropiate solution for this kind of mapping.

### Forces

- Business definition of a Domain Object requires data from disparate systems
- Need for integrating multiple core systems cause high complexity
- Integrating directly from clients towards core systems reduces system evolvability
- Services exposed with higher granularity and larger responsibilities grow too complex over time

### Solution

The Enterprise Domain Repository main responsibility is to provide unified access to Domain Objects in the Enterprise. To achieve this the repository must maintain control of the objects and the providers that supply the data that constructs them. This implies that the Enterprise Domain Repository has to take some form of responsibility for correlation of providersystem identificators.

Another major responsibility is to take decisions on field mapping configuration between the providersystem representations of the data.

**Legend**

| Element | Responsibility | Details |
| --- | --- | --- |
| [EvolvingServiceEndpoint] | Representing the Domain Persistence Service | Uses the Enterprise Domain Respository |
| [RepositoryController] | Call providers, construct DomainObjects and manage Repository | The main public interface for the Enterprise Domain Repository |
| [Correlator] | Correlate the ProviderObjects for the RepositoryController and provide logical Ids | the implementation supplying Id correlation services to the Repository |
| [Repository] | Keep a store of DomainObjects as cache or efficient query store | May be implemented in memory or presistent |
| [ProviderController] | Keep track of registered controllers and execute cross-provider calls | Supports the Correlator and the RepositoryController |
| [Provider] | Encapsulate all complexity in calling the underlying system the provider represents | The provider representing a core system |
| [ProviderObject] | Expose relevant fields from the provider specific representations of data | The object containing Provider Specific data |
| [DomainObjectFactory] | Construct the domain object | Construct the domain object based on input from the Repository Controller |
| [DomainObject] | Expose the main DomainObject definition managed by the Enterprise Domain Respository |

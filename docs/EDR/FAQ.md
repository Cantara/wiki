# FAQ

- [How do you handle Partial Refresh of the Domain Object?](#FAQ-HowdoyouhandlePartialRefreshoftheDomainObject%3F)
- [Will EDR handle different versions of DomainObject](#FAQ-WillEDRhandledifferentversionsofDomainObject)
- [Strategies for data-mapping between ProviderObject´s and DomainObject´s.](#FAQ-StrategiesfordatamappingbetweenProviderObject%C2%B4sandDomainObject%C2%B4s.)
- [How do we handle correlation of Id´s?](#FAQ-HowdowehandlecorrelationofId%C2%B4s%3F)
- [How can we support get(id) in RepositoryController?](#FAQ-Howcanwesupportget%28id%29inRepositoryController%3F)
- [Can EDR only be used for Core Services?](#FAQ-CanEDRonlybeusedforCoreServices%3F)
- [Will EDR not easly break the Context-Mapping recommendations of Eric Evans?](#FAQ-WillEDRnoteaslybreaktheContextMappingrecommendationsofEricEvans%3F)
- [How does the Provider Controller support the Correlator?](#FAQ-HowdoestheProviderControllersupporttheCorrelator%3F)
- [Is it important that the Provider Object contains both correlated id, and the provider specific id?](#FAQ-IsitimportantthattheProviderObjectcontainsbothcorrelatedid%2Candtheproviderspecificid%3F)

### How do you handle Partial Refresh of the Domain Object?

Partial update of the domain object will occur eg. if one provider has a cache time-out of 2 minutes, while the other provider do not have a cache timeout at all. Handling this kind of challenges are regarded as an extension to EDR, and should receive special attention during implementation.

Strategies for Partial Update:

1. Handled by each Provider
   - The Provider must also handle cache.
   - You then need a discusion wether the provderd also will provide metadata describing the cache policy, to the EDR.
   - Provider might accept minimum and maximum values for aceptable cache timeout. This will give the Provider the possibility to throttle is own cache implementation.
2. Handled by [Provider Controller]
3. Handled by [Repository Controller]
   - Prefered strategy, if acheivable.
4. Do not support Partial Refresh at all.
   - Rebuild the full Domain Object if any part of the object is out-of-date.
5. Caching of Provider Objects, not the Domain Object.
   - Gives greater control, more flexibillity. The effect of EDR cache is reduced, due to need for creating new [DomainObject] for each request.
   - [DomainObjectFactory] need a functionality for controlling when parts of the Domain Object need refreshing. Information of when refresh is needed will need to come from the Provider, and from business rules within the Domain Object.
   - Proactive crawl of the Provider will keep the [ProviderObject] updated and valid.
   - Proactive indexing can also keep control regarding Event Driven Architecture. Events will only happen between the data source, and the provider.

|  | SLA/Governance must provide rules for how to handle Partial Refresh. |

### Will EDR handle different versions of DomainObject

Yes.

Handling different versions in the same runtime-environment is best handled by adding an Evolving Service Endpoint in front of the Repository Controller.

### Strategies for data-mapping between [ProviderObject]´s and [DomainObject]´s.

DataMapping is an [extension](/web/20210922183543/https://wiki.cantara.no/display/EDR/Extentions+-+Advanced+Scenarios "Extentions - Advanced Scenarios") to Enterprise Domain Repository pattern. We recommend that you implement [DataMapping](/web/20210922183543/https://wiki.cantara.no/display/EDR/Data+Mapping+Extension "Data Mapping Extension"), though.

See this page for more information on [Data Mapping](/web/20210922183543/https://wiki.cantara.no/display/EDR/Data+Mapping+Extension "Data Mapping Extension").

### How do we handle correlation of Id´s?

The Repository Controller must support ID correlation between Providers used by the EDR. This is vital in order to construct Domain Objects from multiple Provider Objects. The ID correlation mechanism may be an internal implementation or external package designed for this purpose.

|  | The main purpose of the Correlator is to handle mapping of the Id used in each Provider Object, and it´s corresponding Domain Object id. |

Strategies:  
#The correlator only knows the PO´s id for the domain objects that has been constructed by EDR.

- - Mapping an get(id) will not be possible, as the Correlator will not know the Id to be used for fetching data from an Provider.  
    #The correlator has mapping rules that know how data in one provider is corresponding to data in another provider. Eg. that both systems use the same custumer number. Another example will be the scenrio where retrieving data from one provider reveals the id to be used for retreiving data from another provider.

### How can we support get(id) in RepositoryController?

The correlator must contain information that enables mapping from the "id" to provider specific id´s. If this mapping is not possible, we will need to run an find() operation first.

### Can EDR only be used for Core Services?

Yes, EDR should only be used for a core service that handle one thing, and that thing well.

### Will EDR not easly break the Context-Mapping recommendations of Eric Evans?

Q: One of Eric Evans main thesis is that creating one unified domain-model, often is not an good idea. Creating a Context Map of the separate systems within a solution is an clever solution. The Context Map enables the separate domains to co-exist, independently of the other domains, within each domain context. Each domain model is then separated by an anti-corruption adapters.

Will the EDR pattern not enable (naive) developers to try to create an unified domain model, on top of other system, even if this is not always an good idea?

A: Evans is very clear in his recommendation of creating Bounded Contexts. A Bounded Context might be a full system, or a subsystem. Every Bounded Context has its own domain model, with clear boundaries for what functionality that is included within the context. Every Bounded Context should not contain larger parts of a system than a small team can develop, and maintain.

The Context Map describes how different Bounded Contexts relates to the other Bounded Contexts. Further Evans recommends that each Bounded Context will have its own set of services. These services that a Bounded Context offers relates to our Core Service. A service that consume functionality from other Core Services, is named Aggregated Core Service in our terminology.

EDR must be implemented as an Core Service, accessing data directly from different back-end systems. Though possible, you should not attemt to use EDR as an Aggregated Core Service, where an Domain Object will be build from other services.

EDR is an integrational pattern, where the goal is to build an Domain Object based on several data-sources. This Domain Object is served through a service. EDR must be defined within the boundaries of an Bouded Contex, with clear rules of what functionality is offered, and which functionality should not be offered.

What is then achieved is that several Domain Models (or Bounded Contexts), are able to access the same data efficiently.

As an EDR-service will stay within the borders of one Bounded Context, Eric Evan´s recommendations are not broken.

### How does the Provider Controller support the Correlator?

Basically we have only made one implementation of the correlator until August 2007. Our practical experience is somehow limited. The grand idea is that the correlator will detect if a set of Provider Objects has a logic relationship to each other.

If we try to explicitly define responsibilities, then the Provider Controller will be responsible for running actions accros providers, and then either:

1. Be responsible for using the correlator to "synchronize" the PO sets.
2. Let the Repository Controller use the Correlator for making decisions.

Our recommended strategy will most probably be selection 2. This is to ensure the Provider Controller is not overloaded by responsibilities.

### Is it important that the Provider Object contains both correlated id, and the provider specific id?

There are a few scenarios where you would choose to persist the correlator´s logic id in the data-source. The reason for this is to simplify correlation. Persisting the logical id should not be too controversial as this information will have a meaning for the reader of this information.

# Alignment of Enterprise Search Platforms (ESP) and Service-Oriented Architecture

### Intro

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| |  | Search is the realization of the fact that the world is not structured by design | | - Since the human brain does not work hierarchically, and a computer is faster to "remember" where data is stored, we need search-ability to retrieve stored data. - Search-Driven Architecture/Applications (SDA) provide push-events on change in stored data, which enable you to add alerts upon change on Business Objects (i.e. bad publicity in media on partner X) | |  | All attempts to manually categorize the world into structure is doomed to fail. Today - tomorrow - **always!** | |

### Types of search

- Traditional crawling
  - Web search
  - Enterprise/organizational search
  - Desktop search
- Search as BI data provider
  - Trend analysis
  - Knowledge management?
- Proactive search
  - "Deliver information you were not aware of, which give you a competitive edge"
  - Trend watching, benchmarking

# The place for Enterprise Search in Service-Oriented Architecture strategies.

|  | **Value proposition:** How to make your enterprise aware and responsive to unstructured data and real-time trends |

- In SOA we can use an enterprise search engine to structure unstructured data for our Business Objects
- A service can use the search-engine as a provider for rich domain objects. This is especially usefur for EDR, where we can use the search engine index to find the relevant data providers and correlating identifiers
- We can instruct the search engine to crawl the SOA services to provide:
  - The services will define the business entities, and will be welll-aligned with the business departments definitions
  - This will ensure that the search engine picks up semantic changes in the business domain, and avoid business definition duplication
  - Services should support this scenario (aggressive clients), and will have to implement throttle mechanisms or local caches to ensure SLA to all clients.
- To enforce correct ACL on services using a search index as data provider, we need to explicit filter returned data values, typically done through an AOP post-method data filter.

**Architecture with Business Intelligence in a Service-Oriented Architecture**

# Implementing Enterprise Search Platforms in your SOA

- Do not let yourself lead into a top-down analysis. Start simple (within a domain object) and expand as you learn. Stay true to the architecture axiom: Clear and consistent responsibilities powers all great architectures - and build your own great architecture.

### Technology and patterns

- FAST ESP and BI provides read-only entities, but lack the write/mastering aspect of EDR and EDR-MDS.
- In this SOA strategy, we can skip most of the indexing pipeline steps in Fast ESB, as we have already structured data from the service.

# Conclusion

Use an Agile approach. Start simple with simple queries and extend coordinated when need arise with simple applications and file structures. Think in terms of late binding with labels, tags, auto-taxonomies, contexts and rating.

[Metadata](/web/20201124114836/https://wiki.cantara.no/display/OWSOA/Metadata "Metadata")

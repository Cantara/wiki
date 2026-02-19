# Business Intelligence (BI) and Enterprise Search in a Service Oriented Architecture Strategy

## Executive Summary

Today, we are experience a heavy-weight fight to own the definition of the business objects within the enterprise. The contenders are Data warehouse products, Enterprise Search Platforms and Service Oriented Architecture strategies.

Solutions based upon enterprise search are closing in on the traditional Data warehouse value propositions. By promising "Real<sub>~Time Enterprise", platforms like [FAST ESP](http://www.fastsearch.com/thesolution.aspx?m=376) are targeting real</sub>~time Business Intelligence Audiences. 

This leads to a struggle over control of the organizations core definitions, and may lead to duplication and divergence between datawarhouse, search, portals and integration services. By defining forces that operate in the marked, and also strengths and weaknesses with the solution elements, can we create a responsibility sharing and usage plan. The goal is to use 

- The Search technologies efficient handling of unstructured data and _real-time_ capabilities
- The Datawarehouse technologies strength in tools support, handling of structured data, aggregation and preprocessing
- The uniform handling of integration and ownership to organizations core definitions through categorized services based on [OW SOA](OW-SOA.md)

Together this forms the base that secures maximum usage of the potential in the technology platform without unnecessary duplication and potential divergence between solution elements.

Attribution: This content is evolved from CC-licensed content from [wiki.community.objectware.no](http://wiki.community.objectware.no).

## Definitions

- [Data warehouse (DW)](Data<sub>~Warehouse</sub><sub>DW</sub><sub>and</sub><sub>Business</sub><sub>Intelligence</sub>~BI.md)
- [Business Intelligence](Data<sub>~Warehouse</sub><sub>DW</sub><sub>and</sub><sub>Business</sub><sub>Intelligence</sub>~BI.md)
- [Data Warehouse (DW) and Business Intelligence (BI)](Data<sub>~Warehouse</sub><sub>DW</sub><sub>and</sub><sub>Business</sub><sub>Intelligence</sub>~BI.md)
- [Search<sub>~driven Business Intelligence](Search</sub><sub>driven</sub><sub>Business</sub>~Intelligence.md)
- [Enterprise search](Alignment<sub>~of</sub><sub>Enterprise</sub><sub>Search</sub><sub>and</sub><sub>Service</sub>~orientation.md)
- [Metadata](Metadata.md)
- [OW SOA](OW-SOA.md)

## Alignment of Business Intelligence and Service Oriented Architecture

- [Alignment of Business Intelligence and Service Oriented Architecture](Alignment<sub>~of</sub><sub>Business</sub><sub>Intelligence</sub><sub>and</sub><sub>Service</sub>~Oriented-Architecture.md)

## Alignment of Enterprise Search and Service Oriented Architecture

- [Alignment of Enterprise Search and Service Oriented Architecture](Alignment<sub>~of</sub><sub>Enterprise</sub><sub>Search</sub><sub>Platforms</sub><sub>ESP</sub><sub>and</sub><sub>Service</sub>~Oriented-Architecture.md)

## Service Oriented Architecture with Enterprise Search and Business Intelligence

**Architecture and consistent responsibility division between [Data Warehouse (DW) and Business Intelligence (BI)](Data<sub>~Warehouse</sub><sub>DW</sub><sub>and</sub><sub>Business</sub><sub>Intelligence</sub><sub>BI.md), [Enterprise Search](Enterprise</sub><sub>Search.md) and [OW SOA](OW</sub>~SOA.md)**

![SOA<sub>~BI.jpg](SOA</sub><sub>BI</sub><sub>jpg.md)(SOA</sub>~BI.jpg)

## Case

## Conclusion

We have seen implementation of Business Intelligence that makes use of both traditional [Data Warehouse (DW) and Business Intelligence (BI)](Data<sub>~Warehouse</sub><sub>DW</sub><sub>and</sub><sub>Business</sub><sub>Intelligence</sub><sub>BI.md)  and newer trends in [Search</sub><sub>driven Business Intelligence](Search</sub><sub>driven</sub><sub>Business</sub>~Intelligence.md). The technologies are complementary and can draw on each other strengths given that their responsibility is clearly defined and this is reflected in their usage. [OW SOA](OW-SOA.md) helps [Governance](Governance.md) the process by setting this responsibility through [Policy](Policy.md) and drivers for this kind of technology in the categorized service model. 

Services implemented based on [OW SOA](OW<sub>~SOA.md) is very beneficial for [Data Warehouse (DW) and Business Intelligence (BI)](Data</sub><sub>Warehouse</sub><sub>DW</sub><sub>and</sub><sub>Business</sub><sub>Intelligence</sub><sub>BI.md) because the Core Services take responsibility for Extract and Transform of data. This reduces the complexity in practical implementation of [Data Warehouse (DW) and Business Intelligence (BI)](Data</sub><sub>Warehouse</sub><sub>DW</sub><sub>and</sub><sub>Business</sub>~Intelligence-BI.md) and make sure that correlation and establishment of core definitions only occurs in one place in the solution architecture.

[OW SOA](OW-SOA.md) Core Services support Enterprise Search by offering one source for master data pr. core definition. This gives Enterprise Search platforms a valuable reference base for indexing and potentially easier Entity Extraction from unstructured information.

> 💡 In our opinion Business Intelligence today needs **both** search technologies (for unstructured information and _realtime_ data) **and** datawarehouse technology (for structured information).  

### Links

- [FAQ - BI og Enterprise Search in a Service Oriented Architecture](FAQ<sub>~BI</sub><sub>og</sub><sub>Enterprise</sub><sub>Search</sub><sub>in</sub><sub>a</sub><sub>Service</sub>~Oriented-Architecture.md)

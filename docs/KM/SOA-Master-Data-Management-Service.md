# SOA Master Data Management Service

Attribution: This work started on [wiki.community.objectware.no](http://wiki.community.objectware.no)

# EDR-MDS a SOA Master Data Management Service

> ℹ️ To allow standard software to coexist nicely with SOA and to reach SOA Maturity Level 2, we need to master our Business Objects.‏ EDR is the natural, lean, simple and inexpensive choice for a Master Data Management Services.
> ℹ️ 
> ℹ️ * Simplest possible route to managed data
> ℹ️ * Reduced complexity by zooming in to one single Business Object at a time
> ℹ️ * All non-business object relations handled as resource references.
> ℹ️ * Simple first generation implementation within 2-3 months
> ℹ️ * By adding support for managed Business Objects in your SOA,  you facilitate and enable event<sub>~driven architectures and real</sub>~  time enterprise.

## Intro

Service Oriented Architecture is all over us. There seems to be some kind of consensus that one type of SOA services are services that are responsible for the core business objects - and vendors are monitoring and releasing their SOA Data Server products to close the gap. By pioneering the SOA space with EDR, we have gained lots of valuable of experiences of how to solve the Master Data challenges in SOA.

### The problem

- Companies don't have a precise view about their data
- Ownership of data is unclear. Reorganizations and consolidations may obscure ownership.
- Organizations are not static. More data, overlapping with other data, is added thorugh mergers
- Projects define data reconciliation outside project scope
- Developers do not care about data
- Vendors always try to solve to much at once
- The data warehouse guys have beards and funny accents

NB. The problems description needs major rework - most people does not get the message.  possibly by using some example cases..

### The vision

To solve the data problems in the simplest and most flexible way and at the same time provide a solid building block on the way to enable the **[Real Time Enterprise](Real<sub>~Time</sub><sub>Enterprise.md)** vision for a service</sub><sub>oriented **[System Strategy](System</sub><sub>Strategy.md)**. EDR</sub><sub>MDS is primed to be the best strategy to move to SOA Maturity Level 2. ([SOA Maturity Models and EDR</sub><sub>MDS](SOA</sub><sub>Maturity</sub><sub>Models</sub><sub>and</sub>~EDR-MDS.md))

### EDR-MDS

To allow standard software to coexist nicely with SOA, we need to master our disjoint Business Objects (EDR sources)‏ EDR is the natural, simple and inexpensive choice for a Master Strategy for Business Objects.

**Highlights**
- Field/value based mastering (dynamic readable rules(DSL))‏
- Auto<sub>~update/write</sub>~back to all involved parties (using the standard provider)‏
- Out-of bounds mastering/overwrite to leverage the most of all applications
- Out<sub>~of</sub>~bounds triggers for each provider

**Backbones**
- JavaSpace (Blitz)
- EDA/Eventing
- Federated backbones
- Distributed cache

**Tooling**
- JMatter Domain Object Management Client

### Mastering with EDR

Initial discussions identified some core concepts related to mastering strategies. These concepts requires definitions in this context:

    * Master
    * Synchronization
    * Mapping
    * Complex Validation

All mastering strategies are primarily focused towards categorized Core Services implementing Enterprise Domain Repository and utilizing multiple providers.

### Key takeaways

- Simplest possible route to managed data
- Reduced complexity by zooming in to one single Business Object at a time
- All non-business object relations handled as resource references.
- Simple first generation implementation within 2-3 months
- By adding support for managed Business Objects in your SOA,  you facilitate and enable event<sub>~driven architectures and real</sub>~  time enterprise.
- [Value Delivered - Business Cases](Value<sub>~Delivered</sub>~Business-Cases.md)

> ℹ️ EDR-MDS is just **good old common sense** 
> ℹ️ * EDR-MDS can be implemented in your favorite technology, container, product or programming language. 

### Quick links

- [Value Delivered - Business Cases](Value<sub>~Delivered</sub>~Business-Cases.md)
- [SOA Maturity Models and EDR<sub>~MDS](SOA</sub><sub>Maturity</sub><sub>Models</sub><sub>and</sub><sub>EDR</sub>~MDS.md)
- [SOA Hype Chart](SOA<sub>~Hype</sub>~Chart.md)
- [Laws of SOA](Laws<sub>~of</sub>~SOA.md)

![OW<sub>~EDR</sub><sub>Master</sub><sub>Strategy</sub><sub>5</sub><sub>with</sub><sub>text.jpg](OW</sub><sub>EDR</sub><sub>Master</sub><sub>Strategy</sub><sub>5</sub><sub>with</sub><sub>text</sub><sub>jpg.md)(OW</sub><sub>EDR</sub><sub>Master</sub><sub>Strategy</sub><sub>5</sub>~with-text.jpg)
---

{contributors-summary:order=edits|limit=23|childrenshow|Anonymous=true}

---

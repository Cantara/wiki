# Enterprise Domain Repository - Home

.  
.

# Enterprise Domain Repository - handle multi-source DomainObjects

|  |  |
| --- | --- |
| Enterprise Domain Repository (EDR) is a *pattern* for ensuring you are in control when handling Domain Objects containing data from multiple back-ends.  Most enterprises have several systems which own parts of a domain object.The data from these systems might be disjoint, as well as overlapping. The data quality and SLA requirements for each system are often of diversified quality. We need a standardized way to handle multi-source domain objects, and to extend the Domain repository to handle the real-world CRUD of today's enterprises.  The work on this pattern summarize experiences gained in real-life projects on both [.Net] and [Java]. |  |

---

### EDR Technology section

- [EDR - The details](/web/20230928120224/https://wiki.cantara.no/display/EDR/EDR+-+The+details "EDR - The details")
- [EDR - Pattern diagram](/web/20230928120224/https://wiki.cantara.no/display/EDR/EDR+-+Pattern+diagram "EDR - Pattern diagram")

|  |  |
| --- | --- |
| The Java implementation(s).  - [[Java Implementation Details]]  EDR on dev.java.net  - [EDR](https://edr.dev.java.net/) - [Join](https://edr.dev.java.net/servlets/ProjectMemberList) - [Browse SVN](https://edr.dev.java.net/source/browse/edr/)  EDR implemented as a Composite Object Programming multi backend EntityStore  - [Qi4j EDR implementation](/web/20230928120224/https://wiki.cantara.no/display/EDR/Qi4j+EDR+implementation "Qi4j EDR implementation") | The .net/C# implementation.  - [.Net (C#)]  The .Net examples will be made publicly available later. |

---

### Presentations

- [JavaZone 2007](http://www4.java.no/presentations/javazone/2007/slides/5344.pdf)
- [Community Corner at JavaOne 2008](/web/20230928120224/https://wiki.cantara.no/download/attachments/6815745/EDR-JavaOne-08.pdf?version=1&modificationDate=1213268464800)
- [EDR as Integration Strategy at Communities in Action 2010 (Norwegian)](/web/20230928120224/https://wiki.cantara.no/download/attachments/6815745/EDR_as_Integration_Strategy_at_CiA2010.pdf?version=1&modificationDate=1273585272506)

---

### Data Master Strategy

One of the advantages using EDR is the possibility of discovering, and automatically resolve, data inconsistency between different back-end systems.

One example is that the same customer has different street address in your billing and CMS applications.

This strategy is further examined in [**EDR-MDS**](http://wiki.community.objectware.no/display/EDRMDS/EDR-MDS+a+SOA+Master+Data+Management+Service).

### EDR data inconsistency between different back-end systems.

One example is that the same customer has different street address in your billing and CMS applications.

### Extensions / Advanced Scenarios

The [Recording Command Pattern](/web/20230928120224/https://wiki.cantara.no/display/EDR/Recording+Command+Pattern "Recording Command Pattern") may be used to extend the Providers used by the Enterprise Domain Respository. A Recording Gateway will keep track of all executed commands and record all responses to these requests. This enables the gateway to go into offline mode and do playback of the traffic should the provided system be unavailable.

[Merge Strategy Pattern](/web/20230928120224/https://wiki.cantara.no/display/EDR/Merge+Strategy+Pattern "Merge Strategy Pattern")  
[Merge Timing Pattern]  
[Open-ended Integration Merge Pattern](/web/20230928120224/https://wiki.cantara.no/display/EDR/Open-ended+Integration+Merge+Pattern "Open-ended Integration Merge Pattern")  
[Data Mapping in EDR](/web/20230928120224/https://wiki.cantara.no/display/EDR/Data+Mapping+in+EDR "Data Mapping in EDR")  
[EDR and very complex domain objects] How to handle domain objects that might span multiple Bounded Contexts

### Reference Implementation

[EDR Reference Implementation]  
[Moderator Discussion](/web/20230928120224/https://wiki.cantara.no/display/EDR/EDR+-+Moderator "EDR - Moderator")

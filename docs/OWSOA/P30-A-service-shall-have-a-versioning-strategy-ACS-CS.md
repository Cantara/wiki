# P30. A service shall have a versioning strategy (ACS, CS)

### Motivation

When a service-consumer starts using a service, a dependency to that service's contract is created. The service's contract can't undergo any major changes without this having an impact on the service-consumer. This introduces the need for several versions of a service.

### Argumentation

Services evolve over time. Service consumers need to know how the services evolve to be able to evolve alongside the service-lifecycle. The versioning life-cycle need to be predictable for the service-consumers, so that they can plan ahead for new versions of a service. Therefore any service must have a documented versioning strategy, so that consumers can plan their update strategy in accordance.

The versioning strategy and policies should be a part of a service's Service Level Agreement. See: [P32. A service shall document its Service Level Agreement SLA (response time=30ms, availability=99.995%)](/web/20220817073517/https://wiki.cantara.no/pages/viewpage.action?pageId=3146064 "P32. A service shall document its Service Level Agreement SLA (response time=30ms, availability=99.995%)")

### Exceptions/special cases

In most real cases, this policy will be limiting to a small set of versioning strategies (multiple endpoints, evolving service adaptor, adaptors, forced big-bang (really the worst versioning strategy..) et all..).

### Definitions

### Status

| Doc status | [H2A](/web/20220817073517/https://wiki.cantara.no/display/OWSOA/H2A "H2A") | [A2A](/web/20220817073517/https://wiki.cantara.no/display/OWSOA/A2A "A2A") | [ACS](/web/20220817073517/https://wiki.cantara.no/display/OWSOA/ACS "ACS") | [CS](/web/20220817073517/https://wiki.cantara.no/display/OWSOA/CS "CS") | Last [PAB](/web/20220817073517/https://wiki.cantara.no/display/OWSOA/PAB "PAB") discussion |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | 2007.06.08 |

---

### PAB discussions

---

### [Design-Time Governance - SOA Design Rules FAQ](/web/20220817073517/https://wiki.cantara.no/display/OWSOA/Design-Time+Governance+-+SOA+Design+Rules+FAQ "Design-Time Governance - SOA Design Rules FAQ")

- [Question still to be asked..]

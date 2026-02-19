# P41. A service shall provide heartbeat and traffic monitoring

### Motivation

A heartbeat is necessary to be able pro actively react when a service is not responding according to SLA

We want to keep track of the following:

- Does the service provide business value?
- Is the service functioning according to its SLA
- Where is a service-composition failing

### Argumentation

- Monitor and understand which services are used, and how many times they are used.
- Understand which services are candidates for change orders
  - if a service is unused, it does not provide value to its owners/users
- Locate services to be terminated
- A heartbeat is necessary to be able pro actively react when a service is not responding according to SLA
  - This monitoring can will tell you which service(s) are not working
  - A heartbeat is proof of SLA conformance/non-conformance

### Exceptions/special cases

### Definitions

See: [P32. A service shall document its Service Level Agreement SLA (response time=30ms, availability=99.995%)](/web/20220817062727/https://wiki.cantara.no/pages/viewpage.action?pageId=3146064 "P32. A service shall document its Service Level Agreement SLA (response time=30ms, availability=99.995%)")

### Status

| Doc status | [H2A](/web/20220817062727/https://wiki.cantara.no/display/OWSOA/H2A "H2A") | [A2A](/web/20220817062727/https://wiki.cantara.no/display/OWSOA/A2A "A2A") | [ACS](/web/20220817062727/https://wiki.cantara.no/display/OWSOA/ACS "ACS") | [CS](/web/20220817062727/https://wiki.cantara.no/display/OWSOA/CS "CS") | Last [PAB](/web/20220817062727/https://wiki.cantara.no/display/OWSOA/PAB "PAB") discussion |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | 2007.06.08 |

---

### PAB discussions

---

### [Design-Time Governance - SOA Design Rules FAQ](/web/20220817062727/https://wiki.cantara.no/display/OWSOA/Design-Time+Governance+-+SOA+Design+Rules+FAQ "Design-Time Governance - SOA Design Rules FAQ")

- [Question still to be asked..]

# P4. A H2A service (webpart or portlet) shall be an independent component

### Motivation

We want the H2A services to be reusable building blocks.

### Argumentation

WebParts and portlets shall be self-contained components to be conform to the specification and to be reusable in different scenarios and contexts. It is also very important to be able to automatically test the service in isolation, which is almost impossible if you break this rule.

### Exceptions/special cases

---

### Definitions

### Status

| Doc status | [H2A](/web/20220817070949/https://wiki.cantara.no/display/OWSOA/H2A "H2A") | [A2A](/web/20220817070949/https://wiki.cantara.no/display/OWSOA/A2A "A2A") | [ACS](/web/20220817070949/https://wiki.cantara.no/display/OWSOA/ACS "ACS") | [CS](/web/20220817070949/https://wiki.cantara.no/display/OWSOA/CS "CS") | Last [PAB](/web/20220817070949/https://wiki.cantara.no/display/OWSOA/PAB "PAB") Discusion |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | 2007.06.08 |

---

### PAB discussions

It is OK to create (Web) Applications on top of a SOA, these applications may choose to use H2A services ot to call directly services in other categories. It is important to separate applications and H2A services.

---

### [Design-Time Governance - SOA Design Rules FAQ](/web/20220817070949/https://wiki.cantara.no/display/OWSOA/Design-Time+Governance+-+SOA+Design+Rules+FAQ "Design-Time Governance - SOA Design Rules FAQ")

- [Question still to be asked..]

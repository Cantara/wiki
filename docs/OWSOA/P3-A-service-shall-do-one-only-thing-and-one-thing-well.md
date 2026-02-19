# P3. A service shall do one only thing, and one thing well

### Motivation

We want to prevent service rot, duplication and loose coupled services, in other words **good building blocks**

### Argumentation

If a service does more than one thing, it will likely not do everything well. **The success ratio of a service correlates nicely with the characteristics of reusable code**, namely code which does one thing, and one thing well

Use the service layers to decompose the service and place the parts into the correct layers: see [The Laws of SOA](/web/20220817082617/https://wiki.cantara.no/display/OWSOA/The+Laws+of+SOA "The Laws of SOA") paragraph 2.

### Exceptions/special cases

Typical misunderstood attempt on an exception:

> In some cases you may have to violate this principle for performance reason.

However, the service is probably designed incorrect if this is the case.

Arguments:

- If you violate this rule, your service will not be re-usable
- If you violate this rule, your service will duplicate business logic and will be life-cycle dependent on all the services which share data and behavior
- Exposed data from such services will be incompatible with data from all other services
- The quick-win scalability argument is better solved with collaborating instances of data-providing services (shared state backbones, eventing backbones and similar state-sharing techniques)
- See Service governance quiz for detailed discussion.

---

### Definitions

### Status

| Doc status | [H2A](/web/20220817082617/https://wiki.cantara.no/display/OWSOA/H2A "H2A") | [A2A](/web/20220817082617/https://wiki.cantara.no/display/OWSOA/A2A "A2A") | [ACS](/web/20220817082617/https://wiki.cantara.no/display/OWSOA/ACS "ACS") | [CS](/web/20220817082617/https://wiki.cantara.no/display/OWSOA/CS "CS") | Last [PAB](/web/20220817082617/https://wiki.cantara.no/display/OWSOA/PAB "PAB") discussion |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | 2007.06.08 |

---

### PAB discussions

Can a H2A service to too little? We should add a new checklist item which ensures that we provide enough business value..

---

### [Design-Time Governance - SOA Design Rules FAQ](/web/20220817082617/https://wiki.cantara.no/display/OWSOA/Design-Time+Governance+-+SOA+Design+Rules+FAQ "Design-Time Governance - SOA Design Rules FAQ")

- [Question still to be asked..]

# P6. A H2A service shall not have internal workflow

### Motivation

H2A services are pieces. If the pieces includes a lot of internal workflow, they will loose their abillity for reuse, and are in all practical terms not services but applications.

### Argumentation

We create a conflict of responsibility between services when the services start manipulating other services state, which leads to tight coupling between services and recursion conflicts called deadlocks

This rule efficiently separates H2A services and H2A applications/mashups.

### Exceptions/special cases

- GUI-flow/Wizards

---

### Definitions

Workflow is defined to have the following characteristics:

- At least 2 actors
- Often consists of long running transactions

Non workflow examples

- GUI-flow/Wizards

In doubt cases:

- machine actors have to be **external** (asyn, remote)

Argumentation: normally, we define workflow as a flow between at least two **human** actors. This definition looses meaning as soon as we start to automate some of the human actors. This mean that without our definition, we can have a change of operation/rules to our services invoked on our service run-time, without our knowledge, which does not make much sense..

### Status

| Doc status | [H2A](/web/20220817074243/https://wiki.cantara.no/display/OWSOA/H2A "H2A") | [A2A](/web/20220817074243/https://wiki.cantara.no/display/OWSOA/A2A "A2A") | [ACS](/web/20220817074243/https://wiki.cantara.no/display/OWSOA/ACS "ACS") | [CS](/web/20220817074243/https://wiki.cantara.no/display/OWSOA/CS "CS") | Last [PAB](/web/20220817074243/https://wiki.cantara.no/display/OWSOA/PAB "PAB") discussion |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | 2007.06.08 |

---

### PAB discussions

---

### [Design-Time Governance - SOA Design Rules FAQ](/web/20220817074243/https://wiki.cantara.no/display/OWSOA/Design-Time+Governance+-+SOA+Design+Rules+FAQ "Design-Time Governance - SOA Design Rules FAQ")

- [Question still to be asked..]

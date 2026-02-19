# P42. A Core service shall have orthogonal functionality

### Motivation

Service behavior should be predictable and not produce bi-effects in other services

### Argumentation

- Ensure that a services does its thing and not everything else..
- Improved evolve ability of the service, as the impacts of change is understood.

### Exceptions/special cases

### Definitions

|  | If(!totto) Orthogonality guarantees that modifying the technical effect produced by a component of a system neither creates nor propagates side effects to other components of the system. The emergent behavior of a system consisting of components should be controlled strictly by formal definitions of its logic and not by side effects resulting from poor integration, i.e. non-orthogonal design of modules and interfaces. Orthogonality reduces testing and development time because it is easier to verify designs that neither cause side effects nor depend on them. |

### Status

| Doc status | [H2A](/web/20210621072644/https://wiki.cantara.no/display/KM/H2A "H2A") | [A2A](/web/20210621072644/https://wiki.cantara.no/display/KM/A2A "A2A") | [ACS](/web/20210621072644/https://wiki.cantara.no/display/KM/ACS "ACS") | [CS](/web/20210621072644/https://wiki.cantara.no/display/KM/CS "CS") | Last [PAB](/web/20210621072644/https://wiki.cantara.no/display/KM/PAB "PAB") discussion |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | 2007.06.08 |

---

### PAB discussions

---

### [Design-Time Governance - SOA Design Rules FAQ](/web/20210621072644/https://wiki.cantara.no/display/KM/Design-Time+Governance+-+SOA+Design+Rules+FAQ "Design-Time Governance - SOA Design Rules FAQ")

- [Question still to be asked..]

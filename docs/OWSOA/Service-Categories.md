# Service Categories

### SOA Service Categories

| [Human to Application](/web/20220811084522/https://wiki.cantara.no/display/OWSOA/H2A "H2A") | [Application to Application](/web/20220811084522/https://wiki.cantara.no/display/OWSOA/A2A "A2A") | [Aggregated Core Services](/web/20220811084522/https://wiki.cantara.no/display/OWSOA/ACS "ACS") | [Core Services](/web/20220811084522/https://wiki.cantara.no/display/OWSOA/CS "CS") |
| --- | --- | --- | --- |

### Human to Application (H2A)

[H2A](/web/20220811084522/https://wiki.cantara.no/display/OWSOA/H2A "H2A") Services is services involving key user interaction components with one or more humans to fulfill some activity/workflow. For example a booking process or a manual shipment process.

A H2A service is an implementation of a use-case/user story which implements one, and only one human actor

### Application to Application (A2A)

[A2A](/web/20220811084522/https://wiki.cantara.no/display/OWSOA/A2A "A2A") Services is services which orchestrates services from several applications, typically asynchronous and workflow-backed. I.e. a Auction type request against a set of suppliers or an booking/order/delivery process.

An A2A service is a service which is responsible for collaboration between several human or automated actors.

### Aggregated Core Services (ACS)

[ACS](/web/20220811084522/https://wiki.cantara.no/display/OWSOA/ACS "ACS") is extensions to Core Services. ACS is usually either context-specializing (CustomerCustomer and VendorCustomer) or aggregations from several Core Services like in CustomerDashboard which aggregates from Customer Service, Order Service and possibly more services.

### Core Services (CS)

[CS](/web/20220811084522/https://wiki.cantara.no/display/OWSOA/CS "CS") is basically data services. Typically they evolve to become the master repository for the most important business objects in the enterprise. Typical examples are Customer and Product. You will also fint that it often makes sense to split a service for a domain object into a CRUD (master) service and a accompanying Query Service to keep the complexity to a managable level, and to allow a more feature rick query interface.

### Examples

- [BankServiceUniverse] is a banking example, with vertical function segmentation extensions
- [Data Processing](/web/20220811084522/https://wiki.cantara.no/display/OWSOA/Data+Processing "Data Processing")

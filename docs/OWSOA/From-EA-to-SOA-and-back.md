# From EA to SOA (and back)

Enterprise Architecture is a non-mandatory complementary technique to SOA. A Service Oriented system architecture can be aligned with various Enterprise Architecture frameworks and will usually provide strategies around data management, integration, process orchestration etc.

EA will give several inputs to defining your service universe:

- Process-view
  - The bottom-level processes will provide value-chain models, where the involved parties can be typed into a service-role/interface-role which is great candidates to SOA services
  - The activities are candidates for services. The data-elements are candidate for Core Services (Data Repository Services)
- Data-view
  - The conceptual information artifacts breaks down to Business Objects from the "district/block/building/"-context from the system view. The conceptual information artifacts and business objects are key suspects to Core Repository Services. (And possibly extended to Context-specialization as Aggregated Core Services)
- System View.
  - Analysis of the part a system plays in different rooms in the system models are key candidates to A2A services (workflow/process/orchestration services)

### Service types and technology

- [Human to Application Services](/web/20201025053033/https://wiki.cantara.no/display/OWSOA/H2A "H2A")
- [Application to Application Services](/web/20201025053033/https://wiki.cantara.no/display/OWSOA/A2A "A2A")
- [Aggregated Core Services](/web/20201025053033/https://wiki.cantara.no/display/OWSOA/ACS "ACS")
- [Core Services](/web/20201025053033/https://wiki.cantara.no/display/OWSOA/CS "CS")

### Design rules

- [Design-Time Governance - SOA Design Rules](/web/20201025053033/https://wiki.cantara.no/display/OWSOA/Design-Time+Governance+-+SOA+Design+Rules "Design-Time Governance - SOA Design Rules")

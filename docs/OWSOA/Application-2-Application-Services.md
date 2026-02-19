# Application 2 Application Services

### Application 2 Application Services

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| |  | **Application 2 Application Services** Application 2 Application Services is services which orchestrates services from several applications, typically asynchronous and workflow-backed. I.e. a Auction type request against a set of suppliers or an booking/order/delivery process. |  |  | **Suggestion for a more presise definition** An A2A service is a service which is responsible for collaboration between several human or automated actors. | |  |

|  |  |  |  |
| --- | --- | --- | --- |
| Characteristics Two types:  **Process Services**   - Services orchestrated to produce real business value - Workflow-oriented processes - Orchestrated functionality from several services - ACS/CS services as Business/Domain Objects - External applications for sub-processes & tasks - Long running processes - Should not have any long-running transactions - Could (should) have cache (state full)   **Application Integration Service Endpoints**   - Services which integrate and map against external application endpoints - Should (internally) provide for SLA and contractual requirements (via cache, rebind, fail-over and such) - Works as an external data anti-corruption layer for external application endpoints to reduce dependencies and facilitate evolve ability  Patterns for Application 2 Application Services  ---   |  | **Application 2 Application Services** | | Technology/Implementation strategy (Java) **Technology, implementation and products**   - Pick your favorite JEE/ESB/SOA platform vendor   - Sun, IBM, Oracle - Choose your favorite open source ESB/SOA platform   - OpenESB or another Open Source JBI container   - write a simple admin framework (upgrade tool support)  Technology/Implementation strategy (.NET) **Technology, implementation and products**   - BizTalk Server - Enterprise Human Workflow products can do some tasks   - Enterprise Human Workflow with K2.NET / Skelta/ Captaris++   - Portal connectors useful |

### Design rules

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [P1. A service shall have one named owner](/web/20210126124810/https://wiki.cantara.no/display/OWSOA/P1.+A+service+shall+have+one+named+owner) | [P2. A service shall provide documented business value](/web/20210126124810/https://wiki.cantara.no/display/OWSOA/P2.+A+service+shall+provide+documented+business+value) | [P20. All services shall be in the service universe](/web/20210126124810/https://wiki.cantara.no/display/OWSOA/P20.+All+services+shall+be+in+the+service+universe) | [P21. A service shall be categorized (OW SOA category)](/web/20210126124810/https://wiki.cantara.no/display/OWSOA/P21.+A+service+shall+be+categorized+%28OW+SOA+category%29) | [P22. A service shall have an "authentication, authorisation, endpoint strategy"](/web/20210126124810/https://wiki.cantara.no/pages/viewpage.action?pageId=8486983) |
| [P23. A service shall document its Service Level Agreement SLA (response time, availabillity++)](/web/20210126124810/https://wiki.cantara.no/pages/viewpage.action?pageId=8486984) | [P3. A service shall do one only thing, and one thing well](/web/20210126124810/https://wiki.cantara.no/display/OWSOA/P3.+A+service+shall+do+one+only+thing%2C+and+one+thing+well) | [P30. A service shall have a versioning strategy (ACS, CS)](/web/20210126124810/https://wiki.cantara.no/display/KM/P30.+A+service+shall+have+a+versioning+strategy+%28ACS%2C+CS%29) | [P31. A service shall provide for audit and monitoring of service usage](/web/20210126124810/https://wiki.cantara.no/display/KM/P31.+A+service+shall+provide+for+audit+and+monitoring+of+service+usage) | [P31. A service shall provide for audit and monitoring of service usage](/web/20210126124810/https://wiki.cantara.no/display/OWSOA/P31.+A+service+shall+provide+for+audit+and+monitoring+of+service+usage) |
| [P41. A service shall provide heartbeat and traffic monitoring](/web/20210126124810/https://wiki.cantara.no/display/OWSOA/P41.+A+service+shall+provide+heartbeat+and+traffic+monitoring) | [P90. A service shall have a documented coupling to the contractual and requirement for service usage](/web/20210126124810/https://wiki.cantara.no/display/OWSOA/P90.+A+service+shall+have+a+documented+coupling+to+the+contractual+and+requirement+for+service+usage) |

- [Policy Rules for A2A services](/web/20210126124810/https://wiki.cantara.no/display/OWSOA/Design-Time+Governance+for+A2A+Services "Design-Time Governance for A2A Services")

---

### Other technical details

# Human 2 Application Services

### Human 2 Application Services

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| |  | **Human 2 Application Services** Human 2 Application Services is services involving key user interaction components with one or more humans to fulfill some activity/workflow. For example a booking process or a manual shipment process, |  |  | **Suggestion for a more precise definition** A H2A service is an implementation of a use-case/user story  - which implements one, and only one human actor | |  |

|  |  |  |  |
| --- | --- | --- | --- |
| Characteristics Workflow-oriented Services which require human interaction   - Long running transactions - Most services start as H2A Services - Automated on a ROI basis - Non-trivial decisions points that require 'human touch' - Starting-point/front-end of externalized processes  Patterns for Human 2 Application Services  ---   |  | **Human 2 Application Services** | | Technology/Implementation strategy (Java) **Technology, Implementation and products**   - Buy specialized product if close match to requirements   - (K2.NET)-alike products - Build portal upon best-of breed (JSR 168/286)   - SiteVision, Vertical Site, CorePortal (Norwegian CMS and JSR 168 products)  Technology/Implementation strategy (.NET) **Technology, Implementation and products**   - Windows Forms - Microsoft Office (as smart client) - Pure ASP.NET - MOSS (Sharepoint platform) incl. Sharepoint Designer for H2A workflow - Enterprise Human Workflow with K2.NET / Skelta/ Captaris++ - Portal connectors useful |

### Design rules

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [P1. A service shall have one named owner](/web/20210126123344/https://wiki.cantara.no/display/OWSOA/P1.+A+service+shall+have+one+named+owner) | [P2. A service shall provide documented business value](/web/20210126123344/https://wiki.cantara.no/display/OWSOA/P2.+A+service+shall+provide+documented+business+value) | [P21. A service shall be categorized (OW SOA category)](/web/20210126123344/https://wiki.cantara.no/display/OWSOA/P21.+A+service+shall+be+categorized+%28OW+SOA+category%29) | [P3. A service shall do one only thing, and one thing well](/web/20210126123344/https://wiki.cantara.no/display/OWSOA/P3.+A+service+shall+do+one+only+thing%2C+and+one+thing+well) | [P4. A H2A service (webpart or portlet) shall be an independent component](/web/20210126123344/https://wiki.cantara.no/display/OWSOA/P4.+A+H2A+service+%28webpart+or+portlet%29+shall+be+an+independent+component) |
| [P41. A service shall provide heartbeat and traffic monitoring](/web/20210126123344/https://wiki.cantara.no/display/OWSOA/P41.+A+service+shall+provide+heartbeat+and+traffic+monitoring) | [P5. A H2A Service (webpart or portlet) shall be a part of a bigger whole, not trying to dictate other H2A services](/web/20210126123344/https://wiki.cantara.no/display/OWSOA/P5.+A+H2A+Service+%28webpart+or+portlet%29+shall+be+a+part+of+a+bigger+whole%2C+not+trying+to+dictate+other+H2A+services) | [P6. A H2A service shall not have internal workflow](/web/20210126123344/https://wiki.cantara.no/display/OWSOA/P6.+A+H2A+service+shall+not+have+internal+workflow) | [P7. Too generic webparts or portlets shall be avoided](/web/20210126123344/https://wiki.cantara.no/display/OWSOA/P7.+Too+generic+webparts+or+portlets+shall+be+avoided) | [P90. A service shall have a documented coupling to the contractual and requirement for service usage](/web/20210126123344/https://wiki.cantara.no/display/OWSOA/P90.+A+service+shall+have+a+documented+coupling+to+the+contractual+and+requirement+for+service+usage) |

- [Policy rules for H2A services](/web/20210126123344/https://wiki.cantara.no/display/OWSOA/Design-Time+Governance+for+H2A+Services "Design-Time Governance for H2A Services")
- [The most common errors in portal projects](/web/20210126123344/https://wiki.cantara.no/display/OWSOA/The+most+common+portal+project+mistakes "The most common portal project mistakes")

---

### Other technical details

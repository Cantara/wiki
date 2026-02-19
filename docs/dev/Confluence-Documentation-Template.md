# Confluence Documentation Template

Draft quality!

This template is based on the [4 plus 1 View Model](4<sub>~plus</sub><sub>1</sub><sub>View</sub>~Model.md). This is a work in progress and the template is not as a silver-bullet, but as a starting point when documenting a system using Confluence wiki. 

- **System Architecture**
    - Logical View
    - Physical View 
    - Process View
    - Scenario View

- Subsystem **design descriptions**
    - Reading guide
    - Subsystem1
        - Subsystem1 Description 
        - Subsystem1 Installation Guide 
        - Subsystem1 Operation Manual 
            - Configuration
            - Start and stop
            - Logging
        - Subsystem1 Design Description 
    - Subsystem2
        - Subsystem2 Description
        - Subsystem2 Installation Guide
        - Subsystem2 Operation Manual
        - Subsystem2 Design Description

- System Design Principles - principles and decisions common for the entire system
    - Integration documents
    - Logging
    - Monitoring
    - Exception Management
    - Core Domain Model

- Technologies - which technologies are used

- Administration tools
    - Monitoring

- Support 
    - Issue tracker 
    - Contact information for tech lead for each subsystem

- Glossary and Abbreviations

---
## How to interpret the template 

The [4 plus 1 View Model](4<sub>~plus</sub><sub>1</sub><sub>View</sub>~Model.md) is designed for documenting the software _architecture_ of an _application_. When documenting a _system_ or a _system_of_systems_ multi-level documentation it is necessary. However, the remember the golden rule _[Working software over comprehensive documentation](http://agilemanifesto.org/)_ . Applied to the 4+1 view model this means that any views not relevant should be omitted. This also means that diagrams nobody has requested should not be included in the documentation just because myGreatArchitectToolkit can automatically generate them. 

**Q**: Multi-level is one thing, but how about architecture versus design? 
**A**: We have chosen to focus on the system **architecture** and only architecture for the system as a whole and focus on **design** when documenting each application. 

**Q**: Is Core Domain Model architecture or design? 
**A**: At logical/physical level it is design, but on semantical/conceptual level it is architecture. 

**Q**: Which tools can I use to draw my diagrams? 
**A**: See [Diagram Software](Diagram-Software.md).  

#### Software architecture

The purpose of architecture documentation is to emphasize **responsibility** and what measures have been taken to reduce complexity. Like for example architecture axioms [architecture:Clear and consistent responsibility power all great architectures](../architecture/Clear<sub>~and</sub><sub>consistent</sub><sub>responsibility</sub><sub>power</sub><sub>all</sub><sub>great</sub><sub>architectures.md) and [OWSOA:Scalability Axiom no 3 - Divide and Conquer](../OWSOA/Scalability</sub><sub>Axiom</sub><sub>no</sub><sub>3</sub><sub>Divide</sub>~and-Conquer.md).  

- **System Architecture**
    - Logical View
    - Physical View - name, version and links to documentation for all deployment units. + UML deployment diagram 
    - Process View
    - Scenario View

#### Subsystem design descriptions

The design descriptions are primarily used when a new developer joins the team or a team member starts working on a new component. Keep this in mind when choosing what to document. 

Focus on documenting important design decisions. Exactly how is this application designed? What are the driving forces behind this design/architecture? 

Which views are most relevant? 

- Scenario View - Important! Without user stories (or use cases) how do we know what the customer actually wants? 
- Process View - Important! What are the main sequences this application supports? 
- Physical View - Important for multi-node applications. 
- Logical View - Seldom useful, since the overhead writing it and keeping it up to date is to large. A reference to JavaDoc and UML class diagrams is usually sufficient. 
- Implementation view - Seldom useful, since the overhead writing it and keeping it up to date is to large. A reference to JavaDoc and UML class diagrams is usually sufficient. 

- Subsystem **design descriptions**
    - Reading guide
    - Subsystem1
        - Subsystem1 Description - what is the purpose and responsibility of the subsystem 
        - Subsystem1 Installation Guide - how to install/deploy the applications, minimal configuration, Firewall and network requirements  
            - External dependencies JMS, Databases, File shares, Web services
        - Subsystem1 Operation Manual - start/stop applications, complete configuration guide
            - Configuration
            - Start and stop
            - Logging
        - Subsystem1 Design Description - for developers: design for this subsystem
    - Subsystem2
        - Subsystem2 Description
        - Subsystem2 Installation Guide
        - Subsystem2 Operation Manual
        - Subsystem2 Design Description

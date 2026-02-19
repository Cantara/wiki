# 4 plus 1 View Model

### Introduction

The 4+1 View Model of Software Architecture is probably the most commonly used methodology for documenting software architecture. It was introduced by Philippe Kruchten in 1995 in the article [Architectural Blueprints — The "4+1" View Model of Software Architecture](http://www.cs.ubc.ca/~gregor/teaching/papers/4+1view-architecture.pdf) and became part of the (Rational) Unified Process. It organizes the architecture documentation in the **Scenario View**, **Process View**, **Logical View**, **Implementation View** and **Physical View**.

- The logical view, which is the object model of the design (when an object-oriented design method is  
  used),
- the process view, which captures the concurrency and synchronization aspects of the design,
- the physical view, which describes the mapping(s) of the software onto the hardware and reflects its  
  distributed aspect,
- the development view, which describes the static organization of the software in its development  
  environment.

### 4+1 Views with appropriate diagrams

|  |  |
| --- | --- |
|  | Process View  - [Sequence diagrams](http://www.agilemodeling.com/artifacts/sequenceDiagram.htm) - [Communication diagrams](http://www.agilemodeling.com/artifacts/communicationDiagram.htm) - [Activity diagrams](http://www.agilemodeling.com/artifacts/activityDiagram.htm)  Physical View  - [Deployment diagram](http://www.agilemodeling.com/artifacts/deploymentDiagram.htm) - Network topology (not UML)  Logical View Describes the structure of the logical elements of the solution. Examples are the domain model  Diagram types:   - [Class diagrams](http://www.agilemodeling.com/artifacts/classDiagram.htm) - [Object Diagrams](http://www.agilemodeling.com/artifacts/objectDiagram.htm)  Implementation View  - [Component Diagram](http://www.agilemodeling.com/artifacts/componentDiagram.htm) - [Package diagram](http://www.agilemodeling.com/artifacts/packageDiagram.htm)  Scenario View Selected use cases/user stories or scenarios that represent typical and/or important functionality for the final solution. The selection of user stories or scenarios is made with respect to their impact on the architecture, or whether they are special in some way or another. The user stories will be addressed in the other views, and will in that way bind the views together.   Format:   - Textual Use Cases or [User Stories](/web/20210511170034/https://wiki.cantara.no/display/dev/User+Stories "User Stories") (recommended) - [Use Case diagrams](http://www.agilemodeling.com/artifacts/useCaseDiagram.htm) - [Usage Scenarios](http://www.agilemodeling.com/artifacts/usageScenario.htm) |

### Enterprise 4+1 View

In an enterprise architecture context one can combine the [Zachman framework](http://en.wikipedia.org/wiki/Zachman_framework)  and the 4+1 View Model in the following conceptual way:

The IT-part of the enterprise architecture may then be organized as follows:

---

### TODO

Are any of the following appropriate in the 4+1 view model?   
Especially interested in where the state machine diagram belongs.

[Interaction Overview Diagram](http://www.agilemodeling.com/artifacts/interactionOverviewDiagram.htm)    
[State Machine Diagram](http://www.agilemodeling.com/artifacts/stateMachineDiagram.htm)    
[Timing Diagram](http://www.agilemodeling.com/artifacts/timingDiagram.htm)

##### Granularity

Let's say a system is decomposed into subsystems, and each subsystem consists of one or more applications (which can be clustered) and external dependencies like databases, file shares or JMS.

In the spirit of agility it seems prudent to make intelligent choices with regards to

- what views to use?
- what views are relevant at *system*, *subsystem* and *application* level.

##### Mapping to SOA

Can the 4+1 view model be used to document a Service Oriented Architecture?   
The literature is vague at best at this point; can someone write some advice/pin-pointers?

### Resources

- IBM Architectural manifesto: [Introducing the 4+1 view model](http://www.ibm.com/developerworks/wireless/library/wi-arch11/)

- [CMU/SEI Architectural Views](http://www.sei.cmu.edu/publications/documents/01.reports/01tn010/01tn010.html#chap03)

- Agile Architecture: [Strategies for Scaling Agile Development - 6. Model Your Architecture](http://www.agilemodeling.com/essays/agileArchitecture.htm#Model)

- Agile Models Distilled: [Potential Artifacts for Agile Modeling](http://www.agilemodeling.com/artifacts/)

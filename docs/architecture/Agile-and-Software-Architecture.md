# Agile and Software Architecture

|  | This is work in progress |

#### Agile methods and architecture

Agile methods have brought a lot of good practices to the field of system architecture and design. Examples are:

- Focus on [lightweight architecture](/web/20210226094714/https://wiki.cantara.no/display/architecture/lightweight+architecture "lightweight architecture"), products and frameworks that enhance agility
- Automated testing and Continous Integration practices and tools
- Replacing [Big Design Up Front](http://en.wikipedia.org/wiki/Big_Design_Up_Front) with "just enough design up front" and "design as you go"
- Strong focus on continous [refactoring](http://www.refactoring.com/) in order to improve the design and structure of the code
- Working software developed early and frequently
- Focus on Design patterns and Domain Driven Design, or as it is stated in the [Agile Manifesto Principles](http://www.agilemanifesto.org/principles.html): "*Continuous attention to technical excellence and good design*"

Although many of these practices where used also before the agile movement started to gain force, the agile movement has done a very good job in promoting these important practices to such an extent that they can now be considered mainstream practices.

#### Architecture challenges in agile today

However, there are also sometimes challenges regarding the state of architecture in agile projects. Some people in the agile community seem to think that "agile = cowboy coding" which may result in a development process with characteristics such as:

- a quick "napkin design" in the first iteration, and "off we go"
- developers hacking away without design and/or coding guidelines
- very short term focus on delivering functionality to the customer, but cutting corners in the software design when doing so
- having difficulty sustaining the development velocity over time
- little or no documentation
- lack of a well defined domain model

Although it is wrong to say that these characteristics are the norm in agile projects today, they are at least mentioned by critics of agile methodology as being examples of bad practices, and what can go wrong in agile projects. The recommended practices on this site can be used to avoid the "cowboy coding" type of agile projects.

###### Agile and the lost art of modeling

In "pre agile" times most software engineers where familiar with [RUP](http://en.wikipedia.org/wiki/Rup) and [UML](http://en.wikipedia.org/wiki/Unified_Modeling_Language). Although some negative things can be said about RUP and UML, they did at least give a strong focus on architecture and modelling. Most software engineers with an ambition of being a lead developer/architect knew how to write a *Software Architecture Document* (one of the artifacts in RUP), and model the important parts of the system architecture as UML models.

Today many young developers on agile projects have a hard time drawing a "UML" diagram on a whiteboard, and describing the architecture of the application they are developing. If this is the case on your project, then take measures to improve this situation, or else your project might face problems down the road.

#### How to ensure good software architecture in agile projects

[What is software architecture?](/web/20210226094714/https://wiki.cantara.no/pages/viewpage.action?pageId=5472511 "What is software architecture?")

###### Recommended practices to ensure good architecture

- [dev:Use the first iteration to establish the core principles of the architecture]
- [Document the software architecture](/web/20210226094714/https://wiki.cantara.no/display/architecture/Document+the+software+architecture "Document the software architecture")
- [dev:The architect should be a coach, not a dictator]
- [dev:Adhere to good OO design principles and patterns]
- Follow [dev:Lean Software Development Principles]
- [dev:Create code examples for others to follow]
- [dev:Hold regular code and design reviews]
- [dev:Ensure every developer knows and understands the architecture principles]
- [dev:Treat non-functional requirements in the same manner as functional requirements]
- [dev:Continous refactoring in order to avoid architecture corruption]
- [dev:Consider using CI tools to monitor adherence to architecture principles]

---

###### Some questions to get you going

- How to ensure a sound architecture when starting a new project?

- How to handle the risk of architecture corruption?

- How to avoid sub-optimization?
  - I.e., which design/architecture decisions a single programmer (or a pair) make by themselves?
  - How to make developers aware of that their decisions might have more far-reaching effects than their single, small component?
  - See [smidigtonull:Enterprise economy versus Project economy]

###### Principles and OOAD

**TODO**: On what foundation should we build or evaluations on? This section is tightly coupled to [smidigtonull:Agile Mindset and Methodology]

- Domain-Driven Design

- Service-orientation, not application-orientation - [Service Categories](/web/20210226094714/https://wiki.cantara.no/display/OWSOA/Service+Categories "Service Categories")

- Convention over configuration principle

- Maintainability is the most important non-functional requirement

|  | "Any fool can write code that a computer can understand. Good programmers write code that humans can understand". (Fowler) |

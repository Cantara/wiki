# Document the software architecture

Documentation is often given low priority in agile projects. During the development phase, when everybody is involved in the design and construction of the software, this might work okay, but later on, when the system needs to be maintained after the initial developers have moved on, then lack of architecture documentation can be a big problem. Documentation also becomes more important as the size and duration of a project increases. 

We recommend to **use a wiki** (such as Confluence) and a user friendly **UML modelling tool** (such as Enterprise Architect) to document the architecture, as this makes the documentation much more accessible and easier to update. In addition it is of course important to have plenty of whiteboards around with sketches of various parts of the architecture.

Architecture should be documented with a number of different _views_ that describe different aspects of the system. The most common set of views are probably the 4+1 views used by RUP:

- **Scenario view** - describes use cases/user stories that encompasses architecturally significant behavior, or technical risks. 

- **Logical view** - describes the logical structure of the system, including architecture layers, the design patterns used, and a description of the domain model. 

- **Implementation view** - contains an overview of the implementation model, i.e. the source code, and its organization in terms of modules into packages and layers. 

- **Process view** - contains the description of how the system is organized in logical deployment artifacts (components), and their interactions and configurations.

- **Deployment view** - contains the description of the various physical nodes for the most typical platform configurations, and how the deployment artifacts (the target of the build process) are deployed to the physical nodes.

We don't recommend creating large amounts of architecture and design documentation as this quikly becomes a burden to keep up to date with the reality. How much to document will be different from project to project, for instance depending on how the system is going to be maintained after the project is finished. **Scott Ambler** gives many good examples of how to document the system architecture in his [Agile Modelling](http://www.agilemodeling.com/) website.  A good technique to avoid lengthy written documentation is to document the high-level design principles of a part of the system, and refer to a [good code example](../smidigtonull/Create-code-examples-for-others-to-follow.md) for the detailed explanation of how it all fits together.

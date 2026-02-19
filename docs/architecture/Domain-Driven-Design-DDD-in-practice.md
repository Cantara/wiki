# Domain-Driven Design (DDD) in practice

The motivation, the way of thinking, and the techniques behind DDD is well defined in the book by Eric Evans. One of the challenges however, is how these can be applied and implemented in real applications dealing with technical boundaries and constraints. To quote [Greg Young](http://codebetter.com/blogs/gregyoung/default.aspx):
> "Traditional enterprise application architecture, such as JEE usually consists of an "object-oriented" domain model encapsulated inside a procedural service layer, persisted in a relational database, flattened out on a data entry screen by the UI layer, and crunched daily into management reports by some reporting tool".

The content on these pages addresses the implementation details developing an application on the Java platform. To begin practicing DDD, it is recommended to examine the [DDD sample application](http://dddsample.sourceforge.net/). The sample domain is well known to the readers of the DDD book, and gives some examples of how the basic concepts can be implemented. However, the application is too simplistic in many ways. There are several issues that it does not cover, like performance trade-offs and transaction boundaries.

- [Clients of the domain model](/web/20210128024526/https://wiki.cantara.no/display/architecture/Clients+of+the+domain+model "Clients of the domain model")
- [DDD friendly architectures](/web/20210128024526/https://wiki.cantara.no/display/architecture/DDD+friendly+architectures "DDD friendly architectures")
- [Domain objects having dependencies to services](/web/20210128024526/https://wiki.cantara.no/display/architecture/Domain+objects+having+dependencies+to+services "Domain objects having dependencies to services")
- [Domain Object Types](/web/20210128024526/https://wiki.cantara.no/display/architecture/Domain+Object+Types "Domain Object Types")
- [Implementing Report functionality with Domain-Driven Design](/web/20210128024526/https://wiki.cantara.no/display/architecture/Implementing+Report+functionality+with+Domain-Driven+Design "Implementing Report functionality with Domain-Driven Design")
- [Package structure and layers](/web/20210128024526/https://wiki.cantara.no/display/architecture/Package+structure+and+layers "Package structure and layers")
- [Separating domain objects from persistence infrastructure](/web/20210128024526/https://wiki.cantara.no/display/architecture/Separating+domain+objects+from+persistence+infrastructure "Separating domain objects from persistence infrastructure")
- [The right tools for the job](/web/20210128024526/https://wiki.cantara.no/display/architecture/The+right+tools+for+the+job "The right tools for the job")

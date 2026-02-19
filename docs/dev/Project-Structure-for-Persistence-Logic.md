# Project Structure for Persistence Logic

#### Persistence logic in a separate Maven project 
We do not want to have persistence logic spread throughout the application, since this would violate basic OO principles like separation of concerns. In a Maven world we then have two options 

a) a separate module within an application 
or 
b) a separate Maven project
or 
c) a multi-module Maven project 

A separate module might be a good idea for simple projects, but normally a separate Maven project is the best approach. This allows multiple clients to use the same persistence logic. It is also a prerequisite for strategies like [RDBMS testing according to JigZaw](RDBMS<sub>~testing</sub><sub>according</sub><sub>to</sub><sub>JigZaw.md). As the persistence structure stabilizes multiple Maven modules should be considered. Especially if the [architecture:Repository](../architecture/Repository.md) pattern is used, each aggregate should (eventually) be put in its own module. When using a RDBMS as persistence back</sub><sub>end, it is acceptable to let relations between entities _within_ the aggregate be relations in the database. Relations _between_ aggregates, however, should be avoided if possible. See also [architecture:Separating domain objects from persistence infrastructure](../architecture/Separating</sub><sub>domain</sub><sub>objects</sub><sub>from</sub><sub>persistence</sub>~infrastructure.md).  

#### Depend on library or deploy as a standalone service? 

If only a single, simple application needs to use the persistence logic, then it makes sense to depend on the library (the jar file) directly. If you have **multiple clients**, need **scalability** or need **search** functionality, then it makes sense to deploy the persistence logic as a separate service.

#### Why is this _agile architecture_? 

These recommendations illustrate how to make the architecture agile. You can start small, but it is easy and cheap to scale to a more heavyweight solution later. The cost of using a separate Maven project is small, and with an [Enterprise Maven Infrastructure](Enterprise<sub>~Maven</sub>~Infrastructure.md) in place, it is so small that it can be ignored all together.

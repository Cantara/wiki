# Logical Requirements to Persistence Products

#### Possible functional requirements 

- Basic CRUD 

- Search/queries 

- Transactions

- Integration (for example use a RDBMS as integration strategy) 

#### Possible non-functional requirements 

- Short ramp-up time 

- Simple programming model / high level APIs. 

- Testability

- HA/scalability - shared state 

- Support for change ("evolvability") 

#### Some thoughts 

Scalability and HA are often contradictory to  short ramp-up time and the wish for high level APIs to simplify programming. Must be choose? Can we have both? 

- We want short ramp-up time, but it must be possible to scale later without a total rewrite. 

- We need to make the solution testable. 

The obvious approaches are: 

- use **one product/solution** which can be embedded AND can be used standalone/clustered. 
    - Does one exist? 

- Create an interface which can be implemented by **multiple products/solutions with different characteristics**. 
    - In the RDBMS world this could (theoretically) be implemented by using an embeddable database (HSQLDB, H2, Derby) for testing and when the application has little load and use for example Oracle when the load increase. Known problems with this approach: none/few RDBMS are 100% compatible (due to a weak/too small SQL standard?), migrations and schema changes are painful, RDBMS does not scale very well (compared to e.g. tuple spaces or In-memory Distributed-data Grid Solutions), etc.
 

An alternative (less obvious) approach is to accept that there is no silver-bullet and embrace/tackle the complexity instead of struggling to deny it. That is not only create interfaces for what we want, but also create a product which implement the patterns we want to use, bridge the gap between our preferred usage and what the products offer and make this "_enterprisey_" solution easily available to the average programmer. It seems that the EDR pattern might be a central concept here... 

**Note about scope**! The suggested solution should aim to be a good and scalable solution for _most_ enterprise scenarios. Simple setups and specialized applications should consider choosing a product specialized for the task. For example for simple CRUD applications the [Active Record](Active-Record.md) patterns seems appropriate. 

- Repository pattern - Evans 

- EDR 

#### Resources 
- [Drop ACID and Think About Data](http://highscalability.com/drop-acid-and-think-about-data)

- [http://wiki.cantara.no/display/PE/Data+laget](http://wiki.cantara.no/display/PE/Data+laget)

- [Agile databases, by Anders Sveen](http://blog.f12.no/wp/2009/01/03/agile-databases/)
- [Migrations for Java, by Anders Sveen](http://blog.f12.no/wp/2009/01/03/migrations-for-java/)

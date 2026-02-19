# Domain Object Types

#### [Entity](/web/20210128025528/https://wiki.cantara.no/display/architecture/Entity "Entity")

"An Entity is an Object that represents something with continuity and identity. An entity is tracked through different states and implementations."

See [this blog](http://stochastyk.blogspot.com/2008/05/entities-in-ddd.html) for some good advice on implementing Entities.

#### [Value Object](/web/20210128025528/https://wiki.cantara.no/display/architecture/Value+Object "Value Object")

"An object that represents a descriptive aspect of the domain with no conceptual identity is called a VALUE OBJECT." [smidigtonull:Evans 2003]

See [this blog](http://stochastyk.blogspot.com/2008/05/value-objects-in-domain-driven-design.html) for some good advice on implementing Value Objects.

#### [Domain Service](/web/20210128025528/https://wiki.cantara.no/display/architecture/Domain+Service "Domain Service")

"A SERVICE is an operation offered as an interface that stands alone in the model, without encapsulating state, as ENTITIES and VALUE OBJECTS do." [smidigtonull:Evans 2003]

See [this blog](http://stochastyk.blogspot.com/2008/05/domain-services-in-domain-driven-design.html) for some good advice on implementing Domain Services.

#### [Aggregate](/web/20210128025528/https://wiki.cantara.no/display/architecture/Aggregate "Aggregate")

"An AGGREGATE is a cluster of associated objects that we treat as a unit for the purpose of data changes. External references are restricted to one member of the Aggregate, designated as the root. A set of consistency rules applies within the Aggregate's boundaries." [smidigtonull:Evans 2003]

Aggregate is not a concrete domain object type, but rather an abstract design concept that groups a set of Entities and Value Objects together. See Package structure and layers for suggestions on how to visualize aggregates.

One repository for each aggregate is usually a good choice. Some suggests that you should not have lazy-loading within an aggregate, only for associations between objects in different aggregates. This of course depends on the amount of data within each root entity association. If memory consumption and slow database queries is not an issue, then you should not do lazy-loading at all.

**Questions**:  
How to effectively reduce the number of associations, to prevent the entire model being loaded into memory ?  
And how to implement domain objects containing data from other sources than the default database ?

#### [Repository](/web/20210128025528/https://wiki.cantara.no/display/architecture/Repository "Repository")

"A Repository is a mechanism for encapsulating storage, retrieval, and search behavior which emulates a collection of objects." [smidigtonull:Evans 2003]

A repository is **not** the same as a Data Access Object (DAO). A repository may use one or more DAO's internally for fetching data, but the concept of a repository is part of the domain model and not technology specific infrastructure. There are lots of clarifications for this elsewhere on the web. What we are concerned with here, is how these can be implemented.

**Questions**:  
One generic EntityRepository having a Criteria object, or one per aggregate with specifically designed finder methods ?

#### Resources

[Repository, the Foundation of Domain Driven Design](http://geekswithblogs.net/gyoung/archive/2006/05/03/77171.aspx)

#### [Factory](/web/20210128025528/https://wiki.cantara.no/display/architecture/Factory "Factory")

"A Factory is a mechanism for encapsulating complex creation logic and abstracting the type of a created object for the sake of a client." [smidigtonull:Evans 2003]

# Aggregate

"An AGGREGATE is a cluster of associated objects that we treat as a unit for the purpose of data changes. External references are restricted to one member of the Aggregate, designated as the root. A set of consistency rules applies within the Aggregate's boundaries." [smidigtonull:Evans 2003]

Aggregate is not a concrete domain object type, but rather an abstract design concept that groups a set of Entities and Value Objects together. See Package structure and layers for suggestions on how to visualize aggregates.

One repository for each aggregate is usually a good choice. Some suggests that you should not have lazy-loading within an aggregate, only for associations between objects in different aggregates. This of course depends on the amount of data within each root entity association. If memory consumption and slow database queries is not an issue, then you should not do lazy-loading at all.

**Questions**:  
How to effectively reduce the number of associations, to prevent the entire model being loaded into memory ?  
And how to implement domain objects containing data from other sources than the default database ?

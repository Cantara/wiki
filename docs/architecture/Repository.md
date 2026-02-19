# Repository

"A Repository is a mechanism for encapsulating storage, retrieval, and search behavior which emulates a collection of objects." [smidigtonull:Evans 2003]

A repository is **not** the same as a Data Access Object (DAO). A repository may use one or more DAO's internally for fetching data, but the concept of a repository is part of the domain model and not technology specific infrastructure. There are lots of clarifications for this elsewhere on the web. What we are concerned with here, is how these can be implemented.

**Questions**:  
One generic EntityRepository having a Criteria object, or one per aggregate with specifically designed finder methods ?

#### Resources

[Repository, the Foundation of Domain Driven Design](http://geekswithblogs.net/gyoung/archive/2006/05/03/77171.aspx)

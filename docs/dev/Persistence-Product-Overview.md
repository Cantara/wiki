# Persistence Product Overview

All products in this overview support **persistence**, but what other responsibility and properties do they have? 
Which are important enough to group by? 

**TODO**: Split "Scalable" into how they scale OR just use (+) and (+)(+) and (x) to illustrate differences? 
E.g. need to show that while Oracle DB sort of scales, it is not even close to the scalability of Oracle Coherence. 

| Product | Type | License | [ACID/BASE | http://queue.acm.org/detail.cfm?id=1394128] | Queries | Data manipulation | Embeddable | HA | Scalable |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Oracle 10g | [RDBMS | http://en.wikipedia.org/wiki/RDBMS] | commercial | ACID | (+) | (+)(+) | (x) | (/) | (!) |  |
| PostgreSQL | [RDBMS | http://en.wikipedia.org/wiki/RDBMS] |  | ACID | (+) | (+) | (x) |  |  |  |
| MySQL | [RDBMS | http://en.wikipedia.org/wiki/RDBMS] |  | ACID^[1 | http://en.wikipedia.org/wiki/Comparison_of_relational_database_management_systems#feat_1_back] | (+) |  | (x) |  |  |  |
| Derby | [RDBMS | http://en.wikipedia.org/wiki/RDBMS] |  | ACID | (+) |  | (/) | (/) | (x) |  |
| [HSQLDB | http://hsqldb.org/] | [RDBMS | http://en.wikipedia.org/wiki/RDBMS] |  | not ACID | (+) |  | (/) | (x) | (x) |  |
| [H2 | http://www.h2database.com/] | [RDBMS | http://en.wikipedia.org/wiki/RDBMS] | [MPL | http://www.mozilla.org/MPL] 1.1 or (unmodified) [EPL 1.0 | http://opensource.org/licenses/eclipse-1.0.php] | ACID | (+) |  | (/) |  |  |  |
| [Prevayler | http://www.prevayler.org/] | [Serialization | http://en.wikipedia.org/wiki/Serialization] | BSD License, LGPL | ACID | (x) |  | (/) |  |  |  |
| [Itzam | http://www.coyotegulch.com/products/itzam] (replacing [JISP | http://www.coyotegulch.com/products/jisp/]) | [Serialization | http://en.wikipedia.org/wiki/Serialization] | GPL + closed source |  |  |  |  |  |  |  |
| [Blitz | http://www.dancres.org/blitz/] | [JavaSpaces](JavaSpaces.md) | OSS |  |  |  |  | (/) | (/) |  |
| [Gigaspaces | http://www.gigaspaces.com/] | [JavaSpaces](JavaSpaces.md) | commercial | ACID | (/) |  |  | (/) | (/) |  |
| [SemiSpace | http://www.theserverside.com/news/thread.tss?thread_id=55069] | [JavaSpaces](JavaSpaces.md) inspired tuple space | OSS |  | (?) |  |  | (?) | (?) |  |
| [Apache Jackrabbit | http://jackrabbit.apache.org/] | [JCR | http://jcp.org/en/jsr/detail?id=170] | OSS |  |  |  |  |  |  |  |
| [Alfresco | http://wiki.alfresco.com/wiki/Introducing_the_Alfresco_Java_Content_Repository_API] | [JCR | http://jcp.org/en/jsr/detail?id=170] | OSS |  |  |  |  |  |  |  |
| [Oracle Coherence | http://www.oracle.com/technology/products/coherence/index.html] | In<sub>~memory Distributed</sub>~data Grid Solution | commercial |  |  |  |  | (/) | (/) |  |
| [Neo4j | http://neo4j.org/] | graph database | [GNU Affero GPL version 3 | http://www.fsf.org/licensing/licenses/agpl-3.0.html] |  |  |  |  | (/) | (/) |  |
| [Amazon SimpleDB | http://en.wikipedia.org/wiki/Amazon_SimpleDB] | [Distributed database | http://en.wikipedia.org/wiki/Distributed_database] |  |  |  |  |  | (/) | (/) |  |
| [Amazon Simple Storage Service aka. S3 | http://en.wikipedia.org/wiki/Amazon_Simple_Storage_Service] | online storage web service |  |  |  |  |  | (/) | (/) |  |
| Google App Engine using [BigTable | http://en.wikipedia.org/wiki/BigTable] | proprietary database system |  |  |  |  |  | (/) | (/) |  |

###### Legend 

(x) - not supported 
(/) - supported 
(+)(+) - good support 
blank - please fill inn 
[ACID](http://en.wikipedia.org/wiki/ACID) - Atomicity, Consistency, Isolation, Durability
[BASE](http://queue.acm.org/detail.cfm?id=1394128) - An Acid Alternative  

#### Resources 
- http://blog.endpoint.com/2015/04/new<sub>~nosql</sub><sub>benchmark</sub><sub>cassandra</sub>~mongodb.html

- [Anti<sub>~RDBMS: A list of distributed key</sub><sub>value stores](http://www.metabrew.com/article/anti</sub><sub>rdbms</sub><sub>a</sub><sub>list</sub><sub>of</sub><sub>distributed</sub><sub>key</sub><sub>value</sub>~stores/)
- [Comparison_of_relational_database_management_systems](http://en.wikipedia.org/wiki/Comparison_of_relational_database_management_systems) 
- [current<sub>~database</sub><sub>debate</sub><sub>and</sub><sub>graph](http://blog.neo4j.org/2009/04/current</sub><sub>database</sub><sub>debate</sub><sub>and</sub>~graph.html)
- [Cloud_storage](http://en.wikipedia.org/wiki/Cloud_storage#Storage)

# Database categories explained

The purpose of this article is to make it easier to choose what type of database is suited for your application. 
The general idea is to describe data models suited for each type. 

Some use cases are described in [NoSQL, Heroku, and You](http://blog.heroku.com/archives/2010/7/20/nosql/). 

| Category | Product examples | When to use it | Comment |  |
| --- | --- | --- | --- | --- |
| Key Value / Tuple Store | Amazon SimpleDB, Amazon Dynamo, Voldemort | Large datasets, read/write..  no advanced queries, distributed environments | Test using HashMap |  |
| Wide Column Store / Column Families | Google BigTable, Hbase, Cassandra |  |  |  |
| Document Store | MongoDB, CouchDB |  | Collections of K-V collections |  |
| [Graph Databases | http://www.graph-database.org/] | Neo4J, Infinite Graph | graph in domain model, relation intensive queries | K-V on both nodes and edges |  |
| RDBMS | OracleDB, PostgreSQL, MySQL/MariaDB, MS SQL Server |  |  |  |
| Touple-space / Grid & Cloud Database Solutions | GigaSpaces | distributed code&data architectures |  |  |
| Multivalue Databases | Rocket U2, OpenQM |  |  |  |
| [Object Databases | http://odbms.org/] | db4o, Objectivity |  |  |  |
| XML Databases | Mark Logic Server, eXist |  |  |  |

**The event source poem - the tale of polyglot persistence**

- **If I were** an enterprise repository
- I would love to have the read/write of key-value stores for my CRUD operations
- so I could stop worrying about SLA and data volumes

- **If I were** an enterprise repository
- I would kill for the flexibility of a search index to handle the most demanding client
- and rather extend and embrace exciting new queries

- **If I were** an enterprise repository
- I would marry a RDBMS to handle audit ability to the end of my life
- for who does not love answers to who did what to whom and when?

- **If I were** an enterprise repository
- I go to war to archive social experience like in a graph database 
- and rather avoid today's awkward social life

- **If I were** an enterprise repository
- I really need to combine and mix the fantastic features of technology
- and live happy forever after in the land of polyglot persistence....

Totto-11
> 💡 
> 💡 h4. Resources 
> 💡 
> 💡 * [Overview of NoSQL by Emil Eifrem (YouTube)](http://www.youtube.com/watch?v=sh1YACOK_bo&noredirect=1)
> 💡 * [NoSQL Databases: What, Why, and When by Lorenzo Alberton](http://nosql.mypopescu.com/post/6412803549/nosql-databases-what-why-and-when)
> 💡 * [http://nosql.mypopescu.com/kb/nosql](http://nosql.mypopescu.com/kb/nosql) 
> 💡 * [http://nosql-database.org/](http://nosql-database.org/)
> 💡 
> 💡 * [http://bigdatanoob.blogspot.no/2012/11/hbase-vs-cassandra.html](http://bigdatanoob.blogspot.no/2012/11/hbase-vs-cassandra.html)

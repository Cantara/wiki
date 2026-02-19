# NoSQL alternative to RDBMS - CRUD app

Many choose to use a RDBMS, often Oracle, without actually considering alternatives. RDBMS has many advantages and disadvantages.

#### Context / use case

A simple CRUD application with average performance requirements and 99,9% uptime requirements (which suggests no single-point of failure). Cover the most used functionality found in Oracle and be a lot easier to test, deploy, upgrade and scale. (E.g. scale out by adding a new node should be really simple.)

#### Requirements

- ACID

- Possible to have both HA and embeddable solutions without changing business code. (Possible to switch products if they both follow the same standard.
  - It must be possible to test the persistence "layer" on a single, isolated laptop.

- Possible to implement simple searches. A more OO model than SQL would be nice.

- Scale for complexity over size. => Document and graph dbs seems more appropriate than key-value stores and bigtable clones. What about tuplespaces?

#### Brainstorming on products and design

- Using a search engine like for example **Lucene** is enticing. Can we make adapters similar to [Spring JmsTemplate](http://static.springsource.org/spring/docs/2.5.x/reference/jms.html)  to make some common use cases really, really easy to use?

- Is Neo4j embeddable?

- Is Blitz embeddable?

- What about cache strategy? Which are most common?

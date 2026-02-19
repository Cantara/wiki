# Kjartans notes from Emils talk

#### Notes on Emil Eifrem - Neo4J

Check out the [neo page](http://neo4j.org/) for more details

- The death of rdbms
    - CouchDB
    - Simple DB
    - BigTable
    - Cassandra
- Graphs
    - Your file system (Simlinks, shortcuts)
- Trends
    - Trend 1 - Data is getting more connected (from text documents in the early days to wikis, tagging, rdf)
    - Trend 2 - more semi-structured (individualization of content)
- As the information gets more complex the performance of rational databases drops
- Graph database is more "whiteboard friendly"
- Graph database model
    - nodes
    - relationship between nodes
    - properties on both
- the relations are typed (know, belong, coded by)
- Nodes consist of properties
- Only support primitives (its not a object db)
- You can dynamically create relationships (the name of the relationship is a string)
- Traversers (Traversing a node space)
    - order: [breadth first](http://en.wikipedia.org/wiki/Breadth-first_search) and 
- Neo-graph is 
    - disk based
    - transactional
    - scalable (several billion nodes)
    - robust (5 yrs in prod)
- Prs and cons
    - + no o/r impedance
    - + easily evolve schemas
    - - lack in tool and framework support

The session ended with a discussion on licences - conclusion: make sure you look into it before using it!

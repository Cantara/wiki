# Stigs Neo4J notes

In these days of web3.0 with hot topics as "Semantic Web", "RDF", "graphs" and that stuff.
At the GeekCruise, we got a short introduction to Neo4J, a network/graph database that is supposed to provide Web3.0, Semantic Web and RDF greatness. 
Its great advantage is of some kinds of search (graph traversal, shortest route) and do this quite fast.
It can also store partially structured information, eg. V1.0 and v1.1 of Person in the DB at the same time.
It also integrates well with Qi4J, you don't need ORMaping, and the graph can be read from and persisted to RDF.

```
//Setting up the database in a folder called myNeoDB
NeoService neoDb = new EmbeddedNeo("myNeoDB"); 
//Create test dataset
Node neo = neoDb.createNode();
neo.setProperty("name", "Thomas Andersson");
Node trinity = neoDb.createNode();
neo.createRelationshipTo(trinity, MyRelationShipTypes.KNOWS);
```

Queries can be done with SPARQL, or a traverser: 
```
Traverser friendFinder(Node person) {
        return person.traverse(
                Traverser.Order.BREADTH_FIRST,
                StopEvaluator.END_OF_NETWORK,
                ReturnableEvaluator.ALL_BUT_START_NODE,
                MyRelationShipTypes.KNOWS,
                Direction.OUTGOING);
}
```

[The Matrix is as simple as Unzip og "mvn test"!](matrixTest-zip.md)
![matrix.png](matrix-png.md)(matrix.png)

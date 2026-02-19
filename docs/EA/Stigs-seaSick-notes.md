# Stigs seaSick notes

## What I've learned

- The assembly is possibly the more fun part to start poking, when creating a Qi4J project. An assembly, the wiring of the application, can be more easy to understand how works in an early stage, rather than waiting to a later, where wiring is a must.
- Qi4J comes with a store/persistence out of the box, along with a query language. That would be a nice way of starting a project; "Store myTestDB = new Qi4JMagicPersistantHashmap"
- The Qi4J Store has REST for server backend persistence for a thick client - [http://java.dzone.com/news/qi4j<sub>~rest</sub><sub>entitystore</sub><sub>and</sub><sub>spar](http://java.dzone.com/news/qi4j</sub><sub>rest</sub><sub>entitystore</sub><sub>and</sub>~spar)

- Great communication for Geek Cruises: Wiki (possibly slow), IRC (have a server on laptop) and email list 

Persisting store to RDF

MemoryEntityStore is one place to start development

Run the jetty app with /qi4j/extensions/rest/src/test/java/org/qi4j/rest/Main.java
localhost:8080/qi4j/query/index  //Dump as rdf
http://localhost:8040/qi4j/entity.html - watch your entities

JdbmEntityStore should make you able to store on disk as xml

Hope that tutorial/example on entityStorage is coming

Note on Assembly would be nice? Link to documentation?

My model
JavabeanSupport

HyperTransport - Qi4J
JavabeanMixin

## EDR
http://en.wikipedia.org/wiki/EDR - "Election Day Registration", "EDR Desalination, an electrodialysis process", "European Drawer Rack", "Emergency Detour Route"

Use compression, RDF and partitioning

export MAVEN_OPTS="-Xmx1024m -Xms512m" for building qi4j

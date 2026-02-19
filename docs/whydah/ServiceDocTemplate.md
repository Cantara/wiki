# ServiceDocTemplate

description of responsibility here

possibly a diagram of how service integrates with other services.

#### Integration endpoints

| Name | Type | What | Clients | Comment |
| --- | --- | --- | --- | --- |
| One thing | HTTP (REST [level 2](http://martinfowler.com/articles/richardsonMaturityModel.html)) |  |  | not using hypermedia yet |
| Something | JMS Queue |  |  |  |

#### Operations

###### Install MongoDB

1. [Download 2.4.8](http://fastdl.mongodb.org/win32/mongodb-win32-x86_64-2008plus-2.4.8.zip) and unzip
2. md mongodb-data
3. md mongodb-log
4. Create mongod.cfg:
5. D:\SERVERS\mongodb-2.4.8\bin\mongod.exe --config D:\TomraPlus\mongodb-2.4.8\mongod.cfg --install
6. net start MongoDB

Reference documentation: [Install MongoDB on Windows](http://docs.mongodb.org/manual/tutorial/install-mongodb-on-windows/)

###### Install application

1. Use standard installation script *update-application.bat*.

###### Backup

1. Service stores update metadata in a document database, MongoDB. Several [backup strategies](http://docs.mongodb.org/manual/core/backups/) are supported. We suggest using [Backup and Restore with Filesystem Snapshots](http://docs.mongodb.org/manual/tutorial/back-up-databases-with-filesystem-snapshots/) to avoid shutting down the application to take backups.

2. Service stores some resources (files) on filesystem. The location of this file store is controlled by the property *file.store.basedir* in app.properties. It is not considered necessary to stop the application before backup.

###### Monitoring

1. HTTP endpoints available
2. JMS server available
   1. Destination activity (e.g. no or very slow consumers)
3. [Monitoring for MongoDB](http://docs.mongodb.org/manual/administration/monitoring/)
4. Disk space available for file store.

#### Development

Source code: ssh://something.git

Test tools: [TestNG](http://testng.org/doc), [Rest assured](http://code.google.com/p/rest-assured/wiki/Usage), [Fongo](https://github.com/foursquare/fongo)  (in-mem MongoDB)

###### Technology stack

1. [Jersey 2.x](https://jersey.java.net/) (REST endpoints)
2. [Jackson](http://jackson.codehaus.org/) for JSON parsing
3. [Embedded Jetty 9](http://www.eclipse.org/jetty/documentation/current/embedding-jetty.html#d0e15970) (necessary to use web.xml)
4. Spring DI
5. [MongoDB](http://www.mongodb.org/) - Document oriented database for persistence.
   1. Mature, schema-less, well-documented, good backup options, support simple queries
6. [Spring Data MongoDB](http://projects.spring.io/spring-data-mongodb/) to simplify integration with MongoDB
7. [Spring JMS](http://docs.spring.io/spring/docs/2.5.3/reference/jms.html)

###### Design notes

- [Possibility of duplicate Mongo ObjectId's being generated in two different collections?](http://stackoverflow.com/questions/4677237/possibility-of-duplicate-mongo-objectids-being-generated-in-two-different-colle)

#### See also

[RFC 2616 Fielding, et al - Method definitions](http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html)

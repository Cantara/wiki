# Separating domain objects from persistence infrastructure

#### Detecting changes in objects

Domain objects should be unaware of any persistence infrastructure. The objects need to be saved however, whether it is in a database, flat file, over the network, datagrid, or otherwise. The persistence component needs to be aware of runtime changes in the domain model when:
1. New objects are created
1. There are changes to an object's attributes
1. When root entities are deleted. Value objects and other entities not classified as root entities can be detected by the previous bullet point.

What we really want to avoid is to have an explicit call from either a domain object or a client for these notifications.

In ORM frameworks like Hibernate, the session manager needs to control the objects in order to automatically persist any changes. New objects being created and objects modified outside the session context needs to be given to the session manager explicitly. The domain objects should always live inside the session, thus avoid using detached domain objects. Creating new objects should be handled by a Factory. The Factory implementation can notify the session manager before returning the new object to the client.
The last issue was to notify the ORM session manager when root entities are deleted. Root entities does not delete themselves. For example think of a _Bank Account_ entity. The Bank Account does not know how to terminate itself. Instead someone else does that job, in this case either a customer or a bank clerk. In practice, a _Service_ object or a _Repository_ object might implement the delete action. Then it is straight forward to have the implementation of the Service or Repository to invoke the session manager. Remember that it is only the interfaces that are part of the domain, not the particular implementation of it.

#### Use of annotations

The use of annotations in java code for all sorts of purposes have been very welcomed by developers. It may sound like a good idea to put all the necessary configuration in one place: the source file. But not all annotations are for the good. There is a distinction between general concepts & metadata versus specific technical configuration. The former makes the codebase richer, while the latter mix unrelated stuff together. Adding Hibernate specific annotations like table and column names, primary key generators, database indexes etc breaks the separation of concern principle. The domain object should not be concerned with how data are stored in a persistent storage. Move the configuration mappings out into separate files, like hibernate xml files or in separate java classes.

#### Getters and Setters are evil

Do not expose unnecessary methods in your domain objects to clients. It is too easy to have your IDE autogenerate getters and setters for an object's private fields, but don't be tempted to do this. Only expose business methods that makes sense in the domain. The same applies also to class constructors. The reason for this is that it makes an objects interface harder to read and understand, because of the added complexity. And if the client is not supposed to call a single setter method on an object, then just don't make it possible.

Value objects in DDD should most of the time be immutable, for all the good reasons mentioned in the book. Only one constructor and no setters will force this constraint. 

To persist object state using an ORM tool, the tool needs access to the attributes of an object. In Hibernate, configure the mapping to use direct private field access instead of setters and getters: 
```
<hibernate-mapping default-access="field"/>
```

Hibernate does require a null<sub>~constructor for the domain objects it creates. If it doesn't make sense in your domain to have such a constructor, like when a factory or other clients should only use a specific not</sub><sub>null constructor, then declare the null</sub><sub>constructor as private. The clients will not see this "misleading" constructor. Using a Hibernate Interceptor you can code your object initialization yourself. This can be useful in certain situations and the null</sub>~constructor requirement does no longer apply.

Domain objects created as Spring beans typically have setters for bean references. One way of avoiding this is to use the `@Autowired` annotation on the private field instead. If this is not possible or not desirable for other reasons, you might consider creating an interface for the domain object which is returned to clients. This interface will only contain real business methods.

# Catch oriented exception strategy

#### Context 

Java application based on Spring and Hibernate and a SQL database. Integration to other systems using Webservice and JMS. 

#### Principles 

- Focus on the needs of the caller, don't waste time creating a more exceptions than the caller want to use. 

- Isolate the application from technical details of both data access (Hibernate, JDBC and database specifics) and integration details. 

- Let "unexpected errors", e.g. NullPointerException and other programming errors, propagate to the top of the stack and be logged there. 

#### Implementation 

###### Integration with database 

Isolate the data access logic from the rest of the application. 

- Since we use Spring, we can utilize the rather big exception hierarchy created for this purpose, see [DataAccessException](http://static.springsource.org/spring/docs/3.0.x/reference/dao.html#dao-exceptions) or the [JavaDocs](http://static.springsource.org/spring/docs/3.0.x/javadoc-api/org/springframework/dao/DataAccessException.html/). The general advice is to isolate the application from library specifics, but since Spring often is the core of applications which use, it doesn't really add any value to create abstraction layers for Spring. 
    - Developers, dbas and sysadmins should be notified of this type of exceptions. 

- **DataException** - this is intended for situations where the data in the database is wrong or not as expected. It should not be necessary if we control access to the database, but unfortunately it is often the case that data is added to the database from another service, user or script. 
    - The owner of the data should be notified of DataExceptions. 

###### Integration with Webservice, JMS and other technologies 

Catch any exception thrown when calling an external service and wrap it in an application specific, unchecked exception. 

- **ServiceUnavailableException** - network problem, authentication problem, service is rebooting, etc. 
    - The network admin and sysadmin for external service  etc. should be notified of this kind of error. 

- **ErrorInExternalServiceException** - the service is available, but some error occurs and the external service throws an exception. 
    - The sysadmin for the external service should be notified of this error.

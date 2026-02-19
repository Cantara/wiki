# Audit log

## Audit logging in web applications

Audit logging is important in applications that handles sensitive data. It is always nice to have, but mandatory if your application enables viewing of sensitive data. What is a valid audit log:

A good log is: 

A log that keeps track of **who** does **what**, **when**.

What to remember:

- Log **before** you do something. In case of exception the state of the application should be known.
- Is this a human readable log, or is it analysed by a tool?
- Make sure that the trace can be audited
- Which context information is needed when reconstructing actions?
- In order to answer **who**, the logging mechanism should have access to user information.
- In order to answer **what**, the _actions_ of "who" should be logged, be it read data X, update data Y, delete data Z. It is not sufficient to log that a user reads data from a table, you need to log what data was read (don't log the data itself, log sql query with parameters or equivalent information).

## Implementation 

#### Trace methods with AOP as a debugging tool in distributed systems? 

- [Tracing methods with AOP](http://www.developer.com/java/other/article.php/10936_3109831_4)
- [Logging/bugtracing using Spring 2, AOP, Reflection and Log4J](http://articles.alyssar.nl/2008/03/06/loggingbugtracing-using-spring-2-aop-reflection-and-log4j/)

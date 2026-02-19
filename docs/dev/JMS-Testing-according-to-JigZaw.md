# JMS Testing according to JigZaw

#### Introduction 
We will now present how to efficiently test JMS in a complex system. 

#### Unit tests 

Unit tests should not depend on environment, so unit tests should not depend on JMS. This means that any tests that need JMS should not be run when using _mvn clean install_. This can be setup using TestNG and the group functionality found there. A typical setup is to use two testng.xml configuration files: 

- testng.xml - e.g. run all fast tests that doesn't require any environment. (no jms) 
- testng<sub>~test</sub><sub>all</sub><sub>environments.xml - run slow tests and tests that depend environment (JMS</sub>~tests) 

#### Service tests 

###### Service test with in-memory ActiveMQ broker 

To properly test a service which depend on JMS we must of course send JMS messages, but this does not mean that we must employ a standalone, heavyweight JMS server. An in-memory ActiveMQ broker started in a separate process is a faster and functionally equivalent approach. 

It may be a good idea to create a separate package or library for the code necessary to fork off a separate process for in<sub>~memory "infrastructure". See [How to start a new operating system process from Java](How</sub><sub>to</sub><sub>start</sub><sub>a</sub><sub>new</sub><sub>operating</sub><sub>system</sub><sub>process</sub><sub>from</sub>~Java.md) for a code example. 

**TODO**: Explain technical implementation of _processHelper_ and _jmsHelper_. 

 
###### Service test with mocked JMS calls  

Given a good architecture and proper unit testing, the in<sub>~memory tests explained previously covers the purpose of service tests. However, in the real world we have often found that so called _sequence tests_ are useful. Their purpose is to test that a service calls methods in the expected sequence. We recommend writing this kind of tests when a) the flow of the service is complex or b) it is not possible (at this time) to write service tests with in</sub>~memory environment. 

Another type of test which falls into this category is _exception management_. Exception management should theoretically be best to test without environment, but in practice we would prefer to have these tests against a real, in-memory implementation. 

### System tests 

According to JigZaw it is possible to have system tests with no data and no environment, but these types of tests are rare. This leaves us with tests with data or no data (controlled data). A system test can span _one_ or more deployment units. A test which only test one can still be called a system test, but it is probably better to call such tests _service tests with environment_.

System test are structured separate from the other code. In a Maven world they be put in separate Maven projects. 

The purpose of functional system tests is to ensure that all deployment units integrate nicely. This is often verified by running tests which exercise the complete system end to end. A possible initial setup can be one _happy camper_ test for each logical service the systems offers. Further work should focus on top level user stories and functionality necessary for the acceptance test to run cleanly. (It might be possible to let the system tests evolve into acceptance tests if the customer agrees to working agilely all the way.) 

When the functionality works as expected we should extend or system test suite with non-functional tests. 
Non-functional system tests should (IMHO) like e.g. performance test can be setup by extending the functional tests 

So, how to do this for JMS? 

- Set up a JMS server from the same vendor as will be used in production, with configuration identical to the production server. 
    - Write a test which ensures that the setup works. Test communication in isolation with dummy data. 

- Write tests that exercise all different JMS "flows". This would normally entail sending one example of each [Message](http://java.sun.com/javaee/5/docs/api/javax/jms/Message.html) type to all Queues and Topics in the system. 

- Run regular functional and non-functional system tests.

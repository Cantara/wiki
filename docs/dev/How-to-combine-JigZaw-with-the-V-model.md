# How to combine JigZaw with the V-model

The [V<sub>~model](http://en.wikipedia.org/wiki/V</sub>~Model_(software_development)) groups tests into **unit tests**, **integration tests**, **system tests** and **acceptance tests**. To model big distributed systems, higher granularity and additional levels / test types is needed. 

There is also the matter of responsibility; which department or role is responsible for each test level? In an ideal (agile) world this separation would not exist, and the team/organization would organize themselves to solve the problems iteratively. If you are not so fortunate, we can split the tests into two groups. The test department is typically responsible for System integration test, System test, System test and Production test. Development is responsible for Unit test, Service test and Multi-service test. The validation in between is typically the responsibility of a test manager and is a review the test reports from development. These reports enables the test manager to decide what to test in the system test. It also serves as an "approval" of the handover. 

Production test 
Acceptance test 
System test 
System integration test 

(Validation) 

Multi-service test 
Service test 
Unit test 

TODO: figure to illustrate 

See [JigZaw Test Levels](JigZaw<sub>~Test</sub>~Levels.md) for descriptions of each test level.

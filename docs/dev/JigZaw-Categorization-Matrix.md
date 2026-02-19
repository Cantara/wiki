# JigZaw Categorization Matrix

The purpose of the categorization matrix is to be able to discuss and classify different kinds of tests. It is not critical whether a certain test is classified as a unit or service test, but it is important to have separate tests for with/without data and with/without environment. This makes it much easier to **write** the tests in the first place and makes it easier to work in an agile fashion. The main drivers behind the model are

- **speed** (which restricts when it can be run),
- **with or without data** (separate data-driven tests from regular functionality tests) and
- **with or without environment** (Servlet\- and app-containers, database, JNDI, JMS, etc. highly affects the speed of the test. Tests that depend on such an environment should be separated from those that do not.)
- only maven and java should be required for running tests before check-in.
- the CI server should handle all slow tests and all tests that depend on external systems. This allows one developer or system administrator to set up external systems _once_, instead of every time a new development environment is needed. 

|  | Data/environment combination | Location |
| Unit Test | No data and no environment | White box: src/test in the same module as the unit |
| --- | --- | --- |
| Service Test (CS) | All combinations | White box: same Maven module/project as the service |
| --- | --- | --- |
| System Test (ACS/A2A) | All combinations | Black box: as a separate Maven module if it tests modules only within a project, else a separate project |
| --- | --- | --- |

**No data**: Test with one or a few values within the interval. (Which input is not essential.)
**Data**: Test with a set of values, test with all values, test according to a given data set (data driven)
**Environment**: Which hardware is available, which OS, etc.

---
###### Crude interpretation

These examples illustrate the point, but are of course generalizations. 

- **System tests**
    - almost always has environment and/or are data-driven. 
    - almost always has some level of integration of components. 
    - are seldom fast. 
    - are often costly to both implement and run. 

- **Unit tests** 
    - should never depend on environment.
    - should never be data-driven (only controlled data should be used). 
    - should never span multiple components and can this not be called integration tests. 
    - should always be fast. 
    - are the cheapest kind of tests to both implement and run. 

- **Service tests** 
    - can depend on environment.
    - can be data-driven (only controlled data should be used). 
    - should never span multiple domain components, but can integrate with services like JMS, webservices and databases and can thus be termed integration tests. 
    - can be both fast and slow. 
    - are cheaper than system tests, but normally more expensive than unit tests.

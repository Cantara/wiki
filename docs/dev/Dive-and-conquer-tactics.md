# Dive and conquer tactics

#### Tactics 
This paragraph will explain how we can apply the [JigZaw Multidimensional Test Categorization](JigZaw<sub>~Multidimensional</sub>~Test-Categorization.md) to discuss and choose different types of tests. 

###### Loose coupling between endpoint and service 

The coupling between a service and endpoints can be said to be loose if it is possible to test the processing/generation of data and the code used to expose the service in a given endpoint in separate tests. 

**Example 1**: A service which publish some message to a JMS Destination

1. The processing/generation of data should be possible to test using fast, **in-process** developer (unit) tests with no platform dependencies. 
1. Basic integration with the JMS server and the Destination can be tested using an in<sub>~memory JMS server (e.g. ActiveMQ). If the JMS server is run locally and controlled by the test, it can be categorized as **with platform** and **out</sub>~of-process**. These types of tests are slower and more complex than the previous type. 
1. Full<sub>~blown testing (think clustering, fail</sub><sub>over, etc.) of the JMS integration requires an externally deployed JMS server. These types of tests can be categorized as **with platform** and **distributed** (not only out</sub><sub>of</sub>~process). These are the most expensive types of tests with regards to speed and complexity. 

**Example 2**: A service with a synchronous webservice endpoint 

1. The processing/generation of data should be possible to test using fast, **in-process** developer (unit) tests with no platform dependencies. 
1. Basic integration with the webservice can be tested using an in<sub>~memory application server (e.g. Jetty). If the server is run locally and controlled by the test, it can be categorized as **with platform** and **out</sub>~of-process**. These types of tests are slower and more complex than the previous type. 
1. Full<sub>~blown testing (think clustering, fail</sub><sub>over, etc.) of the webservice integration requires an externally deployed webservice. These types of tests can be categorized as **with platform** and **distributed** (not only out</sub><sub>of</sub>~process). These are the most expensive types of tests with regards to speed and complexity.

Another good way to use divide and conquer in example 2 is to separate the endpoint form the implementation so you can do efficient in-process testing on the implementation, and focus on distribution/platform testing on the endpoint artifact.

###### Differentiate between controlled data and user provided data 

All tests needs testdata, but where the testdata comes from can vary. Testdata created by developers to ensure that their code works as they expect can be categorized as **controlled data**. Testdata generated from actual use of the system or by generating all possible permutations of possible input data is something quite different. We can use the data dimension to divide the problem into smaller subproblems by testing that the implementation works as the developer intended it to work first before exposing the code to a unknown dataset. This will reduce or possibly eliminate the need to ask whether the the test failure is caused by **poor/erroneous data** or by a **bug** in the code.

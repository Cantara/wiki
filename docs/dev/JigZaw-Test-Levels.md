# JigZaw Test Levels

The [V-model](http://en.wikipedia.org/wiki/V-Model_(software_development)) groups tests into **unit tests**, **integration tests**, **system tests** and **acceptance tests**. Unit and system tests are the same in JigZaw, but integration and acceptance tests are used as properties/aspects of tests, not as test levels. We also use the test categories **service test** and **multi-service test** to fill the gap between unit test and system tests. 

#### Test levels 

**{+}Production test{+}** are test performed by Operations to verify that the system actually works in production. 

[**Acceptance tests**](http://en.wikipedia.org/wiki/Acceptance_test) are used by the customer to decide whether to accept a delivery or not. In spirit of the ideas from the [agile manifesto](http://agilemanifesto.org/), we boldly claim that acceptance test should be the **{_}property{_}** of a test, not a specific type or classification. In other words, the customer (business side) and the development team should work together to ensure that the tests reflect the behavior the customer wants. I.e., by increased **customer collaboration** we can get a tighter mapping between code and domain and at the same time minimize time and money spent on testing. (We work smarter, so to speak.) These concepts are derived from DDD and BDD.

[**System tests**](http://en.wikipedia.org/wiki/System_testing) are [black-box tests](http://en.wikipedia.org/wiki/Black_box_testing) that verify that the system meets its functional and non-functional requirements. The goal is to ensure that _Application to Application Services (A2A)_ and _Human to Application Services (H2A)_ behave as expected. Note that system tests are often fragile due to tight binding to environment and data and might very often be the most difficult tests to write and maintain. Normally these tests utilize multiple nodes (and of course multiple processes). It is often very expensive to fully automate these tests, so normally we see a combination of semi-automated scripts and manual tests here.  

**{+}System integration tests{+}** are tests that verify the integration between internal and external systems. Message formats, encoding and protocols should be verified at this level. 

**{+}(Validation){+}** is an (in)formal inspection where each service is put through a basic quality review before further testing is begun. 

**{+}Multi-Service tests{+}** are single node, but multi-process tests. These are much cheaper than multi-node system tests because they are much easier to automate. (process-helper is crucial). These tests cover some of the same aspects as the well-known _system_test_, but the overlap _should_ be minimal. Note that only functional aspects can be tested with multi-service tests. All non-functional requirements must be tested with a system test. Always prefer a multi-service test to a system test, because these are cheaper to implement and maintain. 

**{+}Service tests{+}** are code-centric (white box) tests that ensure that a _service_ behave as expected. If we follow [OWSOA:Service Categories](../OWSOA/Service-Categories.md) we typically think _Core services (CS)_ or _Aggregated Core Services (ACS)_. These test supplement unit tests and should not overlap. Service tests can have both be data-driven and have external environment like JMS or database, but should not integrate with other components/subsystems. 

[**Unit tests**](http://en.wikipedia.org/wiki/Unit_test) are low-level, code-centric (white box) tests that verify that your code behaves as expected. In Java the _unit_ is usually a class. Our definition complies with the traditional one, but the delegated responsibility may differ, as explained in the [test structure section](Test-structure-and-Single-Responsibility-Principle.md).

#### Test properties/aspects
[**Integration tests**](http://en.wikipedia.org/wiki/Integration_testing) verify that some set of components/modules/subsystems collaborate as expected. E.g., a test that needs a database is an integration test. A test that depends on more than one component is an integration test. This term is too wide and imprecise to be useful as something more than the abstract concept that everyone is familiar with. We have therefore try to avoid using integration test for categorisation and use instead as an _aspect_ of a test. 

**Functional tests** verify that the code has the expected functionality. If it is an elegant solution, how scalable it is, whether it can be automatically deployed, etc. is not important here. Since many different test types can be used to verify the functionality we have chosen to call this an _aspect_.  

**[Non-functional tests](http://en.wikipedia.org/wiki/Non-functional_tests)**: E.g. performance, robustness

**Diagram: test.aspects**
**TODO**: Will probably need to be updated with new concepts.

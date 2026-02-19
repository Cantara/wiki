# Test nomenclature and classification

# Part 1 

## Intro
The [V<sub>~model](http://en.wikipedia.org/wiki/V</sub><sub>Model_(software_development)) is a popular approach to testing in a  typical [waterfall](http://en.wikipedia.org/wiki/Waterfall_model) project. With the rising popularity of agile development methodologies like XP and Scrum, the V</sub><sub>model is no longer sufficient. We realized the shortcomings of the V</sub>~model while working on a rather complex project in the autumn 2007. Keywords that illustrate the complexity of the project: remoting, integration with multiple external systems, JMS, workflow engine, webstart for deployment, multiple programming languages (C, C++, Java), multiple operating platforms (Solaris, Linux, OSX, Windows) and performance critical data processing. To handle the complexity of this system and make it testable, we developed a new test model more suitable for agile work patterns. We have split the model into three parts: 
- Part 1 explains the terminology used and introduce an categorization matrix. 
- Part 2 discuss drivers that affect test structure. We will also suggest tactics to make the mapping between requirements/user stories more explicit. 
- Part 3 shows how tests can be grouped together to make it possible to set up a fine-grained schedule which runs different groups of tests. 

## Terminology

The [V<sub>~model](http://en.wikipedia.org/wiki/V</sub>~Model_(software_development)) groups tests into **unit tests**, **integration tests**, **system tests** and **acceptance tests**.

[**Unit tests**](http://en.wikipedia.org/wiki/Unit_test) are low<sub>~level, code</sub><sub>centric tests that verify that your code behave as expected. In Java the _unit_ is usually a class. Our definition complies with the traditional one, but the delegated responsibility may differ, as explained in the [test structure section](Test</sub><sub>structure</sub><sub>and</sub><sub>Single</sub>~Responsibility-Principle.md).

[**Integration tests**](http://en.wikipedia.org/wiki/Integration_testing) verify that some set of components/modules/subsystems collaborate as expected. E.g., a test that needs a database is an intms and how we use themegration test. A test that depend on more than one component is an integration test. While the term may be valuable in an application<sub>~oriented environment, in a service</sub>~oriented environment this term is to wide and inprecise to be useful as something more than the abstract concept that everyone is familiar with. We have thus decided to exclude this term from the ubiquitous language. (**TODO**: is ubiquitous the correct description of the language used for discussing testing?) We propose the term service test instead.

**{+}Service tests{+}** are code-centric tests that ensure that a _service_ behave as expected. A service can be a _Core service (CS)_ or an _Aggregated Core Service (ACS)_. (TODO: ref to OW SOA categorization)

[**System tests**](http://en.wikipedia.org/wiki/System_testing) are [black<sub>~box tests](http://en.wikipedia.org/wiki/Black_box_testing) that verify that the system meets its functional and non</sub>~functional requirements. The goal is to ensure that _Application to Application Services (A2A)_ and _Human to Application Services (H2A)_ behave as expected. Note that system tests are often fragile due to tight binding to environment and data and are therefore the most difficult tests to write and maintain.

[**Acceptance tests**](http://en.wikipedia.org/wiki/Acceptance_test) are used by the customer to decide whether to accept a delivery or not. In spirit of the ideas from the [agile manifesto](http://agilemanifesto.org/), we boldly claim that acceptance test should be a **{_}property{_}** of a test, not a specific type or classification. In other words, the customer (business side) and the development team should work together to ensure that the tests reflect the behavior the customer wants. I.e., by increased **customer collaboration** we can get a tighter mapping between code and domain and at the same time minimize time and money spent on testing. (We work smarter, so to speak.) These concepts are derived from DDD and BBD.

**TODO**: Figur som viser forskjellen på V-model og OW Test Model.

## Categorization Matrix

The purpose of the categorization matrix is to be able to discuss and classify different kinds of tests. It is not critical whether a certain test is classified as a unit or service test, but it is important to have separate tests for with/without data and with/without environment. This makes it much easier to **write** the tests in the first place and makes it easier to work agilely.

The main drivers behind the model are
- **speed** (which restricts when it can be run),
- **with or without data** (separate datadriven tests from regular functionality tests) and
- **with or without environment** (Servlet\- and app-containers, database, JNDI, JMS, etc. highly affects the speed of the test. Tests that depend on such an environment should be separated from those that do not.)
- only maven and java should be required for running tests before check-in.
- the CI server should handle all slow tests and all tests that depend on external systems. This allows one developer or system administrator to set up external systems _once_, instead of every time a new development environment is needed. 

|  | No data | Data | No environment | Environment | Location |
| Unit Test | x | n/a | x | n/a | src/test in the same module as the unit |
| --- | --- | --- | --- | --- | --- |
| Service Test (CS) | x | x | x | x | same module as the service; it may be necessary to put slow tests in a separate directory |
| --- | --- | --- | --- | --- | --- |
| System Test (ACS/A2A) | x | x | x | x | as a separate module if it tests modules only within a project, else a separate project |
| --- | --- | --- | --- | --- | --- |
**No data**: Test with one or a few values within the interval. (Which input is not essential.)
**Data**: Test with a set of values, test with all values, test according to a given dataset (data driven)
**Environment**: Which hardware is available, which OS, etc.

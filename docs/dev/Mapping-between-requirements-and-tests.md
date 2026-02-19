# Mapping between requirements and tests

### Single<sub>~point</sub>~of-entry to requirements 

Assumption: Requirements are expressed as [user stories](User-Stories.md) (US).  

We want single point of entry to all requirements and we want a 1-1 mapping to the tests that ensure that they are fulfilled. A wiki makes the USs easily available and it is easy to add mapping (URLs) to different types of tests and test reports. 

For the component level cycle we suggest adding links to; the **test report** for the given US/test group* and a link to the **test source code and javadoc**. 
The same applies to the system level cycle, but the links don't necessarily be to source code, but can be to a description of a **manual test procedure** or a combination (link to source code + recipe) for semi-automatic tests. 

### Component level cycle 

Figure: US -> a group of tests => component release 

White-box tests can be put into groups with the group annotation in TestNG. Each US can then be mapped to one such group. And the Maven release of the module/component ensure the mapping between the tests and these groups. 

It should be possible to automate all tests in this life cycle. [Enterprise Maven Infrastructure](Enterprise<sub>~Maven</sub>~Infrastructure.md) can provide the necessary tool support for Maven-based projects. 

### System (or subsystem) level cycle

Figure: US -> group of tests -> set of released artifacts + configuration => system release 

For black-box, integration tests the picture is a bit more complex. First, these tests require that each component is _released_. In addition we need to lock down the configuration. In other words, the configuration needs to be version controlled as well. Finally, to have complete traceability the tests themselves also need to be version controlled. 

Therefore 
> ℹ️ A set of released artifacts + a configuration with a fixed version + a set of tests with a fixed version = a **system release** 

As we strive to make released artifacts backward compatible, the US (and therefore the tests) can be said to be valid for a **_ version range_** (one range is valid per artifact). 

Note! Many consider test data as a separate dimension, and it is a separate dimension. However, we can avoid an extra level here by expression the set of acceptable test data as a user story. The user story will thus have its own matching group of tests. This ensures that any change in the set of acceptable testdata which demand a change in a test will also require a new system release. 

 

In an ideal world all these tests could be automated as well. In the real world, this is seldom possible. Tests depend on different types test frameworks, and both automated, semi-automated and manual tests can (and often must) be used to cover all requirements. 

**TODO**: Which tools are relevant and what can they offer?

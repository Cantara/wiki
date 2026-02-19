# JigZaw Timeline 3

#### Motivation (hva er det vi prøver å løse) 
- When do we run service tests?
- When to run integration tests?
- When to run Selenium tests?
- What do we do with manual tests?

#### Howto (Hvordan gjør vi det?)

1. Start running all tests as often as possible. 
1. When the test suite start taking too much time, consider using the CI server to run the slowest tests. 
1. Test with special requirements with regards to test data, platform or distribution are typical candidates to move from the default test suite run by all developers to a CI server. 

#### Give me more, my problem is more complex 

- The context of the project.
- What is most important for you!
- Where do you have the most struggle with failing tests, and failing functionality today?

> 💡 Cheap, fast test to be run often.
> 💡 Expensive tests more seldom, even possibly manually.

### Webapp example
TODO: Example Gif for Web<sub>~app, with middleware and legacy systems. Developer, ci</sub>~server, test and prod-environments.

# The Theory....
```

*when should a certain group of tests be run and who is responsible for executing them*?
```

### Dimensions to consider when deciding on when to run your tests.

The following dimensions can be useful when discussing a timeline for a given context. 

| Dimension | Description |
| --- | --- |
| Development methodology | continous (in background), pre commit, post commit in CI environments (unit test, data test, out<sub>~of</sub>~process test, _some level_ of integration tests |  |
| Staging strategy | pre/post deployment to test environment, pre/post deployment to pre-production environment, pre/post deployment to production |  |
| Version Control Strategy | Central trunk/head, release branches, feature branches, distributed VCS, module artifacts |  |
| Executor | Developer, CI server, tester |  |
| Eksterne rammebetingelser | ServiceX is only available on environmentY on Wednesdays |  |

---

---

#### Examples 

###### Context description 

- Development methodology: Scrum 
- Staging strategy: Deploy to testenvironment before production (no pre-production/staging env) 
- Version Control Strategy: release branch before deploy to test env
- Accidental limitations: Only possible to integrate with service1 and service2 in a single test environment. It is not possible to obtain multiple instances of these services, nor can they be shared between multiple test environments. 

###### The chosen timeline 

![test.phase.timeline](test<sub>~phase</sub>~timeline.md)(../images/gliffy/16515318-test.phase.timeline.png)

**Within each sprint** 

- Pre-commit: developers run _mvn clean install_ 
- Post-commit: CI server run _mvn clean install -DdatabaseX -DjmsServerY_ 
- Hourly: CI server run _mvn clean install -DslowTests_

- Nightly: CI server deploy to an environment and run data-bound tests using data recorded from production (takes 4 hours) 

- End of sprint, before release: compare technical debt/accidental complexity metrics with metrics from previous release

**Before production**  

- Create a separate release branch from trunk 

- 1 week extra manual system and acceptance testing using data recorded from production 

[< Back](JigZaw<sub>~Design</sub><sub>Principles</sub><sub>and</sub>~Drivers.md) to Design Principles and Drivers   [Next >](Control-state.md) Control state

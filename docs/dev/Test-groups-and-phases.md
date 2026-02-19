# Test groups and phases

# Part 3

## Group management
Annotating tests with one or more groups makes it possible to have test runs that include group A and B, but excludes tests from group C. It is _technically_ possible to use any number of groups, but we recommend to create groups according to one or more +_dimensions_+. Dimensions should serve a concrete purpose, so do not annotate a test with a group unless you know that you need this label. Too many annotations will make group management complex and difficult to use. It is better to add more annotations later if the need arises. 

#### Dimensions 

The categorization matrix shows two dimensions we have found valuable; data/no data and environment/no environment. In addition, we suggest to to use groups to create an explicit mapping between tests and user stories, use cases or a user requirements specification. 

We have found the following dimensions to be valuable: 

| Purpose | Needed groups | Comment |
| --- | --- | --- |
| Split responsibility between developer and CI server | no data, no environment |  |  |
| Separate tests run by the CI server according to speed | long-running, performance, etc. | Sometimes the "data" group can be used |  |
| A mapping between user stories and tests | US1, US2, US3, etc. | Same can be done for use cases |
| A mapping between acceptance criteria and tests | acceptance | can be used by project managers and test managers to approve a release |  |

#### Implementation 

TestNG provides group functionality and run-time configuration to determine which groups to include in a test run. The Maven support is poor, but dimensions can be implemented with a combination of environment variables/command line parameters and Maven profiles. 

## Phases - when to run a certain group of tests 

There are two main factors that dictate _when_ a certain group of tests should be run; **speed** and **dependencies upon external systems**. The first phase is 

| 1 - **before check-in** to the Version Control System (VCS)

and is the responsibility of the developer. Since we require that developers run this set of test before every commit, it is important that this build is fast. The [One Minute Build](http://jupitermoonbeam.blogspot.com/2008/01/one-minute-build.html) might be a bit too extreme, but to our experience, the [ten minute build](http://martinfowler.com/articles/continuousIntegration.html#KeepTheBuildFast) suggested by Martin Fowler is too long. If the build is too slow, developers will either skip the tests or check-in code less often. 

After check-in, the CI server takes over. Upon check-in, or every 5 or 10 minutes, the CI server should run the tests of phase 1. This ensures that the developer gets fast feedback to his commit. The main purpose of this build definition is to quickly detect compilation and test errors caused by differences in the developer's environment and the CI server's environment. (This is one of the reasons why the CI server should have the same operating system, Java version, etc. as the production system.) 

In addition, we have identified the following the following phases: 
|2 - Multiple times a day (e.g. hourly or every second hour) 
|3 - Nightly
|4 - Weekly
|5 - Release

All unit tests, and service tests that are not extremely slow, should be run in phase 2. This ensures that developers get continuous feedback on the state of the code. 

Phase 3-5 should run tests that are too slow to run multiple times a day. This separation is introduced if it is necessary. Deployment to a test environment to allow the customer to check the system, deployment of nightly snapshots to facilitate beta-testing or deployment of technical documentation are other typical tasks suited for phase 3-5. 

Phase 3-5 is also suitable for black-box system testing and for creating reports and release candidates for management and manual Quality Assurance (QA). 

> 💡 Differentiate between systems that are within the BOUNDED CONTEXT and systems that are outside. Those within needs to be integrated much more often than those outside, because those within affect the model and the ubiquitous language. See page 343 in Eric Evans' Domain-Driven Design for details on this concept. 

#### Baseline for test categorization

Deciding when to run a certain group of tests depend on a number of factors, e.g., the capabilities of the CI server. Important and/or complex functionality should receive high priority and will thus also effect the chosen strategy. With this disclaimer, we suggest the following baseline as a starting point for new projects: 

|  | No data | Data | No environment | Environment | Location |
| Unit Test | Fast (phase 1-5) | n/a | Fast (phase 1-5) | n/a | src/test in the same module as the unit |
| --- | --- | --- | --- | --- | --- |
| Service Test (CS) | Fast (phase 1-5) | Slow (phase 2-5) | Fast (phase 1-5) | Slow (phase 2-5) | same module as the service; it may be necessary to put slow tests in a separate directory |
| --- | --- | --- | --- | --- | --- |
| System Test (ACS/A2A) | Slow (phase 2-5) | Slow (phase 2-5) | Slow (phase 2-5) | Slow (phase 2-5) | as a separate module if it tests modules only within a project, else a separate project |
| --- | --- | --- | --- | --- | --- |

This means that if possible **all unit tests** and **service tests without environment and data** should be run by the developer before checking code into the version control system. All other tests should be automated by a CI server.

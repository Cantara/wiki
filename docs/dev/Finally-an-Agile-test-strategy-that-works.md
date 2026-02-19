# Finally, an Agile test strategy! (that works)

## Title

| Finally, an Agile test strategy (that works)! |

## Speakers
 * Bård Lind (bard.lind@objectware.no)
 * Erik Drolshammer (erik.drolshammer@objectware.no)

## Abstract

Traditional test strategies were typically created in the context of a specific methodology
(like for example the waterfall model) and are unsuited for the service<sub>~oriented and test</sub>~driven
development methodologies we use today. We suggest an agile alternative based on concepts from
Domain<sub>~Driven Design, the Single</sub>~Responsibility Principle and our experiences from working agilely on
complex, distributed systems.

The test-model is founded on the concept that one complex test is harder to write and maintain than multiple smaller, more concise tests.
The goal is to design tests that have only one reason to change. To achieve this goal, we split complex
test-scenarios into dimensions like
- with or without data
- with or without a specific environment (e.g whether a JMS server or a web service is available)
- fast or slow execution time.

These dimensions are used to categorize and group the tests and makes it possible to take the Continuous Integration concept to a new level.

This test<sub>~model has proven its value in complex, real</sub>~world projects. Examples from these projects will be used
to show how this test model can be implemented with popular Open Source Software like TestNG and Maven.
We will also share experienced benefits from using this model compared to traditional test-strategies.

Keywords: DDD, TDD, Single<sub>~Responsibility</sub>~Principle, Continuous Integration, Maven, Maven artifact repository and TestNG.

Participants can expect to learn
- A new approach to testing.
- How to implement this test-model
- Real-world examples from complex projects.

## Outline

#### Introduction (5 minutes)

- A new way of thinking test
    - Grouping tests dependent on data, environment, when to run, cost of execution
    - A more precise language, common understanding in your team and with the customer
    - A test-model that makes it easier to communicate test strategies.
- Experience from multiple complex projects
- Thank you javaPils (where the discussion materialized)
- Goal: make it easier to test complex projects
- How: pragmatic approach, support agile work patterns

- Traditional test strategy descriptions
    - Webapp example
    - Integration intensive application (jms, db, multi-modules) example

#### Problem description (10 minutes)

**The problem with traditional test strategies**
- End to end testing with e.g. FitNesse
- Relaying on the data in the database.
- How do we define the content of a integration test?
- When do we run a integration test?
- How can we write integration tests that ensure user-stories are implemented correclty?
- Hard to define dependency on data and environment.
- Single tests are given too much responsibility

**The problem with complexity**
- A language of well-defined words are missing in the project.
- Complex project =>
    - Hard to discuss tests
    - Hard to write tests
    - Hard to maintain tests
    - Hard to change code

**Crucial functionality are missing tests\!**
- Because the test is too hard to write
- Because we depend on well-defined data.
- Because the test depend on some environment
- Because the test need input at test-time, to give value.
- Because the test depend on app-server, jms server ...
- Because the test depend on remoting.

**Experience**
- Development slowed down dramatically because we could not verify the functionality
- The test had too much responsibility
- Reason: tests for data, environment and logic are traditionally not separated.

#### OW test model (what) (25 min)

- A test should have only one reason to change (Single Responsibility Principle and divide<sub>~&</sub>~conquer)
    - data / no data
    - environment / no environment

- Terminology
    - get rid of unprecise terms ("integration test" must go\!)

- Categorization and test groups
    - Enable/disable tests easily
    - Put more responsibility on the Continuous Integration server
    - Prioritize which tests to write and when to run them

#### How to implement? (5 min)

- JUnit3 is not sufficient
- Need a way to group tests in multiple dimensions
- Don't abuse Maven (avoid "profile-hell")
- Maintainability and scalability are important drivers

#### Experience reports (10 minutes)

**Experience gained**
- Simplified communication in a more precise language.
- Increased number of tests
- Reduced responsibility per test
- Easier to write tests
- Easier to understand the test for complex functionality.
- Easier to maintain and change tests

**Less time spent on tests and testing.**
- Proven by metrics.

**Tests were not the pain any more. The tests improved our functionality.**
- The tests helped the developer do better coding.

#### QA (10 minutes)

## Speaker's profile

###### Bård Lind

Bård has been working with distributed computing for more than 10 years, most of these in financial enterprises. During his work he has
seen how lack of test<sub>~capabilites had a negative inpact on the end</sub>~product. 
Currently Bård works i Objectware as senior<sub>~consultant, mentor and architect. Bård is a mayor contributor to Obectware´s EA</sub>~SOA (Enterprise Architecture and SOA) Research and Development group. 

Motivating teams to work better together, and see all we can accomplish together is a major driver in Bård´s work. 

He has previously had one talk at JavaZone (2007) and two speeches for javaBin. Latest speech were on testing in javaBin-Sørlandet.

###### Erik Drolshammer

Erik holds a Masters degree in Computer Science from NTNU. His thesis was on _Improved Backward Compatibility and API Stability with Advanced Continuous Integration_ and was presented at JavaZone 2007.

Erik strives to find good (enough) solutions to reoccurring problems in software development. The last year he has concentrated on Maven, Continuous Integration and advanced testing.

Erik works as consultant in Objectware.

## Other submission data

Template: [http://www4.java.no/web/show.do?page=190](http://www4.java.no/web/show.do?page=190)

**Language**: English

**Level**: Intermediate

**Required experience**: No experience is required to benefit from the presentation, but experience from testing in an enterprise context will make it easier to grasp the concepts. 

**Expected audience**: Developers, testers, project managers, QA people

**Equipment**: Slide projector that work with both Ubuntu and OSX, and preferably a white-board.

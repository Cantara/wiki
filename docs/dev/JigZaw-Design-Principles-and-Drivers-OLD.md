# JigZaw Design Principles and Drivers - OLD

> ℹ️ Needs refactoring! 

## Dependent tests

If you want to test your database implementation you will need a database. If the database is unavailable, all database tests will fail. A developer with in-depth knowledge of the application will probably quickly come to the conclusion that the database is unavailable if a hundred DAO-tests fail, but why let 100 tests fail due to a single failure? Why not communicate that all these test depend on the database being available more directly? 

The solution is to introduce dependencies between tests. E.g., create at _testDatabaseConnectionTest_ and let all DAO-tests depend on it. All DAO-tests can thus be skipped if the _testDatabaseConnectionTest_ fail. This makes the test failure easier to debug.

See page 103 in [Next Generation Java Testing: TestNG and Advanced Concepts](http://www.amazon.com/Next-Generation-Java-Testing-Advanced/dp/0321503104) for a thorough discussion of the concept. 

## One and only one reason to change

[Single-responsibility principle (SRP)](http://www.objectmentor.com/resources/articles/srp.pdf): A test should have only one reason to change. Test code (as well as regular code) is then easier to refactor and easier to maintain. These attributes are by themselves enticing. Further, tests should be structured in such a way that if one test fails you know exactly where the problem is. This simplifies debugging, since the error message produced by the failed test explains what failed in a precise manner.

## Reduce complexity and cost 

A unit test is cheapest to write because it is the test for a single unit. A service test is cheaper than a system test for much the same reasons. Additionally, white box tests are often cheaper than black box tests, but not always. The most important reason for choosing a service test over a black box system test is that service tests are easier to **automate**. 

There is also the concept of **TDD and agile methodology**. We do not want to defer testing a system's functionality only because it is not completed yet. We want to test a function/service as early as possible. 

In other words, unit tests over service tests and service tests over system tests. 

## Mapping between user requirements and tests 

While made more explicit in BDD methodology, the concept of using the name of a method to reveal its purpose is nothing new. In fact, it might be considered a common, good programming practice. Nevertheless, by putting some effort into good naming, both code and tests alike become easier to interpret for both technical  and non-technical people.  

A mapping between tests and user requirements (for instance in the format of user stories) can be made more explicit if tests are grouped according to which requirement or user story they are relevant for. A test report sorted by group can thus be used as a means of communication between the customer and the developers. It should be possible to define a set of groups that (combined) defines the acceptance criteria for the system. A high degree of involvement and trust between customer of development team is required for this tactic to work, but the technical support already exist. (TestNG has support for test reports sorted by groups.) 

Note: The _**acceptance test report**_ and the inverse of this report should make it possible to identify functionality (and tests) that can safely be removed. And as we all know, less code means less bugs, so this bi effect has potential.  

See also [Mapping between requirements and tests](Mapping-between-requirements-and-tests.md)

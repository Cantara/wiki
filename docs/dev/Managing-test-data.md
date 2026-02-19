# Managing test data

Managing test data represents a major challenge in system development projects.

Read [Evolutionary Database Design](http://www.martinfowler.com/articles/evodb.html) from Fowler and Sadalage for some background material to the subject.  

### Use of test data

Test data is used for:
1. Unit tests
1. Integration tests
1. System tests
1. Acceptance tests and other manual testing
1. Load test
1. Migration tests (deploying new versions of a system on previous installments) 
1. Demo

### Categorization of test data types

Try minimize the number of test data sets. Often only two types of test data is sufficient:
1. A small, compact, well-known test data set that people are familiar with. Should represent all types of variations in the system, 
and the data values should mirror real data (i.e. logical, meaningful values).  
1. Volume-based set, primary for load testing purposes.

For unit testing purposes, there might be a third fragmented type of test set which serves as input data and mock data in tests.
These are implemented in test code, they are informal, and will not be used outside the unit test. 
The rest of this article will thus leave out these test data as they are of no importance for the challenge of managing test data. 

### Loading test data

Mechanisms for loading test data into a system:
1. By code
1. By database scripts
1. By a (live) master database
1. Export/import

When should you use what ?
Where are the test data stored, and in what type of format ?

### Loading frequency

How often should the test data be reloaded ?
Does it depend on the type of environment ?

How to deal with relative test dates - i.e. how to update relative date values to the current date ?

### Maintaining test data set

How to keep the test data set intact when the application is changing, 
and when developers, testers, business analysts, people in marketing, product owners, etc need new tests ?

Who should be responsible for managing the test data ?
- A single person (characteristics and roles for this person) ?
- The dev team/test team ?

How to maintain different versions of each test data set ?

### Automating the load task

How to automate this task, tools, error reporting, separate jobs in CI, dependencies ?

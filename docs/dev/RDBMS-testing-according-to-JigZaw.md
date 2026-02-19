# RDBMS testing according to JigZaw

#### Introduction 

Relational databases are and have been highly popular for a long time. This page is about how to test integration with RDBMSs when they are used for _persistence_ and _queries_. 

###### Testing against the SQL standard 
The database is considered (at least in this context) to be external to the software under test. In theory, it should be possible to accept the [International Standard for SQL (1992)](http://www.contrib.andrew.cmu.edu/~shadow/sql/sql1992.txt)) as a real, working standard. If you do, it is possible to use an in-memory database (like [HSQLDB](http://hsqldb.org/)) in tests. The advantage of this approach is speed and reduced complexity. 

###### Testing non-standard SQL functionality 
If you do not trust the vendors adherence to the SQL standard or you utilize functionality outside the standard, an external database is required. 

#### Test strategy

1. Start database (only if in-mem db is used)
1. Write a test which verifies that the connection to the database is OK. 
1. Annotate all database tests with a name that indicates that a database is required (e.g. "oracle-productName"). 
1. Make sure the following is executed before any tests in this group is run
    1. Run the database connection test 
    1. [Restore default state](Control-state.md)
1. Run tests (each test should insert test data as needed and clean up afterwards) 
1. Stop database (only if in-mem db is used)

Note a dedicated database schema/user is required for each user (developer or CI-server) which will run these tests. 

#### See also 

- [Test strategy for Oracle PL_SQL](Test<sub>~strategy</sub><sub>for</sub><sub>Oracle</sub>~PL_SQL.md) for more on how to test business logic implemented in the database

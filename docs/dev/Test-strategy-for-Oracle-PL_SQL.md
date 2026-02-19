# Test strategy for Oracle PL_SQL

#### Description 
Oracle stored procedure (or other PL_SQL code) which reads from _n_ input tables og put the results to _m_ output tables. 

Test written in plain Java running in-process. 

Primary test aspect: Automated regression test

#### Prerequisites
- A user with empty schema and privileges to **connect, resource, select any table, create procedure** 
    - unitils<sub>~4.0</sub>~SNAPSHOT does not support drop procedures/packages/functions. It is thus necessary to have access to a database _system user_ with privileges to drop user, create user and set up grants whenever pl_sql code is removed. Modified is handled as long as the code is _repeatable. 
- All PL_SQL scripts are _repeatable_ (e.g. a create or replace procedure) and terminated using "/" and a single newline at the end of the file. 

#### Howto  

###### Restore default state  

As discussed in the [RestoreDefaultState - Oracle database](RestoreDefaultState<sub>~Oracle</sub><sub>database.md) page, restoring the default state can be implemented in different ways. This recipe utilize DbMaintain which handles restore default state without relying on drop user functionality. (There are some limitations - [DBM</sub><sub>101](http://jira.unitils.org/browse/DBM</sub>~101).)

There is also a question of _how often_ it is necessary to completely wipe the database. The choices are per **TestNG group**, **class level** or **method level**. We have found that group and class level to be more appropriate than method level as we clean the data only before each test method. 

Note that tests must use different schemas if they need to be run in parallel. 

1. Add a Maven profile and TestNG configuration so this profile can be used to run tests that depend on an external database. See [TestNG run only database tests example](TestNG<sub>~run</sub><sub>only</sub><sub>database</sub><sub>tests</sub><sub>example.md) and [Unitils pom.xml example](Unitils</sub><sub>pom</sub><sub>xml</sub>~example.md).
1. Add unitils as a dependency. See [Unitils pom.xml example](Unitils<sub>~pom</sub>~xml-example.md).
1. Configure DbMaintain using Spring. See [DbMaintain example](DbMaintain-example.md).
    1. Install tables, sequences, constraints etc. 
    1. Install pl_sql code (packages, functions, triggers, views) 
    1. Insert "product data" maintained using database export tools 

###### Run test methods 

Each block of PL_SQL code (e.g. a stored procedure) should have _at least_ one test method. Multiple test methods can be used to limit the number of permutations tested in each method. Natural partitions in test data is a good indication that using multiple test methods is possible. 

Each test method is responsible for inserting the required test data and ensuring that no other test data interferes with the test. That is, clean tables before each test, not after the previous test. 

Each test is responsible for triggering the pl_sql code in question and asserting the expected state changes. 

- Insert test data for this test using Unitils @CleanInsertDataSet
    - [Unitils Test class example](Unitils<sub>~Test</sub>~class-example.md)
    - [Unitils Dataset example](http://www.unitils.org/tutorial.html#Database_testing) - Note that this is the format/syntax used in version 3.1, while this example use 4.0-SNAPSHOT

- [Call stored procedure](How<sub>~to</sub><sub>call</sub><sub>Oracle</sub><sub>stored</sub><sub>procedures</sub>~from-Java.md) 

- Verify data in database - **TODO** What is the most elegant way to assert data? 
    - Raw queries (SimpleJDBCTemplate,  rowmapper) 
    - Unitils @ExpectedDataset? 

#### Known challenges 

- [DBM<sub>~101](http://jira.unitils.org/browse/DBM</sub>~101): Unitils 4.0-SNAPSHOT does not support drop stored procedures, drop packages, drop functions. This is expected in later releases. This means that some manual intervention is required whenever pl_sql scripts are _removed_. 

#### Resources 

- [Unitils](http://www.unitils.org)

- [dbmaintain](http://www.dbmaintain.org)

- [How to call Oracle stored procedures from Java](How<sub>~to</sub><sub>call</sub><sub>Oracle</sub><sub>stored</sub><sub>procedures</sub>~from-Java.md)

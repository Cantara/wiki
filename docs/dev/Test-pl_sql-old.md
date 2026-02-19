# Test pl_sql - old

#### Description 
Stored procedure which reads from _n_ input tables og put the results to _m_ output tables. 

Test written in plain Java running in-process. 

Primary test aspect: Automated regression test

#### Prerequisites
- A user with empty schema and privileges to **connect, resource, select any table, create procedure** 
    - unitils-4.0-SNAPSHOT does not support drop procedures/packages/functions. It is thus necessary to have access to a database _system user_ with privileges to drop user, create user and set up grants whenever pl_sql code is removed. Mofied is handled as long as the code is _repeatable. 
- All PL_SQL scripts are _repeatable_ (e.g. a create or replace procedure) and terminated using "/" and a single newline at the end of the file. 

#### Strategy 

###### Restore default state  

Restore default state using the system user for each test class or group of tests. All tests within the chosen group or class must be run serially. E.g. if one group use schemaA and another group use schemaB, those two groups of tests can be run in parallell. If a single schema is employed, test cannot be run in parallell! 

The following steps must be run by the system user: 

1. drop user, create user, grants 
1. Install tables, sequences, constraints etc. 
1. Install pl_sql code (packages, functions, triggers, views) 

###### Run test methods 

Each block of PL_SQL code (e.g. a stored procedure) should have _at least_ one test method. Multiple test methods can be used to limit the number of permutations tested in each method. Natural partitions in test data is a good indication that using multiple test methods is possible. 

Each test method is responsible for inserting the required test data and ensuring that noe other test data interferes with the test. That is, clean tables before each test, not cleanup after the previous test. 

Each test is responsible for triggering the pl_sql code in question and asserting the expected state changes. (Asserting expected _behaviour_ using mocks is (to the authors knowledge) not possible when testing PL_SQL code.) 

#### Implementation 

###### Restore default state  

- Use TestNG to group together tests with similar exsternal dependencies. This allows flexibility to choose which tests are included in the default test suite run by all developers before commit, what test to be run only by CI server, etc. 

- Use @BeforeClass or @BeforeGroup to decide how when to restore the default state. 

- Use DbMaintain programatically to execute scripts. 
    - **TODO** Example code 

###### Run test methods 

- Load application context programtically to inject of resources used by the test. 

- Insert test data for this test using Unitils @CleanInsertDataSet 

- Call stored procedure using [CallableStatement](http://publib.boulder.ibm.com/infocenter/db2luw/v8/index.jsp?topic=/com.ibm.db2.udb.doc/ad/tjvcscsp.htm)

- Verify data in database 

#### Known gotchas/challenges 

- Support for drop user/create user using user with extra privileges before a group of tests is run. 
    - **TODO** Can DbMaintain via Unitils handle this?

- Find elegant way to assert correct content in database. 
    - Raw queries (SimpleJDBCTemplate,  rowmapper) 
    - Unitils @ExpectedDataset? 

- [UNI-7 Method unitilsBeforeTestSetUp() annotated with @BeforeMethod?](http://jira.unitils.org/browse/UNI-7)

#### Resources 

- [Unitils](http://www.unitils.org)

#### Ignore this 

###### Resources 

\[1\](1.md) http://www.exampledepot.com/egs/java.sql/CreateProcedureAndFunction.html 
\[2\](2.md) http://www.exampledepot.com/egs/java.sql/CallProcedure.html
\[3\](3.md) http://static.springsource.org/spring/docs/2.5.x/reference/jdbc.html#jdbc-StoredProcedure

http://tim.oreilly.com/pub/a/onjava/2003/08/13/stored_procedures.html
http://forum.springsource.org/showthread.php?t=19472

[liquibase](http://www.liquibase.org/manual/generating_changelogs)
[Oracle impdp](http://wiki.oracle.com/page/Data+Pump+Export+%28expdp%29+and+Data+Pump+Import%28impdp%29)

Ensure correct DDL in database, no data (Spring [SimpleJdbcTestUtils.executeSqlScript](http://static.springsource.org/spring/docs/3.0.x/javadoc-api/org/springframework/test/jdbc/SimpleJdbcTestUtils.html#executeSqlScript%28org.springframework.jdbc.core.simple.SimpleJdbcTemplate,%20org.springframework.core.io.Resource,%20boolean%29)) 

[Restore default state](RestoreDefaultState-Oracle-database.md)

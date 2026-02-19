# Testing DB scripts

All code needs to be tested, even the database scripts.
This page contains practices and suggestions for testing database artifacts.

This [PDF book](http://www.informit.com/store/product.aspx?isbn=032150206X) seems to contain very useful practices related to this subject,
also see [Managing test data](Managing<sub>~test</sub>~data.md).

**General recommendation**:

All artifacts should be in the form of SQL scripts managed by a source control system.
Having the master scripts in SQL instead of in database repository or in some other non-standard format makes automation and testing of these scripts much more simple. Put the scripts alongside the rest of the application's source files unless there are other dependencies of the database. 

### DDL

### Stored procedures

Try avoid using stored procedures in your system. Stored procedures are usually database vendor specific, they represent added complexity due to the introduction of another language in your system development, and it is more troublesome to test.

There exists some unit test frameworks for stored procedures, but it may be easier to create the tests in Java. This removes duplication of test running environments, collecting test results, producing reports etc.

### Migration scripts

- Naming and file structure standard for migration scripts in SCS ?
  Note that these files does not follow the same versioning as for the other source files. Each script is valid for a migration between two specific versions of the system.
- How to make migration scripts and clean install scripts synchronized ? 
  By testing both...

### Data loading scripts

### Reports

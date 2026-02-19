# System Test - Logical Overview

System tests that follow this setup can be extended to function as **Factory Acceptance Tests**! 

### Deployment made easy 

###### Install all deployment units 
- ssh app1Machine -> Use ssh to log into the machine you want to run your app 
- rpm -ivh app1.rpm -> use rpm installer to install all artifacts needed. TODO: Link to rpm instructions

This process is also possible to automate completely. TODO: How?

###### Configure all applications 

There are many beliefs on how to configure your application environment. In our opinion you must distinguish the difference between:
- Strictly confidential information, eg password and usernames. This must be stored locally on application machine.
- Environment, application configuration. This info should preferably be fetched from a ConfigService. TODO: Link to ConfigService description.

To support automatic deploy, a **ConfigService** is required.

### Automated test in a multi-node system

Our suggestion on how to automate your tests when your services and applications span over multiple machines and processes.

###### 1. Verify valid system state.

TODO: Examples on how wold be nice.
A description on how to run this verification (manually or automatically) should also be included in the [SysAdmin Production Toolbox](SysAdmin<sub>~Production</sub>~Toolbox.md). 

**Idea** Service manifesto extension: All services should include ping - "I'm alive and healthy"

###### 2. Restore default state 

Ensure that the system you want to test removes all old, uncontrolled information.

Examples are to remove all messages from all queues or drop your tables in your database.

The [Helper Libraries](Helper-Libraries.md) describes how to perform this cleanup. 

###### 3. Populate with test data 

This will ensure that your application is set to a known state before the testing begins.
Here you will also be able to populate your test database with data from the production database.

Again [Helper Libraries](Helper-Libraries.md) will help you out.

###### 4. Prepare instrumentation of your functionality.

To ensure traceability of how your system behaves during development, and for each delivery, we need to log
a few key performance indicators (KPI). Such can be successful run, number of runs, time used and memory usage.
TODO: Link to examples of KPI for a system.

###### 5. Run your test 

System specific test code. 

The system are often tested by sending some message to one application. 
Then we need to verify:
- Was the message processed by the correct applications?
- Verify that the result was correctly returned, or persisted to the expected location.

###### 6. Verify your instrumentation result

Example of verification:
- Was the massage processed in correct order, among the applications (verification of workflow).
- Are the values as we expected? Eg. if the run took more than 10 sec, then fail the test.

TODO: Example of automated verification

###### 7 Store metrics from test run in a repository 

Persist the data so it can be used for reporting and statistics.

Data to be stored:
- Name of test
- Configuration of test (eg. number of users)
- Configuration of the environment used.
- Nodes used.
- KPI result from above.
... 

### Reporting and Statistics

The metrics gathered should be used to generate reports and statistics. This will help document your project's success. 

You must do some thinking, talking and trial and error to identify which values are important to measure.
These values should be compared repeatedly during your development. The total time used for your tests to run, and the amount of memory usage will increase. We recommend that you monitor this as it progress, and assess if there are any unexpected behavior.

Other reports people might be asking for:
- Are the new system better than the old one? 
    - YOU will have to define "better".
- With configB instead of configA; has the performance of app51 increased or decreased? 
...

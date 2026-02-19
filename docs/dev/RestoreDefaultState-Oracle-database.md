# RestoreDefaultState - Oracle database

#### Drivers and rationale 

When using an Oracle database there are many ways and tools to create, delete and maintain database structure and data. Here we will describe what we have learned and why we recommend a certain setup. 

- We need +scripts+, because we want to be able to create identical databases in multiple environments. 

- Scripts must be +version controlled+, because there will be changes and we want traceability. 

- We want _separate scripts for different operations_, because this makes it easier to compare two different sets of scripts. (You can compare one logical part at a time. / Divide and conquer to reduce complexity.) 
    - Instead of creating one huge _diff_ between to sets of scripts (or databases) we have found it valuable to separate between _structure_ (schema, tables, views, indices, etc.) and _data_. We also separate between _product data_ and customer data. The first is configuration and basic settings required for the application to work. This settings (at least their default values) are owned by the developers or product owner of the application. Regular data (whether it is production data or test data) is owned by the user/customer. 
    - Another reason for this separation is that it often is necessary to use different tools for administration.  

- We prefer +tools with good support for automated tests+ whenever they can be used (e.g is not too slow). 
    - This means that whenever possible we try to use categorization, formats and tools that makes it easier to write automated tests. This means that we will prefer a slower tool/approach to the most optimal one, if the speed is _good enough_ for our needs. This can also means that we will minimize the dataset volume at some test levels to increase speed. 
    - This also means that we should structure the scripts so it is possible to remove and reinsert data and reinitialize for example sequences, without being forced to recreate everything. In other words, we must create a structure that is flexible enough to allow optimizing test runtime according to the level of trust/confidence we need that the results are accurate. Unit and service tests will thus probably utilize JDBC and must live with the limitations inferred by JDBC. System tests and performance tests will often require more data and _impdp_ or _imp_ might thus be better choices. 

#### Restore default state with administrative privileges 

In Oracle (at least in this context) a _schema_ and a _user_ is identical. The best way to get a fresh start is therefore to delete and recreate the user. 

###### First time setup 

0. Create tablespaces for data and indices 
1. Create user and add grants 
2. Create tables, views, indices, etc. 
3. Insert product data 
4. Insert data  

###### Regular restore default state

1. drop user app1User cascade; 
2. Create user and add grants 
3. Create tables, views, indices, etc. 
4. Insert product data 
5. Insert data 
 

#### Restore default state with minimum privileges 
Often system administrators and DBAs don't like to give developers enough privileges to drop and create users. We are thus forced to try to maintain scripts which clean up every thinkable change we do. This is a lousy setup, but often it is the best we can do. 

###### First time setup 

Tablespaces, user and grants have been created by some DBA. 

1. Create tables, views, indices, etc. 
2. Insert product data 
3. Insert data 
 
###### Regular restore default state

1. Manually drop tables, views, indices, etc. 
2. Create tables, views, indices, etc. 
3. Insert product data 
4. Insert data 

###### clean data and history 

1. delete content from tables, reset sequences, etc. 
2. insert product data 
3. Insert data  

#### Tools 

| Operation | Tools | Comment |
| --- | --- | --- |
| Create tablespaces and users | **sqlplus** (is this possible with JDBC?) |  |  |
| Create users | **sqlplus** (is this possible with JDBC?) |  |  |
| Create tables, views, indices | **JDBC**, **sqlplus** |  |  |
| Insert product data | **JDBC**, **sqlplus** |  |
| Insert data | **JDBC**, **sqlplus**, **impdp**, **imp** |  |  |

**TODO**: Check JDBC's support for creatings users and adding grants and other more advanced operations. 

If your tests are in Java, JDBC should be preferred if JDBC can do the job, because this simplifies automation. 

- [JDBC](http://java.sun.com/javase/6/docs/technotes/guides/jdbc/)
- [sqlplus](http://www.oracle.com/technology/tech/sql_plus/index.html)
- [impdp](http://www.oracle-base.com/articles/10g/OracleDataPump10g.php)
- [imp](http://www.orafaq.com/wiki/Import_Export_FAQ)

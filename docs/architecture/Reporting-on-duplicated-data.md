# Reporting on duplicated data

#### Use case description 

1. Some physical units generate data. 
1. Data is put into a JMS Queue. 
1. Consumers of the data 
    1. Web application 
        1. Admin of physical units. 
        1. Live queries 
        1. 
    1. Application for providing reports on the data. 
1. User should only have one username and password for authentication. 
1. Users are only allowed to see data for her own units.  
1. It should be possible to download a report from the web application. 
1. Creating new reports may require experts/developers/dbas, but it should not be necessary to restart the web application to get hold of a new report. 

- Let's assume we want to use a commercial tool to do data mining and reporting. 
- Use an off-the-shelf BI/reporting tool to generate reports. 

###### MS SQL Server 

http://stackoverflow.com/questions/789616/sql-server-services-overview-anyone

- Reporting Services (or SSRS)
    - a 'tweaked' version of Visual Studio to make creating/developing/editing these reports much easier. That version of visual studio is called SQL Server Business Intelligence Design Studio (or BIDS). 

- Analysis Services 

#### How to maintain a duplicated version of the master data 

###### Alt 1 - DB vendor way 

- Use RDBMS functionality to duplicate data from one database to another. 
    - On update/insert 
    - Scheduled sync (e.g. nightly) 

###### Alternative 2 - the developer way 

- Polyglot persistence 

#### Integrate reports in web app 

- How easy is it to fetch the reports from the commercial tool from the web application? 
- Can the two data models diverge or is that a problem?

# Mutiple backend repositories scenario

#### One example scenario 

- Application authentication 
    - Local (controlled by Whydah) SQL db for _application_ authentication 

- Application data 
    - Local (controlled by Whydah) SQL db for roles and properties for _applications_

- User Authentication 
    - External, existing AD for user authentication for Norway 
    - External, existing AD for user authentication for Asia 
    - Local (controlled by Whydah) LDAP for _user_ authentication 

- User data 
    - Local (controlled by Whydah) SQL db for roles and properties for _users_

###### Implementation / deployment decisions 

- Integrate with two external AD servers 

- One local LDAP server

- One SQL database, separate tables for user data, application data, application authentication 

#### Design suggestion 

Inspiration: http://soapatterns.org/candidate_patterns/enterprise_domain_repository

Goal: support multiple providers for authentication and data/roles for both users and applications. 

User/ApplicationAggregateService is responsible for querying authentication and dataproviders to assemble a user/application aggregate. The aggregate contains user/application properties, roles and other authorization data. Each provider can be instantiated several times to support multiple repositories. 

Supported user authentication backends: LDAP (ApacheDS), AD 
Supported application authentication backends: SQL
Supported data backends: SQL (hsqldb, postgres and MS SQL Server), HashMapStores? 

LDAP provider supports both AD and LDAP. 
The SQL provider supports several RDBMSs, more implementation specific providers will be added if necessary. 

The AggregateService is also responsible for ordering the providers, e.g. which Provider to query for data first. The aggregate contains information from a single authenticationProvider and a single dataProvider. The merge of data from different authentication/data providers is, for now at least, not supported. It is expected to create different applications/users instead. 

- UserAggregateService
    - LdapUserAuthenticationProvider 
    - SqlUserDataProvider 

- ApplicationAggregateService
    - SqlApplicationAuthenticationProvider 
    - SqlApplicationDataProvider 

### References
- Definition of InetOrgPerson: [http://tools.ietf.org/html/rfc2798](http://tools.ietf.org/html/rfc2798)
- Easily digested info on InetOrgPerson: [http://ldap.akbkhome.com/index.php/objectclass/inetOrgPerson.html](http://ldap.akbkhome.com/index.php/objectclass/inetOrgPerson.html)

# UIB Data storage - persistence

*[Diagram: uib-persistence]*

### Storage options for UserIdentityBackend

- Authentication storage
  - [ApacheDS](http://directory.apache.org/apacheds/) v1.5.7
  - AD

- Authorization storage
  - [MS SQL Server](https://www.microsoft.com/en-us/sqlserver)
    - [JTDS](http://jtds.sourceforge.net/) v1.2.4?
  - [HSQLDB](http://hsqldb.org/) v2.0.0
  - [PostgreSQL](http://www.postgresql.org/) JDBC driver 9.3-1100-jdbc41

### Schemas and datastructures

###### Application authentication

###### Application data

SQL

###### Organization Data (contracts/agreements)

###### Auditlog

###### User authentication

**LDAP [InetOrgPerson - LDAP Usage](/web/20210624223508/https://wiki.cantara.no/display/whydah/InetOrgPerson+-+LDAP+Usage "InetOrgPerson - LDAP Usage")**

- More on *InetOrgPerson: <http://ldap.akbkhome.com/index.php/objectclass/inetOrgPerson.html>*

###### User data - Properties (Often referred to as roles in IAM context)

###### Properties (Often referred to as rolenames)
